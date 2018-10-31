import sys
import numpy

def main():

    if len(sys.argv) == 1:
        print("""To run this script, specify one of --min --mean --max and filename(s) (optional). The specified action will then be performed on said file""", "\n",
              """If filename is left blank, the standard input will be used""", "\n",
              """Example: python readings_w_help.py --min small01.csv""",  sep = "")
        return

    script = sys.argv[0]
    action = sys.argv[1]
    filenames = sys.argv[2:]

    assert action in ['--min', '--mean', '--max'], \
           'Action is not one of --min, --mean, or --max: ' + action
    if len(filenames) == 0:
        process(sys.stdin, action)
    else:
        for f in filenames:
            process(f, action)

def process(filename, action):
    data = numpy.loadtxt(filename, delimiter=',')

    if action == '--min':
        values = numpy.min(data, axis=1)
    elif action == '--mean':
        values = numpy.mean(data, axis=1)
    elif action == '--max':
        values = numpy.max(data, axis=1)

    for m in values:
        print(m)

if __name__ == '__main__':
   main()
