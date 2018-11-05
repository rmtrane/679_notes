import sys

def main():
    if(len(sys.argv[1:]) < 1):
        data = sys.stdin
        n = 0
        for i in data:
            n += 1
        print("The number of lines in the standard input is %s" % n)
        data.close()
    else:
        for file in sys.argv[1:]:
            data = open(file, 'r')
            print("The number of lines in the file %s is %s" % (file, len(data.readlines())))
            data.close()

main()
