def count_vowels_consonants(sentence):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    for char in sentence:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
                print(f"Number of vowels: {vowel_count}")
                print(f"Number of consonants: {consonant_count}")

sentence = input("Enter a sentence: ")
count_vowels_consonants(sentence)



