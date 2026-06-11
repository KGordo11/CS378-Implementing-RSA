#!/usr/bin/env python3

import sys

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
    # get n 
    n, _ = read_public_key()
    
    # open private key
    with open("private_key", "r") as f:
        d_s = f.read().strip()
        
    # check empty
    if not d_s:
        print("Error: private_key file is empty")
        sys.exit()
        
    # make d int
    d = int(d_s)
    
    # open ciphertext
    with open("ciphertext", "r") as f:
        c_s = f.read().strip()
        
    # check empty
    if not c_s:
        print("Error: ciphertext file is empty")
        sys.exit()
        
    # make c int
    c = int(c_s)
    
    # get math tool
    from math_tools import modular_pow
    
    # translate
    m = modular_pow(c, d, n)
    
    # save message
    with open("decrypted_message", "w") as f:
        f.write(str(m) + "\n")
        
    # print done
    print("Wrote decrypted_message")


if __name__ == "__main__":
    main()