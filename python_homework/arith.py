import sys

def main():
    assert len(sys.argv) == 4, "More than three arguments given -- this is not allowed!"

    assert sys.argv[1] in ["add", "subtract"], "action not add or subtract"

    print(operation(to_do = sys.argv[1], input1 = sys.argv[2], input2 = sys.argv[3]))

def operation(to_do, input1, input2):
    if to_do == "add":
        return(float(input1) + float(input2))

    if to_do == "subtract":
        return(float(input1) - float(input2))

if __name__ == '__main__':
    main()
