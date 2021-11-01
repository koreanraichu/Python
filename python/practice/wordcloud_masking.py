from wordcloud import WordCloud
from wordcloud import STOPWORDS
import matplotlib.pyplot as plot
from PIL import Image
import numpy as np
import sys

image=np.array(Image.open("/home/koreanraichu/Spade.jpeg"))
texts = 'The Ace of Spades (also known as the Spadille and Death Card) is traditionally the highest and most valued ' \
        'card in the deck of playing cards in English-speaking countries. The actual value of the card varies from game to game.'
wordcloud = WordCloud(font_path = '/usr/share/fonts/210 해오름R.ttf',
                      background_color="#000000",colormap="PuBu",width = 480, height=480,
                      mask=image)
wordcloud = wordcloud.generate_from_text(texts)
#np.set_printoptions(threshold=sys.maxsize)
plot.axis('off')
plot.imshow(wordcloud)
plot.show()
#Reference: https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=jymoon1115&logNo=221396769733