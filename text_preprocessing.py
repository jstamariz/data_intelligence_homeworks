import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

nltk.download('stopwords')

stemmer = SnowballStemmer("spanish")

unprocessed_text = open('unprocessed_text.txt').read()
txt_wo_special_characters = re.sub('\\W+', ' ', unprocessed_text)
tokenized_text = txt_wo_special_characters.split(" ")
tokenized_text_no_stopwords = [tt for tt in tokenized_text if not tt.lower() in stopwords.words("spanish")]

finished_product = [stemmer.stem(token) for token in tokenized_text_no_stopwords]

print(unprocessed_text)
print(finished_product)