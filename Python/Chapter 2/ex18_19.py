from progressions import FibonacciProgression, ArithmeticProgression

ex18 = FibonacciProgression(2, 2)
ex18.print_progression(8)

ex19 = ArithmeticProgression(128)
# 128 = 2 ^ 7
# Every time we increase 0->2^7->2^7+2^7 = 2^7*2 = 2^8 <=> pow+1
# So to come up 2^63 => at least 63-7 = 58 times calling next

