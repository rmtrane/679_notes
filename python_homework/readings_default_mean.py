import sys
import numpy

def main():
    script = sys.argv[0]

    if all(elem not in ['--min', '--mean', '--max', None] for elem in sys.argv):
        action = '--mean'
        filenames = sys.argv[1:]
    else:
        action = sys.argv[1]
        filenames = sys.argv[2:]

    assert action in ['--min', '--mean', '--max', None], \
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
    elif action in ['--mean', None]:
        values = numpy.mean(data, axis=1)
    elif action == '--max':
        values = numpy.max(data, axis=1)

    for m in values:
        print(m)

if __name__ == '__main__':
   main()
