import requests, string, random

''' pip install requests or pip3 install requests '''

hp_text = requests.get("http://www.glozman.com/TextPages/Harry%20Potter%201%20-%20Sorcerer's%20Stone.txt")

''' to print the whole corpus, run "print hp_text.text" '''

all_words = {}
text = hp_text.text
translator = str.maketrans('', '', string.punctuation)
text = text.translate(translator)

hp_words = [word.replace('"', '') for word in text.split()]
total_words_in_book = 0
for line in hp_words:
	for word in line.split():
		word = word.lower()
		total_words_in_book += 1
		if word not in all_words:
			all_words[word] = 1
		else:
			all_words[word] += 1
###
# First find the probability of a given unigram in the corpus; P(w_i)
###
unigram_probs = {}
def unigram(w1):
	# put code here

###
# Now find all bigrams in the corpus and order them from most popular
# to least; P(w_i | w_j)
# hint: sorting based on probabilty/frequency
###

bigram_probs = {}

def all_bigrams():
	# put code here

## How would you find the 20 most popular bigrams?

###
# Find the probability of a specific bigram in the corpus; P(w_i | w_j)
###

def get_bigram(w1, w2):
	# put code here
print(get_bigram("sobbed", "Hagrid"))

###
# Sentence prediction/generation
###

# randomly generate the first word of your sentence
unique_words = [key for key in all_words.keys()]
idx = random.randrange(0, len(unique_words), 1)
start_word = unique_words[idx]

# generate a sentence given a word and a length of the sentence
# hint: define a function which chooses the next word in your sentence
# 		based on weighted probabilites of bigrams
def get_sentence(word, l=20):
	# put code here
get_sentence(start_word, 15)

