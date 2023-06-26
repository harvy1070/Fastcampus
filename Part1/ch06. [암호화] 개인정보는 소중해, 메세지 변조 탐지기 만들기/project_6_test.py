import getpass
import datetime
import hashlib
import os
import hmac

# 입력된 하이픈을 타입에 맞게 분류하는 함수
def number_parser(input_num, option = 'phone'):
    output_num = ''
    if option == 'phone':
        for i in range(0, len(input_num)):
            if i == 2:
                output_num += input_num[2] + '-'
            elif i == 6:
                output_num += input_num[6] + '-'
            else:
                output_num += input_num[i]

    elif option == 'account':
        for i in range(0, len(input_num)):
            if i == 4:
                output_num += input_num[2] + '-'
            elif i == 9:
                output_num += input_num[9] + '-'
            else:
                output_num += input_num[i]

    elif option == 'id':
        for i in range(0, len(input_num)):
            if i == 5:
                output_num += input_num[5] + '-'
            else:
                output_num += input_num[i]

    elif option == 'transfer':
        output_num = input_num + '0000 원'

    # 위 결과 중 최종결과값 return
    return output_num

if __name__ == "__main__":
    client_name = input("이름 입력 >>> ")
    phone_number = input("전화번호 입력(- 제외 11자리) >>> ")
    # getpass를 활용해서 input대신 입력창 삽입(주민번호 암호화)
    id_number = getpass.getpass("주민번호 입력(- 제외 13자리) >>> ")
    account_number = input("계좌번호 입력(- 제외 15자리) >>> ")
    transfer_amount = input("거래 금액을 만원 단위로 입력 >>> ")

    # 계좌 파일 생성
    with open('계좌정보_원본.txt', 'w') as f:
        f.write(f'등록일시 : {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
        f.write(f'고객명 : {client_name}\n')
        f.write(f'전화번호 : {number_parser(phone_number, "phone")}\n')

        # 정규 표현식으로 표현하기 위해 re 함수를 import
        import re

        pat = re.compile("(\d{6})[-]\d{7}")
        # g<1>로 앞자리를 표현, 뒷자리는 별처리
        id_number = pat.sub("\g<1>-*******", number_parser(id_number, "id"))
        f.write(f'주민번호 : {id_number}\n')

        f.write(f'계좌번호 : {number_parser(account_number, "account")}\n')
        f.write(f'거래금액 : {number_parser(transfer_amount, "transfer")}\n')

    # 비밀키(비밀번호) 호출
    SECRET_KEY = getpass.getpass("비밀번호 입력 >>> ")
    with open('passwd.txt', 'w') as f:
        m = hashlib.sha256()
        m.update(SECRET_KEY.encode('utf-8'))
        f.write(m.hexdigest())

    # 계좌 정보 원본 호출
    with open('계좌정보_원본.txt', 'r') as f:
        message_origin = f.read()

    # 비밀키 활용한 계좌 정보 암호화
    with open('계좌정보_암호화.txt', 'w') as f:
        m = hmac.new(SECRET_KEY.encode('utf-8'), message_origin.encode('utf-8'), hashlib.sha256)

    # 비밀번호 확인
    with open('passwd.txt', 'r') as f:
        m = hashlib.sha256()

    # 암호화된 계좌 정보
    with open('계좌정보_암호화.txt', 'r') as f:
        message_encrypted = f.read()

    # 계좌 원본 메세지와 비교
    with open('계좌정보_원본.txt') as f:
        message_origin = f.read()
        m = hmac.new(SECRET_KEY.encode('utf-8'), message_origin.encode('utf-8'), hashlib.sha256)

        if m.hexdigest() == message_encrypted:
            print("계좌 정보가 변조되지 않음, 안전")
        else:
            print("계좌정보가 변조되었음, 위험")