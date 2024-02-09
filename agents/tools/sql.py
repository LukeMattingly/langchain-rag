import sqlite3 
from langchain.tools import Tool

conn = sqlite3.connect('db.sqlite')

def run_sqlite_query(query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

run_query_tool = Tool.from_function(
    name="run_sqlite_query",
    description="run a sqlite query from a database",
    func=run_sqlite_query,
)