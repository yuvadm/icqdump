import sys

DAT_HEADER = b'\x04\x00\x00\x00\x08\x00\x00\x00'


class ICQDump(object):
    def __init__(self, filename):
        self.filename = filename
        with open(self.filename, 'rb') as f:
            self.content = f.read()

    def process(self):
        header = self.content[:8]
        if header != DAT_HEADER:
            print('Wrong header, file does not appear to be an ICQ DAT file')
            exit(2)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python dump.py <datfile.dat>')
        exit(1)

    icqd = ICQDump(sys.argv[1])
    icqd.process()
