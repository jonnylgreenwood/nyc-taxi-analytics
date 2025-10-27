# 🗄️ Schema: `dq`

## 📊 Tables

| Table | Row Count |
|------|-----------|
| `ingestion_plan` | 12 |

---
## `ingestion_plan`

**Row count:** 12

| Column | SQL Type | Length | Count | Nulls | Unique | Min | Max | Sample |
|--------|-----------|--------|-------|-------|--------|-----|-----|--------|
| `file_month` | VARCHAR | 255 | 12 | 0 | 12 |  |  | ['2025-01', '2025-04', '2025-07'] |
| `file_path` | VARCHAR | 255 | 12 | 0 | 12 |  |  | ['data/raw/yellow_tripdata_2025-01.parquet', 'data/raw/yellow_tripdata_2025-04.parquet', 'data/raw/yellow_tripdata_2025-07.parquet'] |
| `is_loaded` | BOOLEAN | 1 | 12 | 0 | 1 | True | True | [True] |
| `loaded_at` | UNKNOWN |  | 12 | 0 | 12 |  |  | [Timestamp('2025-10-27 13:54:39.667795'), Timestamp('2025-10-27 13:54:40.624116'), Timestamp('2025-10-27 13:54:41.538830')] |

---
