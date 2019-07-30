from progressions import Progression
import math


class SqrtProgression(Progression):
    def __init__(self, start=65536):
        """Create a new square root progression.

        increment  the fixed constant to add to each term (default 1)
        start      the first term of the progression (default 0)
        """
        super().__init__(float(start))  # initialize base class

    def _advance(self):  # override inherited version
        """Update current value by adding the fixed increment."""
        self._current = math.sqrt(self._current)


if __name__ == "__main__":
    print("Square Root Progression:")
    SqrtProgression().print_progression(10)
