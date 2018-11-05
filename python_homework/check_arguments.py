import sys

def main():
    if len(sys.argv[1:]) == 0:
        print("usage: python check_argument.py filename.txt")
    else:
        print("Thanks for specifying arguments!")

main()
