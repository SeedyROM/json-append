import argparse

from parser import reader

def arg_parser():
    parser = argparse.ArgumentParser(
        description='A command line tool to parse, edit and traverse \
                     json files quickly and without a text-editor.'
    )

    parser.add_argument(
        'file', nargs=1,
        help='JSON file to open'
    )

    parser.add_argument(
        '-o', '--output', type=str, required=False,
        help='Output path'
    )

    return parser

def main():
    parser = arg_parser()
    args = parser.parse_args()

if __name__ == '__main__':
    main()
