class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    content = file.read().lower()
                    for punct in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        content = content.replace(punct, ' ')
                    words = content.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f"File {file_name} not found")
                all_words[file_name] = []
        return all_words

    def find(self, word):
        word = word.lower()
        result = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            try:
                position = words.index(word)
                result[name] = position
            except ValueError:
                result[name] = None
        return result

    def count(self, word):
        word = word.lower()
        result = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            result[name] = words.count(word)
        return result


if __name__ == "__main__":
    finder = WordsFinder('Walt Whitman - O Captain! My Captain!.txt', 'Grija.txt')

    print(finder.get_all_words())

    print(finder.find('the'))

    print(finder.count('the'))
