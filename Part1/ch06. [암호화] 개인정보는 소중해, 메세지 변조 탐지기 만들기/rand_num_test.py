# 안전한 난수 생성
# secrets을 활용하여 난수 생성(random으로 난수를 생성하기에는 보안상으로 위험)
# 3.6 이후 버전부터 추가된 난수 생성 모듈

import secrets
import string

# 16진수 난수 16자리 생성(16진수이기 때문에 8x2가 난수의 길이)
rand8 = secrets.token_hex(8)
# print(rand8)

# 16진수 난수 32자리 생성(16진수이기 때문에 16x2가 난수의 길이)
rand16 = secrets.token_hex(16)
# print(rand16)

# otp 비밀번호 생성

otp = ''
digit = string.digits # 0 - 9까지의 수를 모두 string 형태로 저장
for i in range(6):
    # otp에 range 0 - 5 동안 돌며 secrets 모듈을 이용하여 digit에 저장된 수를 무작위로 축적
    # 6자리가 다 차면 for문 탈출
    otp += str(''.join(secrets.choice(digit)))
print(otp)

# 비밀번호 일치 여부 확인
# timing attack 방지하는 기능
print(secrets.compare_digest('password123', 'password123'))

# 보안 url 생성
url = 'https://www.naver.com/reset=' + secrets.token_urlsafe(7)