#!/usr/bin/env python3
"""
Author : mtoucedasuarez <mtoucedasuarez@localhost>
Date   : 2021-09-15
Purpose: Rock the Casbah
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input string or file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type = str,
                        default = '')



    args = parser.parse_args()                                           
 
    if os.path.isfile(args.text):                                        
        args.text = open(args.text).read().rstrip()                      
 
    return args 


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()                                                   
    out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout   
    out_fh.write(args.text.upper() + '\n')                              
    out_fh.close()                                                      
 



# --------------------------------------------------
if __name__ == '__main__':
    main()


