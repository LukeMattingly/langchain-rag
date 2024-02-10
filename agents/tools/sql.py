import sqlite3 
from langchain.tools import Tool
from pydantic.v1 import BaseModel
from typing import List 

conn = sqlite3.connect('db.sqlite')

def list_tables():
    cursor = conn.cursor()
    rows = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    return "\n".join(row[0] for row in rows if row[0] is not None)

def run_sqlite_query(query):
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        return cursor.fetchall()
    except sqlite3.OperationalError as e:
        return f"The following error occured:{e}"

class RunQueryArgsSchema(BaseModel):
    query: str

run_query_tool = Tool.from_function(
    name="run_sqlite_query",
    description="run a sqlite query from a database",
    func=run_sqlite_query,
    args_schema=RunQueryArgsSchema,
)

def describe_tables(table_names):
    cursor = conn.cursor()
    tables = ', '.join("'" + table + "'" for table in table_names)
    rows = cursor.execute(f"SELECT sql FROM sqlite_master WHERE type='table' and name in ({tables});")
    return "\n".join(row[0] for row in rows if row[0] is not None)

class DescribeTablesArgsSchema(BaseModel):
    table_names: List[str]

describe_tables_tool = Tool.from_function(
    name="describe_tables",
    description="Given a list of table names, return a description of each table",
    func=describe_tables,
    args_schema=DescribeTablesArgsSchema,
)