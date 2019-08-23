import blockSQL


def createTable(connection : blockSQL.Connection) -> None:
    connection.execute("""
    CREATE TABLE customer (
        customerID INTEGER PRIMARY KEY AUTOINCREMENT,
        customerName TEXT,
        hositalID INTEGER,

    )
    """)