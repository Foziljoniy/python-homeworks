# q1
name = input("Enter your name: ")
year = int(input("Enter your year of birth: "))
print(f"{name} is {2024 - year} years old.")

# q2
txt = 'LMaasleitbtui'
car_name = ''.join([char for char in txt if char.lower() in 'malibu'])
print(f"Extracted car name: {car_name}")

# q3
my_string = input("Enter a string: ")
print("Length of string:", len(my_string))
print("Uppercase:", my_string.upper())
print("Lowercase:", my_string.lower())

# q4
print("Is palindrome:", my_string == my_string[::-1])

# q5
vowel_count = sum(1 for char in my_string if char.lower() in "aeiou")
print("Vowels:", vowel_count)
print("Consonants:", len(my_string) - vowel_count)

# q6
sub_string = input("Enter a substring to check: ")
print(sub_string in my_string)

# q7
sentence = input("Enter a sentence: ")
word_replace = input("Word to replace: ")
replacement_word = input("Replacement word: ")
print(sentence.replace(word_replace, replacement_word))

# q8
print("First character:", my_string[0])
print("Last character:", my_string[-1])

# q9
print("Reversed string:", my_string[::-1])

# q10
print("Number of words:", len(sentence.split()))

# q11
print("Contains digit:", any(char.isdigit() for char in my_string))

# q12
words = input("Enter words separated by spaces: ").split()
separator = input("Enter separator: ")
print(separator.join(words))

# q13
print("String without spaces:", my_string.replace(" ", ""))

# q14
a = input("Enter first string: ")
b = input("Enter second string: ")
print("Strings are equal:", a == b)

# q15
words = sentence.split()
acronym = ''.join(word[0].upper() for word in words)
print("Acronym:", acronym)

# q16
strr = input("Enter string: ")
charr = input("Character to remove: ")
print("Updated string:", strr.replace(charr, ""))

# q17
vowel_replace_str = input("Enter string: ")
print("String with vowels replaced:", ''.join('*' if char.lower() in "aeiou" else char for char in vowel_replace_str))

# q18
sen = input("Enter a sentence: ")
startt = input("Starts with: ")
endd = input("Ends with: ")
print("Matches condition:", sen.startswith(startt) and sen.endswith(endd))
