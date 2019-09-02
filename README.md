medical-record-system
======
# index
1. [소개](#1소개)
2. [설치](#2설치)

    2.1. [git으로 하기](#2.1.git으로-하기)

    2.2. [다운로드 방식으로 하기](#2.2.다운로드-방식으로-하기)
3. [예제](#3예제)
4. [스키마](#4스키마)
5. [각 모듈 설명](#5각-모듈-설명)

# [1.](#index)소개
 [블록체인 구조로 된 데이터베이스](https://github.com/hslee1539/blockSQL)를 활용하여 병원의 환자 관리를 간단하게 구현한 프로젝트입니다.

# [2.](#index)설치
두가지 방법을 소개합니다.

## [2.1.](#2.설치)git으로 하기
1. cmd를 실행합니다.
2. cd 명령어로 설치하고자 하는 폴더로 path를 이동합니다.
3. cmd에서 `git clone https://github.com/hslee1539/blockSQL.git`를 입력합니다.
4. cmd에서 `git clone https://github.com/hslee1539/medical-recode-system.git`을 입력합니다.

> *주의!! blockSQL [20190902 이전 버전](https://github.com/hslee1539/blockSQL/commit/0c2dd1f0fd008bffa1e5d8317e729d1b86f359f4)은 pycrypto 모듈이 필요합니다. 이 버전을 포함한 이후 버전에는 rc4 암호 알고리즘이 내장됩니다.*

## [2.2.](#2.설치)다운로드 방식으로 하기
1. 두개의 압축 파일을 받습니다

[blockSQL](https://github.com/hslee1539/blockSQL/archive/master.zip)

[medical-recode-system](https://github.com/hslee1539/medical_record_system/archive/master.zip)

또는,

[https://github.com/hslee1539/blockSQL](https://github.com/hslee1539/blockSQL)

[https://github.com/hslee1539/medical_record_system](https://github.com/hslee1539/medical_record_system)

에서 각각 clone or download 버튼을 클릭하여 압축 파일을 받습니다.

2. 작업 폴더에 두개의 압축 파일을 해제합니다.

> *주의!! 꼭 압축 해제한 폴더명이 각각 **blockSQL**과 **medical_recode_system**가 되야 합니다.*
# [3.](#idex)예제

1. ~~[table_test2_module.py](./test/table_test2_module.py)를 실행하세요.~~
2. ~~그 모듈에 정의된 함수를 이용하여 병력관리 시스템을 시물레이션 해보세요.~~

~~newCustomer() : 새로운 환자를 랜덤하게 만듭니다.~~

~~newHospital() : 새로운 병원을 랜덤하게 만듭니다.~~

~~customer_go_hospital(customerID) : 해당 환자로 랜덤한 이벤트로 병원을 가게 합니다.~~

~~display() : 모든 테이블을 출력합니다.~~

예제를 업데이트 예정입니다.

# [4.](#index)스키마
customer

    customerID, customerName, customerAddress, customerPhoneNumber

medical_record

    medical_recordID, customerID, hospitalID, disease, prescription, date

hospital

    hospitalID, hospitalName, hospitalAddress

# [5.](#index)각 모듈 설명
## [5.1.](#5.각-모듈-설명)define_table_module.py
테이블을 정의하는 모듈입니다. 

[blockSQL](https://github.com/hslee1539/blockSQL).[Connection](https://github.com/hslee1539/blockSQL/blob/master/connection_module.py).execute() 메소드로 sql 명령어로 테이블을 만듭니다.
