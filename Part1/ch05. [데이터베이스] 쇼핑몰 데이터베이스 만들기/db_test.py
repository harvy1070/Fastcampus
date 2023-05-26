import sqlite3
import pandas as pd

conn = sqlite3.connect('test4.db')
c = conn.cursor()
# IF NOT EXISTS 구문을 사용하여 중복적으로 테이블 생성하는 것 방지
query = '''CREATE TABLE IF NOT EXISTS test4 (ID INTㅌERGER PRIMARY KEY, PRODUCT_NAME TEXT, PRICE INTERGER)'''
c.execute(query)
c.execute('''SELECT * FROM sqlite_master WHERE type = "table"''')
# # 순서를 정확히 알 경우 / 한줄씩 추가
c.execute("INSERT or IGNORE INTO test4 VALUES(1, '모자', '150000')")
c.execute("INSERT or IGNORE INTO test4 VALUES(2, '코트', '200000')")
# # 순서를 정확히 모를 경우 / 한줄씩 추가
c.execute("INSERT or IGNORE INTO test4(PRODUCT_NAME, PRICE, ID) VALUES(?, ?, ?)", ('티셔츠', 20000, 3))
c.execute("INSERT or IGNORE INTO test4(ID, PRICE, PRODUCT_NAME) VALUES(?, ?, ?)", ('4', 50000, '블라우스'))
# conn.commit()
# 데이터 삭제
# c.execute("DELETE FROM test4")
# 여러줄 한번에 추가하기
product_list = [[1, '모자', 15000],
                [2, '코트', 200000],
                [3, '티셔츠', 20000],
                [4, '블라우스', 55000],
                [5, '가디건', 45000],
                [6, '청바지', 50000],
                [7, '구두', 150000],
                [8, '가방', 170000]]
c.executemany("INSERT or REPLACE INTO test4(ID, PRODUCT_NAME, PRICE) VALUES(?,?,?)", product_list)
conn.commit()

# DATE 수정 >> UPDATE
# tuple 형태 수정 ()
c.execute("UPDATE test4 SET PRODUCT_NAME = ? WHERE ID = ?", ('슬렉스', 6))
# dictionary 형태의 수정 {}
c.execute("UPDATE test4 SET PRICE = :price WHERE ID = :id", {"price":55000, "id":6})
# %s 형태의 수정 // .format으로 대입하는 것과 같은 형태
c.execute("UPDATE test4 SET PRODUCT_NAME = '%s' WHERE ID = '%s'" % ('트렌치코트', 2))

c.execute('''SELECT * FROM test4''')

# DELETE >> 삭제
# TUPLE
c.execute("DELETE FROM test4 WEHRE ID = ?", (8, ))
# DICTIONARY
c.execute("DELETE FROM test4 WHERE PRODUCT_NAME = :product_name", {'product_name':'슬랙스'})
# 전체삭제
c.execute("DELETE FROM test4")

