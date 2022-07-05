from Bio import Entrez
from wordcloud import WordCloud
from wordcloud import STOPWORDS
import matplotlib.pyplot as plot
from PIL import Image
import numpy as np
from argparse import FileType
import tkinter
from tkinter import filedialog
import re
import platform
# 여기까지 모듈
Entrez.email = "blackholekun@gmail.com"
# 이메일 걍 자기꺼 쓰시면 됩니다
terms = input("검색어와 조건을 입력해주세요. 예를 들어서 박테리아가 제목인 논문을 찾으실거면 Bacteria[TITLE] 이런 식으로요: \n")
howmuch = input("논문은 몇 개정도 찾으실 생각이신가요?")
# Windows의 경우 시작하기 전에 코드단에서 폰트랑 경로부터 바꿔야 합니다. 

def replace_function (a):
    a = a.replace('[','-')
    a = a.replace(']','-')
    escape_terms = re.findall('-.{0,5}-',a)
    for i in escape_terms:
        a = a.replace(i,"")
    if '/' in a:
        a = a.replace('/','-')
    return a
# term 변환하는 거 함수로 뺐습니다. 근데 블록 실행하기 더 귀찮아진 건 기분탓인가... ㅡㅡ 

OS = platform.platform()
if 'Linux' in OS: 
    default_dir = '/home'
    root = tkinter.Tk()
    root.withdraw()
    font_dir = '/usr/share/fonts'
    font_path = filedialog.askopenfilename(parent=root, initialdir=font_dir, title='Choose your fonts for Wordcloud',
                                           filetypes=(("*.ttf", "*ttf"), ("*.otf", "*otf")))
elif 'Windows' in OS:
    default_dir = 'C:\\'
    root = tkinter.Tk()
    root.withdraw()
    font_path = filedialog.askopenfilename(parent=root, initialdir=default_dir, title='Choose your fonts for Wordcloud',
                                           filetypes=(("*.ttf", "*ttf"), ("*.otf", "*otf")))

handle = Entrez.esearch(db="pubmed", term=terms,retmax=howmuch)
record = Entrez.read(handle)
IdList=list(record['IdList'])
print("{}개의 데이터를 찾았습니다. 잠시만 기다려주세요. ".format(len(IdList)))
title=[]
for i in IdList: 
    handle = Entrez.esummary(db="pubmed", id=i, retmode="xml")
    records = Entrez.parse(handle)  
    for record in records:
        title.append(record['Title'])    
title=''.join(title)
print("오래 기다리셨습니다! 다 됐어요! ")
# Notes: 무지하게 오래 걸린다. 실화다. (retmax와 소요시간이 미칠듯이 비례함)

root = tkinter.Tk()
root.withdraw()
dir_path = filedialog.askopenfilename(parent=root,initialdir=default_dir,title='Please select a directory',filetypes = (("*.png","*png"),("*.jpg","*jpg"),("*.gif","*gif")))
image = np.array(Image.open(dir_path))
wordcloud = WordCloud(font_path = font_path,
                      background_color="#ffffff",colormap="Dark2",width = 960, height=960,
                      mask=image)
# 이것도 개인적으로 복붙하려고 만든거라;; 

root = tkinter.Tk()
root.withdraw()
save_path = filedialog.askdirectory()
terms = replace_function(terms)
save_dir = "{}/{}.png".format(save_path,terms)
# 얘는 입력하는 단어에 따라 알아서 만들어줍니다. 
wordcloud = wordcloud.generate_from_text(title)
plot.figure(figsize=(15,15),frameon=False)
plot.axis('off')
plot.imshow(wordcloud)
plot.savefig(save_dir,bbox_inches='tight',pad_inches=0)
plot.show()
print("wordcloud saved where {}".format(save_dir))