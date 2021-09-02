#!/usr/bin/env python3
"""
Author : mtoucedasuarez <mtoucedasuarez@arizona.edu>
Date   : 2021-09-01
Purpose: Print greeting
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Greetings and salutations',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-g','--greeting',
                        metavar='str',
                        help='The greeting', 
                        type=str,
                        default="Howdy")

    parser.add_argument('-n',
                        '--name',
                        help='Whom to greet',
                        metavar='str',
                        type=str,
                        default='Stranger')

    parser.add_argument('-e',
                        '--excited',
                        help='Include an exclamation',
                        action='store_true')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    greeting_arg = args.greeting
    name_arg = args.name
    excited_arg = args.excited
    
    bang = '!' if excited_arg == True else '.'

    print('{}, {}{}'.format(greeting_arg, name_arg, bang))
   


# --------------------------------------------------
if __name__ == '__main__':
    main()
