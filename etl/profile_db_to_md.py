import duckdb
import pandas as pd
from pathlib import Path
import re

# --- CONFIG ---
DB_PATH = "etl/analytics.duckdb"
SCHEMAS_TO_PROFILE = ["l0", "l1", "l2", "dq"]  # control what layers you want to export

wiki_path = Path("docs/db_profiles")
wiki_path.mkdir(parents=True, exist_ok=True)

PANDAS_TO_SQL = {
    "object": ("VARCHAR", 255),
    "string": ("VARCHAR", 255),
    "int64": ("BIGINT", 8),
    "int32": ("INTEGER", 4),
    "float64": ("DOUBLE", 8),
    "bool": ("BOOLEAN", 1),
    "datetime64[ns]": ("TIMESTAMP", None),
}

def profile_table(con, full_name):
    cols_df = con.execute(f"DESCRIBE {full_name}").fetch_df()
    profiles = []

    for _, row in cols_df.iterrows():
        col = row["column_name"]
        s = con.execute(f"SELECT {col} FROM {full_name}").fetch_df()[col]
        # s = con.execute(f"SELECT {col} FROM {full_name} LIMIT 50000").fetch_df()[col]

        pd_type = str(s.dtype)
        sql_type, size = PANDAS_TO_SQL.get(pd_type, ("UNKNOWN", None))
        
        profiles.append({
            "Column": col,
            "SQLType": sql_type,
            "Length": size if size else "",
            "Count": len(s),
            "Nulls": s.isna().sum(),
            "Unique": s.nunique(dropna=True),
            "Min": s.min() if pd.api.types.is_numeric_dtype(s) else "",
            "Max": s.max() if pd.api.types.is_numeric_dtype(s) else "",
            "Sample": str(s.dropna().unique()[:3].tolist())
        })

    return pd.DataFrame(profiles)

con = duckdb.connect(DB_PATH, read_only=True)

for schema in SCHEMAS_TO_PROFILE:
    print(f"📚 Profiling schema `{schema}`")
    
    tables = con.execute(f"""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema='{schema}'
          AND table_type='BASE TABLE'
    """).fetchdf()["table_name"]

    md = f"# 🗄️ Schema: `{schema}`\n\n"
    md += "## 📊 Tables\n\n| Table | Row Count |\n|------|-----------|\n"

    table_info = []

    for tbl in tables:
        full_name = f"{schema}.{tbl}"
        try:
            count = con.execute(f"SELECT COUNT(*) FROM {full_name}").fetchone()[0]
            md += f"| `{tbl}` | {count:,} |\n"
            table_info.append((tbl, full_name, count))
        except Exception as e:
            print(f"⚠️ Skipping {tbl}: {e}")

    md += "\n---\n"

    for tbl, full_name, row_count in table_info:
        print(f"  🧩 Profiling {full_name}")
        prof = profile_table(con, full_name)

        md += f"## `{tbl}`\n\n"
        md += f"**Row count:** {row_count:,}\n\n"
        md += "| Column | SQL Type | Length | Count | Nulls | Unique | Min | Max | Sample |\n"
        md += "|--------|-----------|--------|-------|-------|--------|-----|-----|--------|\n"

        for _, r in prof.iterrows():
            md += f"| `{r['Column']}` | {r['SQLType']} | {r['Length']} | {r['Count']:,} | {r['Nulls']:,} | {r['Unique']:,} | {r['Min']} | {r['Max']} | {r['Sample']} |\n"

        md += "\n---\n"

    out_path = wiki_path / f"{schema}.md"
    out_path.write_text(md)
    print(f"✅ Wrote {out_path}")

con.close()
print("✨ Schema profiling complete!")
