import tokenize
import io

inp = """import nltk
 from nltk.stem import PorterStemmer
 porter_stemmer=PorterStemmer()
 words=["connect","connected","connection","connections","connects"]
 stemmed_words=[porter_stemmer.stem(word) for word in words]
 stemmed_words"""

for token in tokenize.generate_tokens(io.StringIO(inp).readline):
 print(token)