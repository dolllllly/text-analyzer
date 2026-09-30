from .cleaning import cleaned
from .metrics import count_vowels,count_character,count_word

def generate_report(text):
    cleaned_text=cleaned(text)
    words=count_word(cleaned_text)
    characters=count_character(cleaned_text)
    vowels=count_vowels(cleaned_text)

    return (
         "\n----------------text report--------------------------\n"

        f"cleaned text: {cleaned_text}\n"
        f"total words: {words}\n"
        f"total characters: {characters}\n"
        f"total vowels: {vowels}"

    )