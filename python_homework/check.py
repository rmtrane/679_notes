import sys
import numpy

def main():
    filenames = sys.argv[1:]

    ## Get rows and columns of first file
    data = numpy.loadtxt(filenames[0], delimiter = ',')
    row, col = data.shape

    ## Loop over the rest of the files
    for i in range(1, len(filenames)):
        data = numpy.loadtxt(filenames[i], delimiter = ',')
        row0, col0 = data.shape

        if (row0, col0) != (row, col):
            print("The file %s has a different number of rows/cols than the first file." % filenames[i])
        else:
            print("The file %s has the same number of rows/cols as the first file" % filenames[i])

main()
