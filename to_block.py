import argparse


class BlockComment:
    __slots__ = ['in_file', 'out_file', 'lines', 'line_length']

    def __init__(self, args):
        self.in_file = args.in_file
        self.out_file = args.out_file
        self.lines = self.from_file()
        self.line_length = self.find_longest()
        self.export()

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
    parser = argparse.ArgumentParser(prog='to_block', description='Java block comment')
    parser.add_argument('-from', required=True, help='Filename (Required)', dest='in_file')
    parser.add_argument('-to', default='output.txt', help='Filename (Default: output.txt)', dest='out_file')
    BlockComment(parser.parse_args())
