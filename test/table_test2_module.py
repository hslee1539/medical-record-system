import os, sys
sys.path.append(os.path.dirname(__file__) + "{0}..{0}..".format(os.path.sep))

import medical_record_system
import blockSQL
import random
import time

connection = blockSQL.Connection(":memory:")
medical_record_system.define_table_module.createTable(connection)

customerNameList = ['홍길동', '이희수','스티브잡스','빌게이츠','주몽','세종','단군','백설','시진핑','모세']
addressList = ['대한민국 서울', '대한민국 수원', '대한민국 천안', '대한민국 공주', '대한민국 대전', '대한민국 세종', '대한민국 부산', '일본 도쿄', '미국 LA', '미국 뉴욕', '이탈리아 로마']
diseaseList = ['폐암','감기','독감','위암','식중독','위염','pnoumonoultramicroscopicsilicovolcanoconiosis','충치']
prescriptionList = ['빨간약','비타민','진통제','후시딘','게보린','이가탄','인삼']
hospitalNameList = ['대한','우리','최고', '전통', 'LA']
hospitalClassList = ['종합병원','치과','내과','외과','이빈후과','한의원']

hospitalCount = 0
customerCount = 0

def display():
    print("------------------------------------------------")
    print("고객 (id, name, hospital id, 병, 처방, 날자 순)")
    tmp = connection.execute("""
    SELECT *
    FROM customer
    """).fetchall()
    for row in tmp:
        print(row)
    
    print("------------------------------------------------")
    print("병원 (id, name, 주소 순)")
    tmp = connection.execute("""
    SELECT *
    FROM hospital
    """).fetchall()
    for row in tmp:
        print(row)

    print("------------------------------------------------")
    print("고객_history (history_id, sqlTime, isCompleted, id, name, hospital id, 병, 처방, 날자 순)")
    tmp = (connection.execute("""
    SELECT *
    FROM customer_history
    """).fetchall())
    for row in tmp:
        print(row)

    print("------------------------------------------------")
    print("병원_history (history_id, sqlTime, isCompleted,id, name, 주소 순)")
    tmp = (connection.execute("""
    SELECT *
    FROM hospital_history
    """).fetchall())
    for row in tmp:
        print(row)

    print("------------------------------------------------")
    print("block (id, historyID, 테이블 명, 암호화된 데이터, 해시, 완료 시간 순)")
    tmp = (connection.execute("""
    SELECT *
    FROM block
    """).fetchall())
    for row in tmp:
        print(row)

def newHospital():
    global hospitalCount
    connection.execute("""
    INSERT INTO hospital (hospitalName, hospitalAddress)
    VALUES ( "{0}", "{1}" )
    """.format(hospitalNameList[random.randint(0, len(hospitalNameList) -1)]\
               + hospitalClassList[random.randint(0, len(hospitalClassList) -1 )],\
        addressList[random.randint(0,len(addressList) - 1)]))
    display()
    hospitalCount += 1

def newCustomer():
    global customerCount
    connection.execute("""
    INSERT INTO customer (customerName, hospitalID, disease, prescription, date)
    VALUES ( "{0}", {1}, "{2}", "{3}", {4} )
    """.format(\
        customerNameList[random.randint(0,len(customerNameList) -1)],\
        random.randint(1,hospitalCount),\
        diseaseList[random.randint(0,len(diseaseList) -1)],\
        prescriptionList[random.randint(0,len(prescriptionList) -1)],\
        int(time.time())))
    display()
    customerCount += 1

def customer_go_hospital(customerID : int):
    connection.execute("""
    UPDATE customer
    SET hospitalID = {0}, disease = "{1}", prescription = "{2}", date = {3}
    WHERE customerID = {4}
    """.format(random.randint(1, hospitalCount), diseaseList[random.randint(0,len(diseaseList)-1)], prescriptionList[random.randint(0,len(prescriptionList)-1)], int(time.time()), customerID))
    display()

newHospital()
newCustomer()
customer_go_hospital(random.randint(1, customerCount))