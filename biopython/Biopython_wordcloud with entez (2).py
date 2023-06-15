from Bio import Entrez
# 논문 긁어올 때 필요한거
from wordcloud import WordCloud
from wordcloud import STOPWORDS
import matplotlib.pyplot as plot
# Wordcloud 그릴 때 필요한거
import numpy as np
from PIL import Image
# 이미지 마스킹할 때 필요한거
image=np.array(Image.open("/home/koreanraichu/1599661.jpg"))
font_path = '/usr/share/fonts/dovemayo.otf'
# 마스킹할 이미지
# 근데 이거 어떤건 되고 어떤건 안되더라...
Entrez.email = "blackholekun@gmail.com"
handle = Entrez.esearch(db="pubmed", term="Arabidopsis[title] AND 2021[Years]", retmax="30")
# 날짜 이거였냐
record = Entrez.read(handle)
IdList=record['IdList']
# 일차적으로 Pubmed에서 논문을 찾을 수단인 PMID를 입수한다.
# 숫자를 20개로 늘려서 시간이 좀 걸린다.
title=[]
for i in range(len(IdList)):
    handle = Entrez.esummary(db="pubmed", id=IdList[i], retmode="xml")
    records = Entrez.parse(handle)
    for record in records:
        title.append(record['Title'])
title=''.join(title)
# 타이틀 뽑았다.
# 아 이거 근데 묶어줘야되더라...
wordcloud = WordCloud(stopwords=STOPWORDS,font_path = font_path, width = 800,height = 800,
                      background_color="#ffffff",colormap='Spectral_r',mask=image)
wordcloud = wordcloud.generate_from_text(title)
# 생(별)성
plot.axis('off')
plot.imshow(wordcloud)
plot.show()
# wordcloud generate
