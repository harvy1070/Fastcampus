import re

contact = '''김미키 21 010-3344-5566 Mike@google.com 
             김소은 20 010-5032-1111 Soeun@naver.com
             유한슬 34 010-2789-1476 Lyu@school.ac.com
             박민철 40 010 4040 1313 Zoe@school.ac.com
             이민아 23 010-7777-2222 Kate@google.com'''

regex = r'0\d{1,2}[-]?\d{3,4}[ -]?\d{3,4}'
phone = re.findall(regex, contact)
# print("\n".join(phone))

pat = re.compile(r'0\d{1,2}[-]?\d{3,4}[ -]?\d{3,4}')
print(pat.sub("***-****-****", contact))