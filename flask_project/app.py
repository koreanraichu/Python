from flask import Flask, render_template
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
from konlpy.tag import Okt
import nltk
okt=Okt()

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
