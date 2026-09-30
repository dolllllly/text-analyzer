

def count_word(text):
    return len(text.split())

def count_character(text):
    return sum(1 for i in " ".join(text.split())) 

def count_vowels(text):
    vowels="aeiou"
    return sum(1 for i in text.lower() if i in vowels)

if __name__=="__main__":
    text="  PYTHon Is  fUN   "
    print(count_word(text))
    print(count_character(text))
    print(count_vowels(text))

