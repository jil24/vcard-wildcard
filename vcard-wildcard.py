#!/usr/bin/env python

import sys
import argparse

def expandwildcards(wildcard):
    digits = [str(digit) for digit in range(0,10)]
    newwc = []
    if isinstance(wildcard, str):
        wildcard = wildcard.split(",")
        wildcard = [ wcs.strip() for wcs in wildcard]
    for wcs in wildcard:
        try:
            newwc.extend(expandwildcards(
                [wcs[0:wcs.index("?")] + digit + wcs[wcs.index("?")+1:]
                for digit
                in digits]))
        except ValueError:
            return wildcard
    return newwc
    


parser = argparse.ArgumentParser(description="Generate a Vcard (vcf) that contains a range of phone numbers defined by wildcards;"
                                " useful for matching automated paging systems that cycle through a range of numbers.")
parser.add_argument("--lastname")
parser.add_argument("--firstname")
parser.add_argument("--company")
parser.add_argument("number", help="number with wildcards (?) in format (555) 555 5555."
                            " Optionally, seperate multiple numbers, each containing wildcards,"
                            " with commas")
args = parser.parse_args()

for arg in ["lastname", "firstname", "company"]:
    if vars(args)[arg] is None:
        vars(args)[arg] = ""
        
print("""BEGIN:VCARD
VERSION:3.0
PRODID:-//Apple Inc.//Mac OS X 10.13.3//EN""")
print("N:"+args.lastname+";"+args.firstname+";;;")
print("FN:"+" ".join([args.lastname,args.firstname,args.company]))+";"
print("ORG:"+args.company+";")
for number in expandwildcards(args.number):
    print("TEL;type=CELL;type=VOICE;type=pref:"+number)
print("END:VCARD")
