from collections import Counter
from heapq import heappush, heappop, heapify

def encode_huffman(data):
    """Encodes the given data using Huffman coding."""

    frequency = Counter(data)

    heap = [[weight, [char, ""]] for char, weight in frequency.items()]
    heapify(heap)

    # Build the Huffman tree
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]: # builds the codes with the tree
            pair[1] = '0' + pair[1] #lower node goes to the left and gets the 0
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    huffman_codes = sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

    huffman_dict = {char: code for char, code in huffman_codes}

    encoded_data = ''.join(huffman_dict[char] for char in data)

    return encoded_data, huffman_dict

def decode_huffman(encoded_data, huffman_dict):
    """Decodes the given encoded data using the provided Huffman dictionary."""
    
    reverse_huffman_dict = {v: k for k, v in huffman_dict.items()}
    current_code = ""
    decoded_data = ""

    for bit in encoded_data:
        current_code += bit
        if current_code in reverse_huffman_dict:
            decoded_data += reverse_huffman_dict[current_code]
            current_code = ""

    return decoded_data

def compression_ratio(original_data, encoded_data):
    """Calculates the compression ratio."""
    
    original_size = len(original_data) * 8  # Assuming 8 bits per character
    encoded_size = len(encoded_data)
    
    return (original_size - encoded_size) / original_size * 100 

string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac."

encoded, huff_dict = encode_huffman(data=string)
string_decode =  decode_huffman(encoded_data=encoded, huffman_dict=huff_dict)
compression_ratio = compression_ratio(original_data=string, encoded_data=encoded)
string_bytes = string.encode('utf-8')
print(f"""
String original:
{string}

String codificada:
{encoded}
String decodificada:
{string_decode}

Taxa de compressão:
{compression_ratio}
""" )