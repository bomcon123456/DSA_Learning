from progressions import Progression


class AbsoluteDifferenceProgression(Progression):
    def __init__(self, first=0, second=1):
        """Create a new Absolute DifferenceProgression progression.

        first      the first term of the progression (default 0)
        second     the second term of the progression (default 1)
        """
        super().__init__(first)  # start progression at first
        self._next = second  # fictitious value preceding the first

    def _advance(self):
        self._next, self._current = abs(self._current - self._next), self._next


if __name__ == "__main__":
    print("Absolute Difference Progression:")
    AbsoluteDifferenceProgression(2, 200).print_progression(10)

