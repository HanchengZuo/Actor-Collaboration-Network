# processing_functions.py

def keep_top_five_actors(cast):
    return str(cast.strip("[]").replace("'", "").split(", ")[:5])

def process_row(row):
    row['Cast'] = keep_top_five_actors(row['Cast'])
    return row
