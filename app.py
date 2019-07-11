from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from flask import Flask, render_template, request, jsonify
from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.summarizers.luhn import LuhnSummarizer as LuhnSummarizer
from sumy.summarizers.lex_rank import LexRankSummarizer as LexSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer as TextSummarizer
from sumy.summarizers.sum_basic import SumBasicSummarizer as SumSummarizer
from sumy.summarizers.kl import KLSummarizer as KLSummarizer

app = Flask(__name__)




@app.route('/')
def index():
    return render_template('summarizer.html')

@app.route('/dependent')
def dependent():
	return render_template('dependent.html')


@app.route('/subscriber')
def subscriber():
	return render_template('subscriber.html')


LANGUAGE = "english"
SENTENCES_COUNT = 10


@app.route('/dependent', methods = ['POST'])
def mySumD():
	if request.form['action'] == 'LSA':
		para = ""
		url = request.form['url_link']
		parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
		stemmer = Stemmer(LANGUAGE)
		summarizer = Summarizer(stemmer)
		summarizer.stop_words = get_stop_words(LANGUAGE)

		for sentence in summarizer(parser.document, SENTENCES_COUNT):
			data = str(sentence)
			para += data 
		return render_template('dependent.html', para = para)
	
	elif request.form['action'] == 'Luhn':
		para = ""
		url = request.form['url_link']
		parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
		stemmer = Stemmer(LANGUAGE)
		summarizer = LuhnSummarizer(stemmer)
		summarizer.stop_words = get_stop_words(LANGUAGE)

		for sentence in summarizer(parser.document, SENTENCES_COUNT):
			data = str(sentence)
			para += data 
		return render_template('dependent.html', para = para)
	
	elif request.form['action'] == 'LexRank':
		para = ""
		url = request.form['url_link']
		parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
		stemmer = Stemmer(LANGUAGE)
		summarizer = LexSummarizer(stemmer)
		summarizer.stop_words = get_stop_words(LANGUAGE)

		for sentence in summarizer(parser.document, SENTENCES_COUNT):
			data = str(sentence)
			para += data 
		return render_template('dependent.html', para = para)
	
	elif request.form['action'] == 'TextRank':
		para = ""
		url = request.form['url_link']
		parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))

		stemmer = Stemmer(LANGUAGE)
		summarizer = TextSummarizer(stemmer)
		summarizer.stop_words = get_stop_words(LANGUAGE)

		for sentence in summarizer(parser.document, SENTENCES_COUNT):
			data = str(sentence)
			para += data 
		return render_template('dependent.html', para = para)
	
	elif request.form['action'] == 'SumBasic':
		para = ""
		url = request.form['url_link']
		parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))

		stemmer = Stemmer(LANGUAGE)
		summarizer = SumSummarizer(stemmer)
		summarizer.stop_words = get_stop_words(LANGUAGE)

		for sentence in summarizer(parser.document, SENTENCES_COUNT):
			data = str(sentence)
			para += data 
		return render_template('dependent.html', para = para)
	
	else:
		para = ""
		request.form['action'] == 'KL-Sum'
		url = request.form['url_link']
		parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))

		stemmer = Stemmer(LANGUAGE)
		summarizer = KLSummarizer(stemmer)
		summarizer.stop_words = get_stop_words(LANGUAGE)

		for sentence in summarizer(parser.document, SENTENCES_COUNT):
			data = str(sentence)
			para += data 
		return render_template('dependent.html', para = para)

@app.route('/subscriber', methods = ['POST'])
def mySumS():
	if request.form['action'] == 'LSA':
		para = ""
		url = request.form['url_link']
		parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))

		stemmer = Stemmer(LANGUAGE)
		summarizer = Summarizer(stemmer)
		summarizer.stop_words = get_stop_words(LANGUAGE)

		for sentence in summarizer(parser.document, SENTENCES_COUNT):
			data = str(sentence)
			para += data 
		return render_template('subscriber.html', para = para)
	
	elif request.form['action'] == 'Luhn':
		para = ""
		url = request.form['url_link']
		parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))

		stemmer = Stemmer(LANGUAGE)
		summarizer = LuhnSummarizer(stemmer)
		summarizer.stop_words = get_stop_words(LANGUAGE)

		for sentence in summarizer(parser.document, SENTENCES_COUNT):
			data = str(sentence)
			para += data 
		return render_template('subscriber.html', para = para)
	elif request.form['action'] == 'LexRank':
		para = ""
		url = request.form['url_link']
		parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))

		stemmer = Stemmer(LANGUAGE)
		summarizer = LexSummarizer(stemmer)
		summarizer.stop_words = get_stop_words(LANGUAGE)

		for sentence in summarizer(parser.document, SENTENCES_COUNT):
			data = str(sentence)
			para += data 
		return render_template('subscriber.html', para = para)
	elif request.form['action'] == 'TextRank':
		para = ""
		url = request.form['url_link']
		parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))

		stemmer = Stemmer(LANGUAGE)
		summarizer = TextSummarizer(stemmer)
		summarizer.stop_words = get_stop_words(LANGUAGE)

		for sentence in summarizer(parser.document, SENTENCES_COUNT):
			data = str(sentence)
			para += data 
		return render_template('subscriber.html', para = para)
	elif request.form['action'] == 'SumBasic':
		para = ""
		url = request.form['url_link']
		parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
	
		stemmer = Stemmer(LANGUAGE)
		summarizer = SumSummarizer(stemmer)
		summarizer.stop_words = get_stop_words(LANGUAGE)

		for sentence in summarizer(parser.document, SENTENCES_COUNT):
			data = str(sentence)
			para += data 
		return render_template('subscriber.html', para = para)
	else:
		para = ""
		request.form['action'] == 'KL-Sum'
		url = request.form['url_link']
		parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))

		stemmer = Stemmer(LANGUAGE)
		summarizer = KLSummarizer(stemmer)
		summarizer.stop_words = get_stop_words(LANGUAGE)

		for sentence in summarizer(parser.document, SENTENCES_COUNT):
			data = str(sentence)
			para += data 
		return render_template('subscriber.html', para = para)

if __name__ == '__main__':
    app.run()
