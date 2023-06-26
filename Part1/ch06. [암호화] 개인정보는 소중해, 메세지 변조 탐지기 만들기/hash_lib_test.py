import hashlib
import getpass

passwd = 'fastcampus123!'

# passwd 해싱작업
h = hashlib.sha256()
h.update(passwd.encode('utf-8'))

# hashing passwd
h_passwd = h.digest()
# print(h_passwd)

# 해싱을 사용하여 getpass 활용하기
def passwd_hash(original_passwd):
    h = hashlib.sha256()
    h.update(original_passwd.encode('utf-8'))
    hashed_passwd = h.digest()
    return hashed_passwd

user_input = passwd_hash(getpass.getpass("password input >>> "))

while user_input != h_passwd:
    # password not in
    user_input = passwd_hash(getpass.getpass("not correct password! re try >>> "))
    print("your password ... : {}".format(user_input))

print('잠금 해제')
print('''
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    ▒▒▒▒▒▒▒▒▓▒▒▒▓▒▒▒▒▒▒▒
    ▒▒▒▒▒▒▒▒▓▒▒▒▓▒▒▒▒▒▒▒
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    ▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒
    ▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒''')