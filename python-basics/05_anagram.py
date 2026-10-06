word1 = input("Enter first word: ").strip().lower()
word2 = input("Enter second word: ").strip().lower()

word1 = word1.replace(" ", "")
word2 = word2.replace(" ", "")

if sorted(word1) == sorted(word2):
    print("The words are Anagrams.")
else:
    print("The words are NOT Anagrams.")
