import sys


def from_file(filepath):  # Get a list of stripped lines from a text file
    return [line.rstrip("\n") for line in open(filepath)]


def find_longest(lines):  # Find longest string in a list of strings
    return max([len(line) for line in lines])


def c_line(line):  # Comment line
    return f"/*   {line}{' '*(longest-len(line))}   */"


def c_block(lines):
    global longest  # Length of longest line in list
    longest = find_longest(lines)
    edge = f"/{'*'*(longest+8)}/"  # Top / bottom of comment block
    return [edge] + list(map(c_line, lines)) + [edge]  # Concatenate block


def to_file(filepath, text):  # Output text to file
    return open(filepath, "w").write("\n".join(text))


if __name__ == '__main__':
    to_file(sys.argv[2], c_block(from_file(sys.argv[1])))
