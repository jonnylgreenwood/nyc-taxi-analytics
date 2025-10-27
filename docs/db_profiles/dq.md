# 🗄️ Schema: `dq`

## 📊 Tables

| Table | Row Count |
|------|-----------|
| `ingestion_plan` | 36 |

---
## `ingestion_plan`

**Row count:** 36

| Column | SQL Type | Length | Count | Nulls | Unique | Min | Max | Sample |
|--------|-----------|--------|-------|-------|--------|-----|-----|--------|
| `service_type` | VARCHAR | 255 | 36 | 0 | 3 |  |  | ['yellow', 'green', 'fhv'] |
| `file_month` | VARCHAR | 255 | 36 | 0 | 12 |  |  | ['2024-10', '2024-11', '2024-12'] |
| `file_path` | VARCHAR | 255 | 36 | 0 | 36 |  |  | ['data/raw/yellow_tripdata_2024-10.parquet', 'data/raw/yellow_tripdata_2024-11.parquet', 'data/raw/yellow_tripdata_2024-12.parquet'] |
| `is_loaded` | BOOLEAN | 1 | 36 | 0 | 1 | True | True | [True] |
| `loaded_at` | UNKNOWN |  | 36 | 0 | 12 |  |  | [Timestamp('2025-10-27 16:49:07.319597'), Timestamp('2025-10-27 16:49:07.928027'), Timestamp('2025-10-27 16:49:08.579246')] |

---
