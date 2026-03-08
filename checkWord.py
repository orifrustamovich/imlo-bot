from uzwords import words
from difflib import get_close_matches

print(len(words))

def checkWord(word):
    word = word.lower()
    matches = set(get_close_matches(word, words, n=3))
    available = False


    if word in matches:
        available = True
        matches = word

    elif "ҳ" in word:
        word = word.replace("ҳ", "х")
        matches.update(get_close_matches(word, words, n=3))

    elif "х" in word:
        word = word.replace("х", "ҳ")
        matches.update(get_close_matches(word, words, n=3))



    return {'available':available, 'matches':matches}



if __name__ == "__main__":
    print(checkWord('кийим'))
    print(checkWord('мано'))
    print(checkWord('хавас'))
    print(checkWord('ҳато'))
    print(checkWord('тариҳ'))



