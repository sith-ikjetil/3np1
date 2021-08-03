#!/usr/bin/python3
#: Title       : 3np1 main program
#: Date        : 2021-08-03
#: Author      : "Kjetil Kristoffer Solberg" <post@ikjetil.no>
#: Version     : 0.1
#: Description : Main 3n+1 application.
#: Usage       : 3np1.py <start number>
import sys
import ItsMath

#
# Prints usage information
#
def PrintUsage():
    print("")
    print("Usage   : 3np1.py <start number>")
    print("(i)     : <start number> must be greater than or equal to 1")
    print("Example : 3np1.py 21")
    print("")

#
# Run main calc method
#
def Run(n):
    if ( n == 1 ):
        print(n)
        return

    while (n != 1):
        print(n)
        if ItsMath.ItsMath.isEven(n):
            n = int(n / 2)
        else:
            n = ((n*3)+1)

    print(n)

#
# main method
#
def main():
    try:
        if len(sys.argv) != 2:
            print("> Invalid number of arguments <")
            PrintUsage()
            return
        else:
            n = int(sys.argv[1])
            if (n <= 0):
                print("> Argument <start number> must be a number greater than or equal to 1 <")
                return
            Run(n) 
    except ValueError:
        print("> Invalid <start number> <")   
    except KeyboardInterrupt:
        print("> Program Interrupted <")

##
#: Call main if main module
##
if __name__ == "__main__":
    main()

