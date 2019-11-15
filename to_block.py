import sys, os


def from_file(filepath):
    return [line.rstrip("\n") for line in open(filepath)]


def find_longest(lines):
    return max([len(line) for line in lines])


def c_line(line):
    return f"/*   {line}{' '*(longest-len(line))}   */"


def c_block(lines):
    global longest
    longest = find_longest(lines)
    edge = f"/{'*'*(longest+8)}/"
    return [edge] + list(map(c_line, lines)) + [edge]


def to_file(filepath, text):
    return open(filepath, "w").write("\n".join(text))


if __name__ == '__main__':
    to_file(sys.argv[2], c_block(from_file(sys.argv[1])))
