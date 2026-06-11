#!/usr/bin/env python3

import sys
from math_tools import modular_pow

def read_public_key(path="public_key"):
    # open file
    f = open(path, "r")
    
    # read lines
    lines = []
    for line in f:
        # keep if text
        clean_line = line.strip()
        if clean_line:
            lines.append(clean_line)
    f.close()
    
    # check two lines
    if len(lines) < 2:
        print("Error: public_key must contain n and e on separate lines")
        sys.exit()
        
    # get n e
    n = int(lines[0])
    e = int(lines[1])
    return n, e

def main():
    # min digits
    min_digits = 150
    
    # get n e
    n, e = read_public_key()
    
    # open message
    f = open("message", "r")
    message_string = f.read().strip()
    f.close()
    
    # check empty
    if not message_string:
        print("Error: message file is empty")
        sys.exit()
        
    # check length
    if len(message_string) < min_digits:
        print("Error: message must have at least " + str(min_digits) + " decimal digits")
        sys.exit()
        
    # make m int
    m = int(message_string)
    
    # check size
    if m < 0 or m >= n:
        print("Error: message must be non-negative and less than n")
        sys.exit()
        
    # encrypt
    c = modular_pow(m, e, n)
    
    # save ciphertext
    f2 = open("ciphertext", "w")
    f2.write(str(c) + "\n")
    f2.close()
    
    # print done
    print("Wrote ciphertext")

# start
if __name__ == "__main__":
    main()