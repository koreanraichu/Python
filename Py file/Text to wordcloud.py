from wordcloud import WordCloud
from wordcloud import STOPWORDS
import matplotlib.pyplot as plot
from PIL import Image
import numpy as np
# Summon module
text = []
input_text= input("wordcloud로 만들 텍스트를 입력해주세요. ")
text.append(input_text)
yorn = input("더 추가할 텍스트가 있나요?")
# 일단 입력을 받는다. (없으면 n, 있으면 n 말고 다른거)
while yorn != "n":
    yorn = input("더 추가할 텍스트가 있나요? ")
    if yorn == "n":
        text = ''.join(text)
    else:
        input_text= input("wordcloud로 만들 텍스트를 입력해주세요 ")
        text.append(input_text)
# 추가로 입력이 있을 경우 입력이 '없다'고 할 떄까지 입력을 받고 입력이 더 이상 들어오지 않으면 join한다. (입력 받을때마다 join하면 에러남)
image = np.array(Image.open("/home/koreanraichu/1599661.jpg"))
# 이미지를 부르고
font_path = '/usr/share/fonts/독립서체_백범김구_GS.ttf'
wordcloud = WordCloud(stopwords=STOPWORDS, font_path= font_path,background_color="#ffffff",colormap="PuBu_r",
                      width = 800,
                      height=800, mask=image)
wordcloud = wordcloud.generate_from_text(text)
# 그리고
plot.figure(figsize=(15,15))
plot.axis('off')
plot.imshow(wordcloud)
plot.show()
# 출력