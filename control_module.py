import blockSQL

def insertCustomer(connection : blockSQL.Connection, name : str, address : str, phoneNumber : str, id = 0) -> blockSQL.Cursor:
    """고객을 추가합니다."""
    if(id > 0):
        return connection.execute("""
        INSERT INTO customer
        VALUES ({0}, "{1}", "{2}", "{3}")
        """.format(id, name, address, phoneNumber))
    else:
        return connection.execute("""
        INSERT INTO customer (customerName, customerAddress, customerPhoneNumber)
        VALUES ("{0}", "{1}", "{2}")
        """.format(name, address, phoneNumber))

def updateCustomer(connection : blockSQL.Connection, id : int, name = "", address = "", phoneNumber = "")->blockSQL.Cursor:
    """고객을 업데이트 합니다.
    id를 제외한 컬럼들은 빈 텍스트가 오면 그 컬럼은 업데이트 하지 않습니다."""
    set_SQL = ""
    if(name != ""):
        set_SQL += " customerName = '" + name + "',"
    if(address != ""):
        set_SQL += " customerAddress = '" + address + "',"
    if(phoneNumber != ""):
        set_SQL += " customerPhoneNumber = '" + phoneNumber + "'"
    if(set_SQL[-1] == ','):
        set_SQL = set_SQL[:-1]
    return connection.execute("""
    UPDATE customer
    SET{1}
    WHERE customerID = {0}""".format(id, set_SQL))

def insertHospital(connection : blockSQL.Connection, name : str, address : str, id = 0) -> blockSQL.Cursor:
    """병원을 추가합니다. id가 0이면 자동 배정됩니다."""
    if(id == 0):
        return connection.execute("""
        INSERT INTO hospital (hospitalName, hospitalAddress)
        VALUES ("{0}", "{1}")
        """.format(name, address))
    else:
        return connection.execute("""
        INSERT INTO hospital
        VALUES ({0}, "{1}", "{2}")
        """.format(id, name, address))

def updateHospital(connection : blockSQL.Connection, id : int, name = "", address = "") -> blockSQL.connection_module:
    """병원을 업데이트 합니다"""
    set_SQL = ""
    if(name != ""):
        set_SQL += " hospitalName = '" + name + "',"
    if(address != ""):
        set_SQL += " hospitalAddress = '" + address + "'"
    if(set_SQL[-1] == ','):
        set_SQL = set_SQL[:-1]
    return connection.execute("""
    UPDATE hospital
    SET{1}
    WHERE hospitalID = {0}
    """.format(id, set_SQL))

def insertMedicalRecord(connection : blockSQL.Connection, customerID : int, hospitalID : int, disease : str, prescription : str, date : int, id = 0) -> blockSQL.Cursor:
    """병력 기록을 추가합니다."""
    if(id == 0):
        return connection.execute("""
        INSERT INTO medical_record ( customerID, hospitalID, disease, prescription, date)
        VALUES ({0}, {1}, "{2}", "{3}", {4})
        """.format(customerID, hospitalID, disease, prescription, date))
    else:
        return connection.execute("""
        INSERT INTO medical_record
        VALUES ({0}, {1}, {2}, "{3}", "{4}", {5})
        """.format(id, customerID, hospitalID, disease, prescription, date))

def updateMedicalRecord(connection : blockSQL.Connection, id : int, customerID = "", hospitalID = "", disease = "", prescription = "", date = 0) -> blockSQL.Cursor:
    """병력 기록을 수정합니다."""
    set_SQL = ""
    if(customerID != ""):
        set_SQL += " customerID = " + str(customerID) + ','
    if(hospitalID != ""):
        set_SQL += " hospitalID = " + str(hospitalID) + ','
    if(disease != ""):
        set_SQL += " disease = '" + disease + "',"
    if(prescription != ""):
        set_SQL += " prescription = '" + prescription + "',"
    if(date != 0):
        set_SQL += " date = " + str(date)
    
    if(set_SQL[-1] == ','):
        set_SQL = set_SQL[:-1]

    return connection.execute("""
    UPDATE medical_record
    SET{1}
    WHERE medical_recordID = {0}
    """.format(id, set_SQL))
