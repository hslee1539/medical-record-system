import os, sys
sys.path.append(os.path.dirname(__file__) + "{0}..{0}..".format(os.path.sep))

import random
import time
import blockSQL
import medical_record_system

customerNameList = ['홍길동', '이희수','스티브잡스','빌게이츠','주몽','세종','단군','백설','시진핑','모세']
addressList = ['대한민국 서울', '대한민국 수원', '대한민국 천안', '대한민국 공주', '대한민국 대전', '대한민국 세종', '대한민국 부산', '일본 도쿄', '미국 LA', '미국 뉴욕', '이탈리아 로마']
diseaseList = ['폐암','감기','독감','위암','식중독','위염','pnoumonoultramicroscopicsilicovolcanoconiosis','충치']
prescriptionList = ['빨간약','비타민','진통제','후시딘','게보린','이가탄','인삼']
hospitalNameList = ['대한','우리','최고', '전통', 'LA']
hospitalClassList = ['종합병원','치과','내과','외과','이빈후과','한의원']
phoneNumberList = ['+8212345678', '+1012345679', '+0112345679', '+5512345679']

connection = blockSQL.Connection(":memory:")

medical_record_system.define_table_module.createTable(connection)

customerCount = 0
hospitalCount = 0
medical_recordCount = 0

def randomNewCustomer():
    global customerCount
    customerCount += 1
    medical_record_system.control_module.insertCustomer(connection, customerNameList[random.randint(0, len(customerNameList) -1)], addressList[random.randint(0, len(addressList)-1)], phoneNumberList[random.randint(0,len(phoneNumberList) -1)])

def randomNewHospital():
    global hospitalCount
    hospitalCount += 1
    medical_record_system.control_module.insertHospital(connection, hospitalNameList[random.randint(0, len(hospitalNameList) -1)]\
               + hospitalClassList[random.randint(0, len(hospitalClassList) -1 )], addressList[random.randint(0, len(addressList)-1)])

def randomNewMedicalRecord():
    global medical_recordCount
    medical_recordCount += 1
    medical_record_system.control_module.insertMedicalRecord(connection,\
        random.randint(1, customerCount), random.randint(1, hospitalCount), \
        diseaseList[random.randint(0, len(diseaseList)-1)],\
        prescriptionList[random.randint(0, len(prescriptionList)-1)],
        int(time.time()))

def randomUpdateCustomer():
    medical_record_system.control_module.updateCustomer(connection, random.randint(1, customerCount),\
        customerNameList[random.randint(0, len(customerNameList)-1)], \
        addressList[0, len(addressList)-1],\
        phoneNumberList[0, len(phoneNumberList)-1])

def randomUpdateHospital():
    medical_record_system.control_module.updateHospital(connection,\
        random.randint(1, hospitalCount),\
        hospitalNameList[random.randint(0, len(hospitalNameList) -1)]\
        + hospitalClassList[random.randint(0, len(hospitalClassList) -1 )],\
        addressList[random.randint(0, len(addressList)-1)])

def randomUpdateMedical():
    medical_record_system.control_module.updateMedicalRecord(connection,\
        random.randint(1,medical_recordCount),\
        random.randint(1,customerCount),\
        random.randint(1,hospitalCount),\
        diseaseList[random.randint(0, len(diseaseList)-1)],
        prescriptionList[random.randint(0, len(prescriptionList)-1)],
        int(time.time()))

def display():
    c = connection.execute("SELECT * FROM customer").fetch_tkinter("customer")
    ch = connection.execute("SELECT * FROM customer_history").fetch_tkinter("customer_history")
    h = connection.execute("SELECT * FROM hospital").fetch_tkinter("hospital")
    hh = connection.execute("SELECT * FROM hospital_history").fetch_tkinter("hospital_history")
    m = connection.execute("SELECT * FROM medical_record").fetch_tkinter("medical record")
    mh = connection.execute("SELECT * FROM medical_record_history").fetch_tkinter("medical record_history")
    b = connection.execute("SELECT * FROM block").fetch_tkinter("block")
    b.mainloop()
    mh.mainloop()
    m.mainloop()
    hh.mainloop()
    h.mainloop()
    ch.mainloop()
    c.mainloop()

#display()
randomNewCustomer()
randomNewHospital()
randomNewCustomer()
randomNewHospital()
randomNewCustomer()
randomUpdateHospital()
randomNewMedicalRecord()
randomNewMedicalRecord()
randomUpdateMedical()
display()