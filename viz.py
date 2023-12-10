# Harsh Pandya
from lab3 import huffman
from lab3.huffman import text_encoding, text_decoding
import argparse
def print_huffman_tree(node, level=0):
    if node is None:
        return

    print("  " * level, end="")
    if node.char:
        print(f"'{node.char}':{node.freq}")
    else:
        print("─┐")
        print_huffman_tree(node.left, level + 1)
        print_huffman_tree(node.right, level + 1)

def generate_encoding_steps_text(text, encoding_table):
    steps_text = "Encoding steps:\n"
    for char in text:
        char_upper = char.upper()  # Convert to uppercase
        if char_upper in encoding_table:
            code = encoding_table[char_upper]
            steps_text += f"'{char}' → {code}\n"
    return steps_text

def huffman_visualize(freq_table_file_path):
    # Read frequency table from file
    freq_table = {}
    with open(freq_table_file_path, 'r') as freq_file:
        for line in freq_file:
            char, freq = line.strip().split(' - ')
            freq_table[char] = int(freq)

    # Build Huffman Encoding Tree
    huffman_root = huffman.huffman_tree_builder(freq_table)

    print("Huffman Tree:")
    print_huffman_tree(huffman_root)

# Call the function with the freq_table_file_path
if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("freq_table_file", type=str, help="Frequency table file pathname")
    args = arg_parser.parse_args()
    huffman_visualize(args.freq_table_file)