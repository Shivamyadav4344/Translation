def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation+="S"
            else:
                translation+="s"
        else:
            translation+=letter
    return translation
print(translate(input("Enter the phrase:-")))

