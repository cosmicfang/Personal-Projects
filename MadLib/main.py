# First I will do it without classes and objects

# open file and read
# find < >
# make word
# ask user for answers and store
# replace()
# print
from constants import TARGET_START, TARGET_END

with open('story.txt', 'r') as f:
    story = f.read()

words = set()
start_idx = -1

for i, char in enumerate(story):
    if char == TARGET_START:
        start_idx = i

    if char == TARGET_END and start_idx != -1:
        word = story[start_idx: i + 1]
        words.add(word)
        start_idx = -1

answers = {}
for word in words:
    answers[word] = input(f"{word} : ")

for word in words:
    story = story.replace(word, answers[word])

print(story)
