#!/usr/bin/env python3

# setup keys
import sys
from math_tools import generate_prime, modinv
import math

def write_file(path, content):
    # save file
    with open(path, "w") as f:
        f.write(content)

def generate_keys(digits=100, k=20, diff_power=95):
    # set min diff
    diff_min = 10 ** diff_power
    
    # set e
    e = 65537
    
    # loop
    while True:
        # make p
        p = generate_prime(digits, k=k)
        
        # make q
        q = generate_prime(digits, k=k)
        
        # print status
        print("Generated candidate primes p and q")
        
        # check if same
        if p == q:
            print("p == q, regenerating")
            continue
            
        # check diff
        if abs(p - q) < diff_min:
            print("|p-q| too small, regenerating")
            continue
            
        # get n
        n = p * q
        
        # get phi
        phi = (p - 1) * (q - 1)
        
        # check e
        if math.gcd(e, phi) != 1:
            print("e not coprime with phi, regenerating")
            continue
            
        # get d
        d = modinv(e, phi)
        
        # return keys
        return n, e, d

def main():
    # set digits
    digits = 100
    
    # set rounds
    k = 20
    
    # set diff power
    diff_power = 95
    
    # print start
    print("Generating two primes (this will take some time)...")
    
    # get keys
    n, e, d = generate_keys(digits, k, diff_power)
    
    # save public
    write_file("public_key", str(n) + "\n" + str(e) + "\n")
    
    # save private
    write_file("private_key", str(d) + "\n")
    
    # print done
    print("Wrote public_key and private_key")

# start
if __name__ == "__main__":
    main()