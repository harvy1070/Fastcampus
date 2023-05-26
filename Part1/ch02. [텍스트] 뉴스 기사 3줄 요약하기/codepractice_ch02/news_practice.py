import base64
from PIL import Image

f = open("C:/Users/kwon/Fastcampus/Part1/ch02. [텍스트] 뉴스 기사 3줄 요약하기/news/image", 'rb')
image = f.readlines()
f.close()
# print(Image)
a = open("C:/Users/kwon/Fastcampus/Part1/ch02. [텍스트] 뉴스 기사 3줄 요약하기/news/article", 'rb')
article = a.readlines()
a.close()
# print(article)

#
file_base64 = image[0]
path = "C:/Users/kwon/Fastcampus/Part1/ch02. [텍스트] 뉴스 기사 3줄 요약하기/news/image.jpg"
with open(path, 'wb') as f:
    decoded_data = base64.decodebytes(file_base64)
    f.write(decoded_data)

img = Image.open(path)
# print(img)

file_base64_2 = article[0]
decoded_data = base64.decodebytes(file_base64_2)
article = decoded_data.decode('utf-8')
# print(article)

# 키워드 추출
from collections import Counter
import textwrap
import re

article_align = textwrap.fill(article, width=50)
# print(article_align)
# 단어 추출
words = re.findall(r'\w+', article_align)
# print(words)
# 빈도수 추출
counter = Counter(words)
# print(counter)
keywords = counter.most_common(5)[1:]
# print(keywords)

from IPython.display import Image
Image(filename=path, width=300)

keys = ['# ' + elem[0] for elem in keywords]
keys = ' '.join(keys)
print(keys)


# from gensim.summarizations.summary import summarization