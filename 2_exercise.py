def most_vowel_element(lst):
    def vowel_count(word):
        vowels = "aeiou"
        count = 0
        for letter in word:
            if letter.lower() in vowels:
                count += 1
        return count
    
    max_vowel_word = None
    max_vowel_count = 0
    
    for word in lst:
        curr_count = vowel_count(word)
        if curr_count > max_vowel_count:
            max_vowel_word = word
            max_vowel_count = curr_count
    
    return max_vowel_word, max_vowel_count

arr1 = ["hello", "world", "google", "independent"]
word1, count1 = most_vowel_element(arr1)
print("Javob:", f'"{word1}", {count1} ta unli')

