from Bio import Entrez
# 논문 긁어올 때 필요한거
from wordcloud import WordCloud
from wordcloud import STOPWORDS
import matplotlib.pyplot as plot
# Wordcloud 그릴 때 필요한거
Entrez.email = "blackholekun@gmail.com"
handle = Entrez.esearch(db="pubmed", term="Arabidopsis[title]", retmax="15")
record = Entrez.read(handle)
IdList=record['IdList']
# 일차적으로 Pubmed에서 논문을 찾을 수단인 PMID를 입수한다.
# 날짜검색이 안돼서 키워드에 '애기장대'가 있는 논문 10개를 찾음.
for i in range(len(IdList)):
    handle = Entrez.esummary(db="pubmed", id=IdList[i], retmode="xml")
    records = Entrez.parse(handle)
    title=[]
    for record in records:
        title.append(record['Title'])
# 타이틀 뽑았다.
# wordcloud에서 뺄 단어들(접속사 이런거)
font_path = '/usr/share/fonts/truetype/nanum/BinggraeMelona.ttf'
wordcloud = WordCloud(stopwords=STOPWORDS,   font_path = font_path, width = 800,
    height = 800,background_color="#ffffff")
wordcloud = wordcloud.generate_from_text(record['Title'])
plot.axis('off')
plot.imshow(wordcloud)
plot.show()
# wordcloud generate