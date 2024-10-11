import os
import sys
from typing import Dict, Optional
import argparse
import heapq
from collections import defaultdict
from dataclasses import dataclass
import json

@dataclass
class Node:
    char: Optional[str]
    count: int
    left: Optional['Node'] = None
    right: Optional['Node'] = None

    def __lt__(self, other: 'Node') -> bool:
        return self.count < other.count


def encode_text(data: str):
    tab = build_freq_table(data)

    root = build_huffman_tree(tab)

    code_table: Dict[str, str] = {}

    # assign bits to each edge
    # DFS traversal: preorder
    def build_code_table(node: Node, code: str):
        if node.char is not None:
            code_table[node.char] = code
            return

        build_code_table(node.left, code + '0')
        build_code_table(node.right, code + '1')


    build_code_table(root, '')

    encoded_text = ''
    for char in data:
        encoded_text += code_table[char]

    return encoded_text, tab


def build_huffman_tree(tab: Dict[str, int]) -> Node:
    min_heap = []
    for char, count in tab.items():
        node = Node(char=char, count=count)
        heapq.heappush(min_heap, node)

    while len(min_heap) > 1:
        node1 = heapq.heappop(min_heap)
        node2 = heapq.heappop(min_heap)

        merged_node = Node(
            char=None,
            count=node1.count+node2.count,
            left=node1,
            right=node2,
        )

        heapq.heappush(min_heap, merged_node)

    root = heapq.heappop(min_heap)
    return root


def build_freq_table(data: str) -> Dict[str, int]:
    tab = defaultdict(int)
    for char in data:
        tab[char] += 1
    return tab


def decode_text(data: str) -> str:
    # read freq_table from header
    parts = data.split('\n\n')
    if len(parts) != 2:
        raise ValueError('Data is improperly encoded')

    header, encoded_data = parts[0], parts[1]

    freq_table = json.loads(header)

    root = build_huffman_tree(freq_table)

    decoded_data = ''
    curr = root
    for bit in encoded_data:
        if bit == '0':
            curr = curr.left
        else:
            curr = curr.right

        if curr.char is not None:
            decoded_data += curr.char
            curr = root

    return decoded_data


def write_encoded_data(data: str, freq_table, filename: str):
    header = json.dumps(freq_table)
    with open(filename, 'w') as file:
        file.write(header)
        file.write('\n\n')
        file.write(data)


def write_decoded_data(data: str, filename: str):
    with open(filename, 'w') as file:
        file.write(data)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('action', help='encode or decode', choices=['encode', 'decode'])
    parser.add_argument('-i', '--infile', help='Input file')
    parser.add_argument('-o', '--outfile', help='Output file')
    args = parser.parse_args()

    action = args.action
    infile = args.infile
    outfile = args.outfile

    if not os.path.exists(infile):
        print(f"ERROR: File {infile} not found.")
        sys.exit(1)

    if not os.access(infile, os.R_OK):
        print(f"ERROR: File {infile} is not readable.")
        sys.exit(1)

    data: str = ''
    with open(infile, 'r') as file:
        data = file.read()

    if action == 'encode':
        encoded_text, freq_table = encode_text(data)
        write_encoded_data(encoded_text, freq_table, outfile)
        sys.exit(0)

    if action == 'decode':
        decoded_text = decode_text(data)
        write_decoded_data(decoded_text, outfile)
        sys.exit(0)

