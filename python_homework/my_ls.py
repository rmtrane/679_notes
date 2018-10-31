import sys
import glob

def main():
    assert len(sys.argv) < 3, "more than one argument given"
    print(sorted(glob.glob('*.' + sys.argv[1])))

if __name__ == "__main__":
    main()
