def cleaned(text):
    return " ".join(text.lower().split())

if __name__=="__main__":    # execute only if you run it directly
    print(cleaned("    PYTHon  is Fun  "))