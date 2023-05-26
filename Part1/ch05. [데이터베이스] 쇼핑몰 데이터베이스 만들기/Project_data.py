import sqlite3
import pandas as pd


# 쇼핑몰 DB연결 및 Cursor 생성
conn = sqlite3.connect("shopping_mall.db")
c = conn.cursor()

# 기존에 만든 상품 리스트 // 한글이 섞여 있기에 encoding 해줘야함
product_list = pd.read_csv('product_list.csv', encoding='euc-kr')

# 곧바로 리스트를 테이블에 추가
# if_exits = 'append' 이미 테이블에 해당 항목이 있으면 그 뒤에 이어서 append 하란 의미
# index = False // ID가 이미 있어서 INDEX를 굳이 설정하지 않아도 되서 FALSE 처리
product_list.to_sql('productList', conn, if_exists='append', index = False)

