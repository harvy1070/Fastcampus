import getpass

passwd = 'fastcampus123!'

# 사용자 입력 비밀번호
user_input = getpass.getpass("비밀번호를 입력하세요 >>> ")

while user_input != passwd:
    # 비밀번호 불일치 메세지
    user_input = getpass.getpass("잘못된 비밀번호입니다! 다시 입력해주세요 >>> ")

print('잠금 해제')
print('''
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    ▒▒▒▒▒▒▒▒▓▒▒▒▓▒▒▒▒▒▒▒
    ▒▒▒▒▒▒▒▒▓▒▒▒▓▒▒▒▒▒▒▒
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    ▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒
    ▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒''')