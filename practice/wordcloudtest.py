from wordcloud import WordCloud
from wordcloud import STOPWORDS
import matplotlib.pyplot as plot
import numpy as np

texts = 'The Ace of Spades (also known as the Spadille and Death Card) is traditionally the highest and most valued ' \
        'card in the deck of playing cards in English-speaking countries. The actual value of the card varies from game to game.'
wordcloud = WordCloud(font_path = '/usr/share/fonts/210 해오름R.ttf',
                      background_color="#ffffff",colormap="PuBu",width = 480, height=480)
wordcloud = wordcloud.generate_from_text(texts)

plot.axis('off')
plot.imshow(wordcloud)
plot.show()

# 참고 사이트
# https://lovit.github.io/nlp/2018/04/17/word_cloud/
# https://wannabe00.tistory.com/entry/Word-cloud-%EC%9B%90%ED%95%98%EB%8A%94-%EC%83%89%EC%9C%BC%EB%A1%9C-%EA%BE%B8%EB%AF%B8%EA%B8%B0-word-cloud-customize-color