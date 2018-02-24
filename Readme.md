# vcard-wildcard


```
usage: vcard-wildcard.py [-h] [--lastname LASTNAME] [--firstname FIRSTNAME]
                         [--company COMPANY]
                         number

Generate a Vcard (vcf) that contains a range of phone numbers defined by
wildcards; useful for matching automated paging systems that cycle through a
range of numbers.

positional arguments:
  number                number with wildcards (?) in format (555) 555 5555.
                        Optionally, seperate multiple numbers, each containing
                        wildcards, with commas

optional arguments:
  -h, --help            show this help message and exit
  --lastname LASTNAME
  --firstname FIRSTNAME
  --company COMPANY
```
