import argparse

def get_cli_arguments():
    parser = argparse.ArgumentParser(description='Pure Python command-line RSS scrapper.')
    parser.add_argument('source', help='RSS URL')
    parser.add_argument('--json', action='store_true', help='write result as JSON')
    parser.add_argument('--limit', type=int, help='Limit news topics if this parameter is provided.')
    parser.add_argument('--filename',
                         type=str, help='if provided the script will save result to a file with name in this argument',
                           default=None)
    return parser.parse_args()