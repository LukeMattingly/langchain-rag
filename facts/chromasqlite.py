import sqlite3

# Connect to the Chroma database
conn = sqlite3.connect('emb/chroma.sqlite3')
cursor = conn.cursor()

'''
# Get a list of tables in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in the database:", tables)

# Describe the structure of each table
for table in tables:
    cursor.execute(f"PRAGMA table_info({table[0]});")
    columns = cursor.fetchall()
    print(f"\nColumns in table '{table[0]}':")
    for column in columns:
        print(column)

conn.close()

'''
# Execute the query to retrieve all documents
cursor.execute("SELECT * FROM embedding_fulltext_search")

# Fetch all results
documents = cursor.fetchall()

# Process the documents
for document in documents:
    print(document)  # Example: printing each document

# Close the connection
conn.close()
