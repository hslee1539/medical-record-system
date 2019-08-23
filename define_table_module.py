import blockSQL

def createTable(connection : blockSQL.Connection) -> None:
    connection.execute("""
    CREATE TABLE customer (
        customerID INTEGER PRIMARY KEY AUTOINCREMENT,
        customerName TEXT,
        hospitalID INTEGER,
        disease TEXT,
        prescription TEXT,
        date INTEGER
    )
    """)
    connection.execute("""
    CREATE TABLE hospital (
        hospitalID INTEGER PRIMARY KEY AUTOINCREMENT,
        hospitalName TEXT,
        hospitalAddress TEXT
    )
    """)
