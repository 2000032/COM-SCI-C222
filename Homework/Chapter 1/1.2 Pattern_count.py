import sys

# Please do not remove package declarations because these are used by the autograder.

# Insert your PatternCount function here, along with any subroutines you need
def pattern_count(text: str, pattern: str) -> int:
  count = 0
  for i in range(0, len(text) - len(pattern) + 1):
    if text[i: i+len(pattern)] == pattern:
      count += 1
  return count