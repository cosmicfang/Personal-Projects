from constants import TARGET_START, TARGET_END

class Story:
    def __init__(self):
        self.filename = 'story.txt'
        self.words = set()
        self.start_idx = -1

    def read_file(self):
        with open(self.filename, 'r') as file:
            self.story = file.read()
        return self.story

    def find_word(self):
        for i, char in enumerate(self.story):
            if char == TARGET_START:
                self.start_idx = i
            if char == TARGET_END and self.start_idx != -1:
                word = self.story[self.start_idx: i + 1]
                self.words.add(word)
                self.start_idx = -1
        return self.words

class Answers:
    def __init__(self, story_class):
        self.answers = {}
        self.story_class = story_class

    def replace_needed(self):
        for word in self.story_class.words:
            self.answers[word] = input(f"{word} : ")

        for word in self.story_class.words:
            self.story_class.story = self.story_class.story.replace(word, self.answers[word])


if __name__ == '__main__':
    story_obj = Story()
    story_obj.read_file()
    story_obj.find_word()

    answer_obj = Answers(story_obj)
    answer_obj.replace_needed()

    print(story_obj.story)




