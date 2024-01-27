def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    words = file_contents.split()
    count = 0
    l = len(words)

    for i in range(l):
        count += 1
    
    letters = {}

    for c in file_contents:
        if c.isalpha():
            if c.lower() in letters:
                letters[c.lower()] += 1
            else:
                letters[c.lower()] = 1

    letters = list(letters.items())
    letters.sort(key=lambda item: item[1], reverse=True)
    l = len(letters)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count} words found in the document")
    print()
    
    for i in range(l):
        print(f"The {letters[i]} character was found {letters[i][1]} times")

    print("--- End report ---")
    

main()
