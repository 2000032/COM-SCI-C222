import sys

# Please do not remove package declarations because these are used by the autograder.

# Insert your reverse_complement function here, along with any subroutines you need
reverse_dict = {"A":"T",
                "T":"A",
                "C":"G",
                "G":"C"
}
def reverse_complement(pattern: str) -> str:
    """Calculate the reverse complement of a DNA pattern."""
    new_pattern = []
    for s in pattern:
        new_pattern.append(reverse_dict[s])
    return "".join(new_pattern[::-1])