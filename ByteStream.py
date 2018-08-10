class ByteStream:
    def __init__(self):
        self.lines = []

    def append(self, msg):
        lines = msg.splitlines(True)
        if len(self.lines) > 0 and len(lines) > 0 and not self.lines[len(self.lines)-1].endswith(b'\n'):
            self.lines[len(self.lines)-1] += lines.pop(0)
        self.lines.extend(lines)

    def read_line(self):
        if len(self.lines) > 0:
            return self.lines.pop(0).rstrip(b'\n')
        else:
            return b''

    def has_next(self):
        return len(self.lines) > 0 and self.lines[0].endswith(b'\n')

if __name__ == "__main__":
    b = ByteStream()
    b.append(b'abc\n')
    b.append(b'def\naf')
    b.append(b'n\nxy\nt')
    print(b.lines)
    while b.has_next():
        print("line: " + str(b.read_line()))

