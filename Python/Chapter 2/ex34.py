import re
import matplotlib.pyplot as plt
import numpy as np


class WordCount:
    def __init__(self, document):
        self._map = {}
        self._document = document
        self._countChars()

    def _countChars(self):
        for char in re.findall("[\w]", self._document):
            if char not in self._map:
                self._map[char] = 1
            else:
                self._map[char] += 1

    def get_counts(self):
        return self._map

    def draw(self):
        char = []
        times = []
        for key, val in self._map.items():
            char.append(key)
            times.append(val)
        index = np.arange(len(char))
        # print(items)
        plt.bar(index, times)
        plt.xlabel("Character", fontsize=5)
        plt.ylabel("Repetition", fontsize=5)
        plt.xticks(index, char, fontsize=5, rotation=30)
        plt.title("Char Count Chart")
        plt.show()
        # print(self._map)


if __name__ == "__main__":
    WordCount(
        "Write a Python class that extends the Progression class so that each value in the progression is the square root of the previous value. (Note that you can no longer represent each value with an integer.) Your constructor should accept an optional parameter specifying the start value, using 65,536 as a default."
    ).draw()
