import random
import requests
from bs4 import BeautifulSoup
import re

TAG_RE = re.compile(r'<[^>]+>')
"""
1º passo: criar a frase

2ºpassso: alterar a frase de forma random e reter a palavra / palavras para depois serem inseridas

3ºpasso: retornar tudo para o utilizador
"""

class main:
	def __init__(self):
		self.sopeira()

	def remove_tags(self,text):
		return TAG_RE.sub('', text)

	def sopeira(self):
		url = "https://www.pensador.com/frases/"
		website = requests.get(url)
		classHtml = "frase fr"
		sopinha = BeautifulSoup(website.content, "html.parser") 
		resultados = sopinha.find_all(id = "phrasesList")
		for resultado in resultados:
			frase = resultado.find_all(class_ = "frase fr")
		fraseParaUsar = random.choice(frase)
		fraseParaUsar = self.remove_tags(str(fraseParaUsar))
		self.word = fraseParaUsar
		self.editorFrases()

	def editorFrases(self):
		numPalavras = self.numOfWords()
		print(numPalavras)
		indexPalavraARemover= random.randrange(0, numPalavras)
		word = self.wordSelector(indexPalavraARemover)
		while(word == "  "):
			word = self.wordSelector(indexPalavraARemover-1)
		self.printer(word)

	def printer(self, word):
		newWord = self.word.replace(word, self.blanks(word)[:-1]+ " ")
		print(newWord)
		self.inputer(word)

	def inputer(self, word):
		lives = 3
		while(lives != 0):
			userInput = input("Qual a palavra em falta? ")
			if (userInput == word[:-1]):
				print("Acertaste")
				break
			else:
				lives-=1

	def numOfWords(self):
		palavras = 0
		words = self.word
		for i in words:
			if (i == " "):
				palavras +=1
		return palavras

	def wordSelector(self,index):
		word = ""
		pos = 0
		for i in self.word:
			if (pos>index):
				
				return word

			if (pos == index):
				word +=i
			if (i == " "):
				pos +=1

	def blanks(self,word):
		blank = ""
		for i in word:
			blank+="_"
		return blank


main()