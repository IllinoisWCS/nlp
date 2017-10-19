import requests, string, random

''' pip install requests or pip3 install requests '''

hp_text = requests.get("http://www.glozman.com/TextPages/Harry%20Potter%201%20-%20Sorcerer's%20Stone.txt")

''' to print the whole corpus, run "print hp_text.text" '''

unique_words = {}
text = hp_text.text

# Remove punctation from text
translator = str.maketrans('', '', string.punctuation)
text = text.translate(translator)
# hp_words is a list of each word in the text
# (in order of appearance, duplicates included)
hp_words = [word.replace('"', '') for word in text.split()]
total_words_in_book = len(hp_words)

# Get the number of times of each word in the text appears
for line in hp_words:
    for word in line.split():
        word = word.lower()
        if word not in unique_words:
            unique_words[word] = 1
        else:
            unique_words[word] += 1
###
# First find the probability of a given unigram in the corpus; P(w_i)
###
unigram_probs = {}

def get_all_unigrams():
    pass

def unigram(w1):
    pass

get_all_unigrams()
print(unigram("Harry"))

###
# Now find all bigrams in the corpus and order them from most popular
# to least; P(w_i | w_j)
# hint: sorting based on probabilty/frequency
###

bigram_counts = {}

def get_all_bigrams():
    pass

get_all_bigrams()

###
# Get 20 most popular bigrams
###

# code here

###
# Find the probability of a specific bigram in the corpus; P(w_i | w_j)
###

def get_bigram(w1, w2):
    pass

print(get_bigram("sobbed", "Hagrid"))

###
# Sentence prediction/generation
###

# randomly generate the first word of your sentence
unique_words = [key for key in unique_words.keys()]
idx = random.randrange(0, len(unique_words), 1)
start_word = unique_words[idx]


# Generate a sentence given a word and a length of the sentence
# Hint: define a function which chooses the next word in your sentence
#       based on weighted probabilites of bigrams

def get_sentence(word, l=20):
    pass

def weighted_choice(second_word_options):
    pass

get_sentence(start_word, 15)
