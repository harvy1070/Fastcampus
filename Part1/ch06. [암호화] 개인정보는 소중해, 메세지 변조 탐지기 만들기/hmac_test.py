# 메시지 변조 탐지기
# hmac은 비밀 키, 해싱 기술(hashlib 등)을 활용하여 송수신자 간 메시지 변조를 확인할 수 있는 모듈
# 비밀 키를 사용하여 해싱된 데이터 내용이 같은 지 대조하는 원리
# 해커 등 3자가 메시지 변조를 했을 시, 비밀 키로 해싱한 결과가 달라짐

# 비밀 키 설정
secret_key = 'FASTCAMPUS'

# 암호화 파일 생성
import hmac
import hashlib

# [송신] 메시지 입력
important_massage = 'very important message'

# 원본 파일 오픈
with open('message.txt', 'w') as f:
    f.write(important_massage)

# 비밀 키 암호화 파일 오픈
with open('message_encrypted.txt', 'w') as f:
    m = hmac.new(secret_key.encode('utf-8'), important_massage.encode('utf-8'), hashlib.sha256)
    f.write(m.hexdigest()) # 암호화된 메세지가 'm' 파일에 작성이 됨

# [수신] 복호화 및 변조 확인
with open('message_encrypted.txt') as f:
    message_encrypted = f.read()

with open('message.txt') as f:
    message = f.read()
    m = hmac.new(secret_key.encode('utf-8'), message.encode('utf-8'), hashlib.sha256)

    if m.hexdigest() == message_encrypted:
        print("메시지가 변조되지 않았음, 안전")
    else:
        print("변조된 메시지, 위험")