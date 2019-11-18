import sys


class BlockComment:
    __slots__ = ['in_file', 'out_file', 'lines', 'line_length', 'comment_block']

    def __init__(self, in_file, out_file):
        self.in_file = in_file
        self.out_file = out_file
        self.lines = self.from_file()
        self.line_length = self.find_longest()

    def from_file(self):  # Get a list of stripped lines from a text file
        return list(map(lambda x: x.rstrip("\n"), open(self.in_file)))

    def find_longest(self):  # Find longest string in a list of strings
        return max(map(lambda x: len(x), self.lines))

    def comment(self, line):  # Comment line
        return f"/*   {line}{' ' * (self.line_length - len(line))}   */"

    def make_block(self):
        edge = f"/{'*' * (self.line_length + 8)}/"  # Top / bottom of comment block
        return "\n".join([edge] + list(map(self.comment, self.lines)) + [edge])  # Concatenate block

    def export(self):  # Output text to file
        open(self.out_file, "w").write(str(self))
        print(f"Exported {len(self.lines)+2} lines to '{self.out_file}'")

    def __str__(self):
        return self.make_block()


if __name__ == '__main__':
    BlockComment(sys.argv[1], sys.argv[2]).export()