from wordcloud import WordCloud
from wordcloud import STOPWORDS
import matplotlib.pyplot as plot
from PIL import Image
import numpy as np
from argparse import FileType
import tkinter
from tkinter import filedialog
import platform
# Summon module

text = []
while True: 
    input_text = input("wordcloud로 만들 텍스트를 입력해주세요. ")
    text.append(input_text) 
    if input_text == "":
        break
text = ''.join(text)

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

root = tkinter.Tk()
root.withdraw()
dir_path = filedialog.askopenfilename(parent=root,initialdir=default_dir,title='Add your masking Image',filetypes = (("*.png","*png"),("*.jpg","*jpg"),("*.gif","*gif")))
image = np.array(Image.open(dir_path)) 
# 마스킹할 이미지(흰 바탕에 검정색을 권장함)
wordcloud = WordCloud(font_path = font_path,stopwords=STOPWORDS,
                      background_color="#ffffff",colormap="magma",width = 960, height=960,
                      mask=image)
# Font path: 글꼴 설정하실 경우 여기에 쓰세요
# background color: wordcloud 배경 설정할 때 여기서 하세요 
# colormap: 워드클라우드 글자색을 여기서 바꿔주세요(matplotlib colormap 치면 많이 나옵니다)

root = tkinter.Tk()
root.withdraw()
save_path = filedialog.asksaveasfilename(parent=root,initialdir=default_dir,title='Save locations for wordcloud',filetypes = (("*.png","*png"),("*.jpg","*jpg"),("*.gif","*gif")))
# 워드클라우드 저장하는 경로(저장은 png파일만 됩니다)
wordcloud = wordcloud.generate_from_text(text)
plot.figure(figsize=(15,15))
plot.axis('off')
plot.imshow(wordcloud)
plot.savefig(save_path,bbox_inches='tight',pad_inches=0)
plot.show()
print("wordcloud saved where {}.png".format(save_path))