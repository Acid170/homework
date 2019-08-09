import re
#number of words
open_file = open('lab_5.txt').read()
words = open_file.split()

print(len(words))

#Number of occurrence of a word
search_word = input("Enter search word:")
x = re.findall(search_word,open_file)
print(len(x))

#Number of lines in the text file
num_lines = 0
for line in open_file:
    num_lines += 1
print("Number of lines:" + str(num_lines))
#open_file.close()
