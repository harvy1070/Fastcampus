import sqlite3


conn = sqlite3.connect("test4.db")
c = conn.cursor()

# product_list = [[1, '모자', 15000],
#                 [2, '코트', 200000],
#                 [3, '티셔츠', 20000],
#                 [4, '블라우스', 55000],
#                 [5, '가디건', 45000],
#                 [6, '청바지', 50000],
#                 [7, '구두', 150000],
#                 [8, '가방', 170000]]
#
# c.executemany("INSERT OR REPLACE INTO test4(ID, PRODUCT_NAME, PRICE) VALUES(?,?,?)", product_list)
# conn.commit()
#
# for line in conn.iterdump():
#     print(line)
#
# with conn:
#     with open('backup.sql', 'w') as f:
#         for line in conn.iterdump():
#             f.write(r'%s\n' % line)
#         print("Completed")
#
#
# # 테이블 삭제
# c.execute("DROP TABLE test4")
# conn.commit()

# 백업 SQL 파일 로딩
with open('backup.sql', 'r') as sql_file:
    sql_script = sql_file.read()

sql_script = sql_script.replace("\\", "/")

print(sql_script)
# 스크립트 실행
c.executescript(sql_script)
conn.commit()