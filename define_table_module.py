import blockSQL

def createTable(connection : blockSQL.Connection) -> None:
    connection.execute("""
    CREATE TABLE customer (
        customerID INTEGER PRIMARY KEY AUTOINCREMENT,
        customerName TEXT,
        customerAddress TEXT,
        customerPhoneNumber TEXT
    )
    """)
    connection.execute("""
    CREATE TABLE medical_record(
        medical_recordID INTEGER PRIMARY KEY AUTOINCREMENT,
        customerID INTEGER,
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
