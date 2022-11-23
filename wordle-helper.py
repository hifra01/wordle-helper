#!/usr/bin/env python3

import json
import re
import sys

def get_word_list() -> list:
    with open('five_letter_words.json', 'r') as f:
        words_json: dict = json.load(f)
        words: list = list(words_json.keys())
    
    return words

def get_words_matching_pattern(pattern: str, wordlist) -> list:
    if pattern == "" or pattern is None or pattern == "-----":
        return wordlist

    regex_pattern_list = list(map(lambda x : "\w" if x == "-" else x, list(known_pattern)))
    regex_pattern_compiled = re.compile("".join(regex_pattern_list))
    matching_words = list(filter(lambda word: re.match(regex_pattern_compiled, word), wordlist))
    return matching_words

def remove_words_matching_letters(letters: str, wordlist) -> list:
    if letters == "" or letters is None or letters == "-":
        return wordlist

    regex_pattern_string = "[" + letters + "]"
    regex_pattern_compiled = re.compile(regex_pattern_string)
    filtered_words = list(filter(lambda word: regex_pattern_compiled.search(word) == None, wordlist))
    return filtered_words

def filter_words_contain_letters(letters: str, wordlist: list) -> list:
    if letters == "" or letters is None or letters == "-":
        return wordlist
    
    words = wordlist.copy()

    for letter in letters:
        words = list(filter(lambda word: re.compile("["+letter+"]").search(word), words))

    return words



if __name__ == "__main__":
    known_pattern = ""
    invalid_letters = ""
    known_letters = ""

    try:
        known_pattern = sys.argv[1]
    except IndexError:
        print("Pattern required. If not known, insert dash (-) 5 times (e.g. -----)")
        sys.exit()

    try:
        invalid_letters = sys.argv[2]
    except IndexError:
        pass

    try:
        known_letters = sys.argv[3]
    except IndexError:
        pass

    wordlist = get_word_list()

    matching_words_by_pattern = get_words_matching_pattern(known_pattern, wordlist)
    filtered_words_by_invalid_letters = remove_words_matching_letters(invalid_letters, matching_words_by_pattern)
    filtered_words_by_known_letters = filter_words_contain_letters(known_letters, filtered_words_by_invalid_letters)

    [print(word) for word in filtered_words_by_known_letters]
