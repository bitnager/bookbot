def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        number_of_words = count_words(file_contents)
        # print(f"Number of words: {number_of_words}")
        histogramm = (zeichen_histogramm(file_contents))
        print_report(number_of_words, histogramm)

def count_words(string_to_parse):
    words = string_to_parse.split()
    return(len(words))

def zeichen_histogramm(string_to_parse):
    in_klein = string_to_parse.lower()
    histogramm = {}
    for i in range(0,len(in_klein)):
        buchstabe = in_klein[i]
        if not (buchstabe in histogramm):
            histogramm[buchstabe] = 1
        else:
            histogramm[buchstabe] += 1
    return histogramm

def print_report(number_of_words, histo):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{number_of_words} words found in the document")
    print()
    for letter in histo:
        if letter in "abcdefghijklmnopqrstuvwxyz":
            print(f"The '{letter}' was found {histo[letter]} times")
    print()
    print("--- End report ---")

main()

