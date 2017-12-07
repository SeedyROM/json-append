import argparse
import sys
import os

from .parser import reader


def arg_parser():
    """Generate our ArgumentParser and setup our arguments.
    """
    parser = argparse.ArgumentParser(
        description='A command line tool to parse, edit and traverse \
                     json files quickly and without a text-editor.'
    )

    parser.add_argument(
        'file', nargs=1,
        help='JSON file to open'
    )

    parser.add_argument(
        'key', nargs=1,
        help='Key to change or get'
    )

    parser.add_argument(
        'value', nargs='?',
        help='Value to set',
    )

    parser.add_argument(
        '-o', '--output', type=str, required=False,
        help='Output path'
    )

    return parser


def main():  # pragma: no cover
    """The main entry point for our program.
    """
    parser = arg_parser()
    args = parser.parse_args()
    args.file = args.file[0]

    if not os.path.exists(args.file):
        sys.stdout.write('{}: File does not exist!\n' % args.file)
        sys.exit(-1)

    json_reader = reader(file_path=args.file)


if __name__ == '__main__':
    main()
