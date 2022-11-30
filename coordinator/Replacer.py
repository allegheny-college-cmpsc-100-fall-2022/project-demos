class Replacer:

    def __init__(self, template, word):
        template = template.text
        word = word.value
        self.result = template.replace("_ADJ_", word)