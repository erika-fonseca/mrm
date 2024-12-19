# Databricks notebook source
# MAGIC %md
# MAGIC # Exporting Datasets to pdf
# MAGIC
# MAGIC The solution to display big tables in pdf is to split the dataframe into smaller tables and display them one below the other.
# MAGIC
# MAGIC This implementation considers datasets that fit in memory, for big data the solution is to provide a read-only version of a file.

# COMMAND ----------

import pandas as pd

def split_dataframe_with_index(df, row_chunk_size, col_chunk_size):
    """
    Split a DataFrame into smaller chunks for both rows and columns, 
    preserving the index to uniquely identify all records.
    
    Args:
        df (pd.DataFrame): The DataFrame to split.
        row_chunk_size (int): Number of rows per smaller table.
        col_chunk_size (int): Number of columns per smaller table.
    """
    
    css = '''table table-striped table-hover; html {
    font-family: sans-serif;
    -ms-text-size-adjust: 100%;
    -webkit-text-size-adjust: 100%;
    }'''
    row_chunks = range(0, len(df), row_chunk_size)
    col_chunks = range(0, len(df.columns), col_chunk_size)

    # Save the output to a file
    with open(f"exports/data/tables.html", "w", encoding="utf-8") as f:
        f.write('''
                <html>
                <head>
                </head>
                <body class = "tbl">
                <div>
                <h5>Table: Demo Dataset Exported as Table</h5>
                ''')
        for row_start in row_chunks:
            for col_start in col_chunks:
                # Slice rows and columns
                chunk = df.iloc[row_start:row_start + row_chunk_size, col_start:col_start + col_chunk_size]
                f.write(f"<div>Rows {row_start} to {min(row_start + row_chunk_size - 1, len(df) - 1)}, "
                    f"Columns {col_start} to {min(col_start + col_chunk_size - 1, len(df.columns) - 1)}</div>")
                f.write(chunk.to_html(index=False, classes=css))
        f.write('''
                </div>
                </body>
                </html>''')

df = spark.sql('select * from samples.bakehouse.sales_customers').toPandas().head(200)

# Split the DataFrame into chunks with 3 rows and 2 columns each
split_dataframe_with_index(df, row_chunk_size=30, col_chunk_size=6)
