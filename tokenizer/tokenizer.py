import re

class Tokenizer:
    def __init__(self):
        self.token_pattern = re.compile(r"""(?x)
            (?:[A-Z]\.)+                    # abbreviations, e.g. U.S.A.
          | \$\d+(?:\.\d+)?                 # currency like $5.99
          | \d+(?:\.\d+)?%                  # percentage like 20%
          | \w+(?:-\w+)*                    # words with optional hyphens
          | \.\.\.|[.,;!?()\"']             # punctuation or ellipsis
        """)

    def tokenize(self, text):
        return self.token_pattern.findall(text)
