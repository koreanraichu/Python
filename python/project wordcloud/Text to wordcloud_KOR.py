from wordcloud import WordCloud
from wordcloud import STOPWORDS
import matplotlib.pyplot as plot
from PIL import Image
import numpy as np  
# Summon module
# 아, 참고로 일본어는 안됩니다. 밑에 부르는 모듈이 한글 처리 전문이라... 
from konlpy.tag import Okt
import nltk  
okt=Okt()
# 한글은 이렇게 처리하면 된다. 
from argparse import FileType
import tkinter
from tkinter import filedialog
# 파일 저장 관련 모듈
import platform

def munjang_to_noun (a):
    a = ' '.join(a)
    a = okt.nouns(a)
    a = ' '.join(a)
    return a

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

text = []
while True: 
    input_text = input("wordcloud로 만들 텍스트를 입력해주세요. ")
    text.append(input_text) 
    if input_text == "":
        break
text = munjang_to_noun(text)

root = tkinter.Tk()
root.withdraw()
dir_path = filedialog.askopenfilename(parent=root,initialdir=default_dir,title='Please select a directory',filetypes = (("*.png","*png"),("*.jpg","*jpg"),("*.gif","*gif")))
image = np.array(Image.open(dir_path)) 
# 마스킹할 이미지(흰 바탕에 검정색을 권장함)
image = np.array(Image.open(dir_path))
wordcloud = WordCloud(font_path = font_path,stopwords=STOPWORDS,
                      background_color="#ffffff",colormap="inferno",width = 960, height=960,
                      mask=image)

root = tkinter.Tk()
root.withdraw()
save_path = filedialog.asksaveasfilename(parent=root,initialdir=default_dir,title='Please select a directory',filetypes = (("*.png","*png"),("*.jpg","*jpg"),("*.gif","*gif")))
# 워드클라우드 저장하는 경로(저장은 png파일만 됩니다)
wordcloud = wordcloud.generate_from_text(str(text))
plot.figure(figsize=(15,15))
plot.axis('off')
plot.imshow(wordcloud)
plot.savefig(save_path,bbox_inches='tight',pad_inches=0)
plot.show()
print("wordcloud saved where {}.png".format(save_path))