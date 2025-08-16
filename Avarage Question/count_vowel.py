# Count the number of vowels and consonants in a string.

text = input("Enter Name=")

text_new = text.lower()

vowel = "aeiou"

vowel_count = 0
cons_count = 0
for a in text_new:
    if a in vowel:
        vowel_count+=1
    else:
        cons_count+=1
print(f"Vowel={vowel_count}")
print(f"Consonants={cons_count}")