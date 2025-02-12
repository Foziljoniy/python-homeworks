#q1
year = int(input("Years: "))
name = input("name: ")
print(f"{name} is {2024-year} year")

# q2

txt = 'LMaasleitbtui'
car_name = ''.join([char for char in txt if char.lower() in 'malibu'])
print(f"Extracted car name: {car_name}")
    
# q3
my_string = input("String: ")
print(len(my_string))
my_string.upper()
my_string.lower()

#q4
print(my_string == my_string[::-1])

#q5
vowel_count = 0
vowels = "aeiouAEIOU"
for char in my_string:
    if char in vowels:
        vowel_count += 1
print(vowel_count)
print(len(my_string) - vowel_count)

#q6
g = "qw"
print(g in my_string)

#q7
sentence = input("sentence: ")
word_replace = input("replace: ")
replacement_word = input("replacement: ")
updated_sentence = sentence.replace(word_replace, replacement_word)
print(updated_sentence)

#q8
print(my_string[0])
print(my_string[-1])

#q9
print(my_string[::-1])

#q10
print(len(sentence.split()))

#q11
for i in my_string:
    if i.isdigit():
        print(True)
        break
else:
    print(False)

#q12
new_string = my_string+"_"+replacement_word
print(new_string)

#q13
yangi = my_string.replace(" ", "")

#q14
a = input()
b = input()
a == b

#q15
words = sentence.split()
acronym = ''.join(word[0].upper() for word in words)
print(acronym)

#q16
strr = input("Enter: ")
charr = input("Char")
strr.replace(charr, "")

#q18
sen = input()
startt = input()
endd = input()
sen.startswith(startt) and sen.endswith(endd)