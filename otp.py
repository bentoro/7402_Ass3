#!/usr/bin/python3.5

#
# =====================================================================================
#
#       Filename:  otp.py
#
#    Description: Take file or keyboard input and xor the plaintext with a random key
#
#        Created:  02/8/2019
#
#         Author:  Benedict Lo
#
# =====================================================================================
import sys, random, argparse

def main (argv):
    content = ""
    output = ''

    #if len (sys.argv[1:]) < 3:
     #   print ('Usage: ./otp.py -f <ciphertext file> or -m <ciphertext message> and -o <output file>')
      #  sys.exit(2)

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', action="store",dest="filename")
    parser.add_argument('-m', action="store",dest="message")
    parser.add_argument('-o', action="store",dest="output", required=True)

    #generate random key

    if parser.parse_args().filename:
        filename = str(parser.parse_args().filename)
        file = open(filename)
        content = file.read()
    elif parser.parse_args().message:
        file = open('input.txt', 'w+')
        file.write(parser.parse_args().message)
        file = open('input.txt', 'r')
        content = file.read()

    outfile = str(parser.parse_args().output)

    xormessage(content, outfile)

#
# =====================================================================================
#
#       Function:  generaterandom()
#
#     Parameters: void
#
#    Description: Generate random key
#
#        Created:  02/8/2019
#
#         Author:  Benedict Lo
#
# =====================================================================================

def generaterandom():
    return int(random.random()*255.0)


#
# =====================================================================================
#
#       Function:  xormessage()
#
#     Parameters: void
#
#    Description: XOR the provided message
#
#        Created:  02/8/2019
#
#         Author:  Benedict Lo
#
# =====================================================================================


def xormessage(content, outfile):
    key = generaterandom()
    fileout = open(outfile, 'w')

    for i in range(0, len(content)):
        msg =  content.encode('utf8')
        line = msg[i].split(" ")
        word = line[0]
        for i in range (0,len(word)):
            wd = ord(word[i])
            encrypt = wd ^ key
            fileout.write(chr(encrypt))
        fileout.write(" ")

    fileout.close()


if __name__ == "__main__":
    main (sys.argv[1:])
