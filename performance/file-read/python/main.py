import argparse
from collections import defaultdict, Counter

def process_file(func: str, filename: str) -> None:
    print(f'Reading file {filename}')
    data = read_file(filename)
    print(f'Processing data in file {filename} using {func}')

    globals()[func](data)
    print(f'Processed data using {func}')


def read_file(filename: str) -> str:
    with open(filename) as f:
        data = f.read()

    return data

def process_data_simpledict(data: str) -> None:
    # freq table
    freq = {}
    for c in data:
        if c not in freq:
            freq[c] = 0
        freq[c] += 1

def process_data_defaultdict(data: str) -> None:
    # freq table
    freq = defaultdict(int)
    for c in data:
        freq[c] += 1

def process_data_counter(data: str) -> None:
    # freq table
    _ = Counter(data)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    parser.add_argument('func', choices=
        ['process_data_simpledict',
         'process_data_defaultdict',
         'process_data_counter']
    )
    args = parser.parse_args()

    process_file(args.func, args.filename)
