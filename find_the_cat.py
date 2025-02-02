import random
import string
import re
print('all library imported\n')

# Generate alphabets
letters = string.ascii_lowercase

# Generate a random number from a string
random_sequence = random.randint(10,50)
print(random_sequence)

# Generate random words
merge = []
for i in range(0,random_sequence):
    merge.append(letters[random.randint(0,len(letters)-1)])
print(merge)

# Lower levels with for loop and if else
# level 1 :  1 character only
cat = letters[random.randint(0,len(letters)-1)]
print(f'find : {cat}')
if cat in merge:
    print(f'cat found on {[i for i, letters in enumerate(merge) if letters == cat]}')
    print('level 1 complete\n')
else:
    print('cat not found')
    print('level 1 complete\n')

# level 2 : strings
## For loops and if else solution
random_strings = []

for i in range(0,random_sequence):
    random_string = []
    for i in range(0,5):
        random_string.append(letters[random.randint(0,len(letters)-1)])
    gen_str = ''.join(random_string)
    random_strings.append(gen_str)

print(random_strings)

found_pos = [index for index, string in enumerate(random_strings) if cat in string]
print(f'cat found on {found_pos}\n')          

# Level 3 : find substrings
import english_words as word
wordset = word.get_english_words_set(['web2'], lower=True)
wordlist = list(wordset)
word_list = []

for i in range(0,random_sequence):
    word_list.append(wordlist[random.randint(0,len(wordlist)-1)])

print(word_list)
found_pos = [index for index,string in enumerate(word_list) if re.search(r'cat',string) is not None ]
print(found_pos)