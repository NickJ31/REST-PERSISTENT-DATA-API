import sqlite3

conn = sqlite3.connect("clinical_data.db")
existing_columns = {row[1] for row in conn.execute("PRAGMA table_info(clinical_data)")}
new_columns = {
    "blood_pressure": "VARCHAR",
    "heart_rate": "INTEGER",
    "medications": "VARCHAR",
}
for column, type_ in new_columns.items():
    if column not in existing_columns:
        conn.execute(f"ALTER TABLE clinical_data ADD COLUMN {column} {type_}")
conn.commit()
conn.close()
print("Database migration completed successfully.")
