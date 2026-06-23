"""
Data Quality Validation Rules
"""

import pandas as pd


def dq01_pk_uniqueness(df, pk_column):
    duplicates = df[df.duplicated(pk_column, keep=False)]

    if len(duplicates) == 0:
        print(f"✅ DQ-01 Passed: {pk_column} is unique")
    else:
        print(f"❌ DQ-01 Failed: Duplicate values found in {pk_column}")
        print(duplicates[[pk_column]])
def dq02_composite_pk(df, columns):
    duplicates = df[df.duplicated(columns, keep=False)]

    if duplicates.empty:
        print(f"✅ DQ-02 Passed: {columns} unique")
    else:
        print(
            f"❌ DQ-02 Failed: "
            f"{len(duplicates)} duplicate rows found"
        )

        print(
            duplicates[columns]
            .drop_duplicates()
            .head(10)
        )

def dq06_positive_sales(df):
    if "sales" not in df.columns:
        print("⚠️ sales column not found")
        return

    invalid = df[df["sales"] <= 0]

    if len(invalid) == 0:
        print("✅ DQ-06 Passed: All sales values positive")
    else:
        print(f"❌ DQ-06 Failed: {len(invalid)} invalid rows")
def dq03_fk_integrity(
    child_df,
    parent_df,
    child_key,
    parent_key
):
    invalid = child_df[
        ~child_df[child_key]
        .isin(parent_df[parent_key])
    ]

    if invalid.empty:
        print(
            f"✅ DQ-03 Passed: "
            f"All {child_key} values valid"
        )
    else:
        print(
            f"❌ DQ-03 Failed: "
            f"{len(invalid)} invalid rows"
        )

        print(
            invalid[[child_key]]
            .drop_duplicates()
        )
def save_validation_failure(
    rule_id,
    severity,
    description,
    records
):
    df = pd.DataFrame({
        "rule_id": [rule_id],
        "severity": [severity],
        "description": [description],
        "records": [str(records)]
    })

    df.to_csv(
        "output/validation_failures.csv",
        mode="a",
        header=not pd.io.common.file_exists(
            "output/validation_failures.csv"
        ),
        index=False
    )