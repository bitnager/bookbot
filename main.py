def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        number_of_words = count_words(file_contents)
        print(f"Number of words: {number_of_words}")

def count_words(string_to_parse):
    words = string_to_parse.split()
    return(len(words))

main()

