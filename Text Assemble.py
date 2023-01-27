import re
import nltk
nltk.download('punkt')

from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

data1 ="Hello I am dhotar Chor"
x = re.search('dhotar',data1)
print(x)

data2 ="dhotar chor is present in the college premices "
x2=re.findall("^\w+",data2)

x3 =re.split(r'\s','data splitter need to work')
print(x3)

data3 ="The list of projected top 10 skills from 2015 - 2017 is as follows"

tokenlist =sent_tokenize(data3)
print(tokenlist)

print (word_tokenize(data3))