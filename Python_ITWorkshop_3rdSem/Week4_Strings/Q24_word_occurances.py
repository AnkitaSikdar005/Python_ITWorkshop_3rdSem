sentence = input("Enter a sentence: ")
word = input("Enter a word: ")
words = sentence.split()
count = 0
for i in words:
  print(i)
  if i==word:
        count += 1
print(count)
print(f"The word '{word}' occurs {count} times in the sentence.")