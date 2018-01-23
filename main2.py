# AmethystImpala
# 9/15/17
# Challenge 2
# TutorialsPoint.com
# StackOverFlow.com https://stackoverflow.com/questions/4211209/remove-all-the-elements-that-occur-in-one-list-from-another
# https://stackoverflow.com/questions/5466618/too-many-values-to-unpack-iterating-over-a-dict-key-string-value-list

from __future__ import division
import matplotlib.pyplot as mplot
import re

file = raw_input("Enter the file name: ")

# Reading and Manipulating d08.txt
data = open(file, "r")
data = data.read()
data = re.sub(r'\W+', ' ', data)
data = data.lower()
data = data.split(" ")
data.pop()

# Read in 105 Common Words
comWords = open("105_common.txt")
comWords = comWords.read()
comWords = comWords.lower()
comWords = comWords.split("\n")
comWords.pop()

# take out common words from data
data = [x for x in data if x not in comWords]

# Reading Lexixon and Manipulating it
lex = open("sent_lexicon.csv", "r")
lex = lex.read()
lex = lex.split("\n")
lex.pop()

for x in range(len(lex)):
	lex[x] = lex[x].split(",")


for list in lex:
	list[1] = float(list[1])

# Counts the unique words in the speech
data_dct = {}
for word in data:
	try:
		data_dct[word] = data_dct[word] + 1
	except:
		data_dct[word] = 1

# making categories and keeping count
negative = 0
weakNegative = 0
neutral = 0
weakPositive = 0
positive = 0

for key, value in data_dct.iteritems():
	for list in lex:
		if key == list[0]:
			if (list[1] >= -1.0) & (list[1] < -0.6):
				negative = negative + value
			elif (list[1] >= -0.6) & (list[1] < -0.2):
				weakNegative = weakNegative + value
			elif (list[1] >= -0.2) & (list[1] < 0.2):
				neutral = neutral + value
			elif (list[1] >= 0.2) & (list[1] < 0.6):
				weakPositive = weakPositive + value
			else: 
				positive = positive + value

# Finding the total number of words with sentiment values
total = negative + weakNegative + neutral + weakPositive + positive

# calculating the percentages
percentages =[(negative/total), (weakNegative/total), (neutral/total), (weakPositive/total), (positive/total)]

# labels for x-axis
xLabels = ["Negative", "Weakly Negative", "Neutral", "Weakly Positive", "Positive"]

# positions for labels and bars
bar_pos = [0.1, 1.6, 3.1, 4.6, 6.1]
label_pos = [0.5, 2.0, 3.5, 5.0, 6.5]

# Graph labels
mplot.xlabel("Sentiment")
mplot.ylabel("Percent of Words")
mplot.title("Sentiment Distribution for Challenge 2")

# making the graph
mplot.bar(bar_pos, percentages, color = "blue")

# dimensions of graph
#mplot.axis([-0.5, 8.0, 0.0, 0.4])

mplot.xticks(label_pos, xLabels)

mplot.show()



		











