# -*- coding: utf-8 -*-
"""
Created on Fri Jul 11 10:58:56 2025

@author: Tim w/ Janet
"""

from pathlib import Path
from marian_utils import load_and_clean_data, extract_minimal_metadata, save_to_json

# Constants
INPUT_FILE  = Path("../data/librarything_tgraettinger.xlsx")
OUTPUT_FILE = Path("../data/marian_knowledge_base.json")

# Load, clean, and process
df = load_and_clean_data(INPUT_FILE)
metadata = extract_minimal_metadata(df)
save_to_json(metadata, OUTPUT_FILE)

print(f"Processed {len(metadata['books'])} books and saved to {OUTPUT_FILE}")
