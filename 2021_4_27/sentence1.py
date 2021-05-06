import re
import reprlib


RE_WORD = re.compile('\w+')


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __len__(self):
        return len(self.words)

    def __getitem__(self, item):
        return self.words[item]

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)


# s = Sentence('niu haibao 12')
# print(s)
# print(list(s))
# print(len(s))
# for w in s:
#     print(w)
# from collections import abc
# print(isinstance(s, abc.Iterable))
# print(issubclass(s, abc.Iterable))
s = 'ABC'
it = iter(s)
while True:
    try:
        print(next(it))
    except StopIteration:
        del it
        break
