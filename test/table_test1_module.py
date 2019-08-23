import os, sys
sys.path.append(os.path.dirname(__file__) + "{0}..{0}..".format(os.path.sep))

import medical_record_system
import blockSQL

connection = blockSQL.Connection(":memory:")
medical_record_system.define_table_module.createTable(connection)

################################################################################
# 시나리오
# 
# 병원 2개가 생김
# 병원 하나가 이름을 바꿈
# 종합병원에 감기 환자 A가 옴
# 종합
################################################################################
connection.execute("""
INSERT INTO hospital (hospitalName ,hospitalAddress)
VALUES(
    "천안공주종합병원",
    "충남 천안시"
)
""")
connection.execute("""
INSERT INTO hospital (hospitalName, hospitalAddress)
VALUES(
    "의료원",
    "충남 천안시"
)
""")

connection.execute("""
UPDATE hospital
SET hospitalName = "대박의료원"
WHERE hospitalName = "의료원"
""")

print(connection.execute("""
SELECT * FROM hospital
""").fetchall())

print(connection.execute("""
SELECT * FROM hospital_history
""").fetchall())

print(connection.execute("""
SELECT * FROM block
""").fetchall())