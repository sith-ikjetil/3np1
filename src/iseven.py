#!/usr/bin/python3
#: Title       : iseven main program
#: Date        : 2021-08-03
#: Author      : "Kjetil Kristoffer Solberg" <post@ikjetil.no>
#: Version     : 0.1
#: Description : Main iseven application.
#: Usage       : iseven.py <number>
import sys
import ItsMath

#
# Prints usage information
#
def PrintUsage():
    print("")
    print("Usage   : iseven.py <number>")
    print("(i)     : <number> must be greater than or equal to 1")
    print("Example : iseven.py 11")
    print("")

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
                print("> Argument <number> must be a number greater than or equal to 1 <")
                PrintUsage()
                return
            if (ItsMath.ItsMath.IsEven(n)):
                print("Number is even")
            else:
                print("Number is odd") 
    except ValueError:
        print("> Invalid <number> <")
        PrintUsage()
    except KeyboardInterrupt:
        print("> Program Interrupted <")

##
#: Call main if main module
##
if __name__ == "__main__":
    main()

