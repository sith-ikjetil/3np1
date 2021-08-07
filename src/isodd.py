#!/usr/bin/python3
#: Title       : isodd main program
#: Date        : 2021-08-03
#: Author      : "Kjetil Kristoffer Solberg" <post@ikjetil.no>
#: Version     : 0.1
#: Description : Main isodd application.
#: Usage       : isodd.py <number>
import sys
import ItsMath

#
# Prints usage information
#
def PrintUsage():
    print("")
    print("Usage   : isodd.py <number>")
    print("(i)     : <number> must be greater than or equal to 1")
    print("Example : isodd.py 11")
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
            if (ItsMath.ItsMath.IsOdd(n)):
                print("Number is odd")
            else:
                print("Number is even") 
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

