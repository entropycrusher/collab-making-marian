# -*- coding: utf-8 -*-
"""
Created on Fri Jul 11 10:59:53 2025

@author: Tim w/ Janet
"""

import pandas as pd
import json

def load_and_clean_data(file_path):
    df = pd.read_excel(file_path)

    # Clean page count (remove preface if semicolon present)
    def clean_page_count(val):
        if pd.isna(val):
            return None
        if ";" in str(val):
            try:
                return int(str(val).split(";")[1].strip())
            except ValueError:
                return None
        try:
            return int(val)
        except ValueError:
            return None

    df["Clean Page Count"] = df["Page Count"].apply(clean_page_count)
    return df

def extract_minimal_metadata(df):
    books = []
    skipped = []

    for i, row in df.iterrows():
        if pd.isna(row["Title"]) or pd.isna(row["Primary Author"]):
            skipped.append(i)
            continue

        book = {
            "title": row["Title"],
            "author": row["Primary Author"],
            "rating": float(row["Rating"]) if not pd.isna(row["Rating"]) else None,
            "review": row["Review"] if not pd.isna(row["Review"]) else "",
            "tags": [tag.strip() for tag in str(row["Tags"]).split(",")] if not pd.isna(row["Tags"]) else [],
            "date_started": str(row["Date Started"]) if not pd.isna(row["Date Started"]) else None,
            "date_read": str(row["Date Read"]) if not pd.isna(row["Date Read"]) else None
        }

        books.append(book)

    print(f"Skipped {len(skipped)} rows (missing title/author). Row indices: {skipped}")
    return {"books": books}

def save_to_json(data, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
