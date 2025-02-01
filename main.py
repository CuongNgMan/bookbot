

def count_string(text: str):
    words = text.split()
    return len(words)

def count_characters(text: str):
    r = {}
    for i in range(len(text)):
        if text[i].lower() in r:
            r[text[i].lower()] += 1
        else:
            r[text[i].lower()] = 1
    return r

def main():
    with open("books/frankenstein.txt") as f:
        contents = f.read()
        words = count_string(contents)
        cc = count_characters(contents)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{words} words found in the document")

        for k in cc.keys():
            if k.isalpha():
                print(f"The '{k}' character was found {cc[k]} times")




main()
