import json

f = open('words_dictionary.json')

words = json.load(f)

five_words = { word: words[word] for word in words.keys() if len(word) == 5 }

with open('five_letter_words.json', 'w') as outfile:
    json.dump(five_words, outfile)
