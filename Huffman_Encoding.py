import heapq

# Node class for Huffman Tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # defining comparators for priority queue
    def __lt__(self, other):
        return self.freq < other.freq

# Function to generate Huffman codes
def huffman_codes(root, code, codes_dict):
    if root is None:
        return
    # If leaf node, store the code
    if root.char is not None:
        # handle single-character case by assigning "0"
        codes_dict[root.char] = code if code != "" else "0"
        return
    huffman_codes(root.left, code + "0", codes_dict)
    huffman_codes(root.right, code + "1", codes_dict)

# Main Huffman Encoding Function
def huffman_encoding(data):
    # Count frequency of each character
    freq_dict = {}
    for char in data:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1

    # Create priority queue (min heap)
    heap = [Node(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(heap)

    # Build Huffman Tree
    if not heap:
        return {}
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    # Generate codes
    root = heap[0]
    codes_dict = {}
    huffman_codes(root, "", codes_dict)
    return codes_dict

# Driver Code
data = input("Enter the string to encode: ")
codes = huffman_encoding(data)
print("\nHuffman Codes for each character:")
for char in codes:
    print(f"{char}: {codes[char]}")
# Encode the input string
encoded_data = "".join([codes[char] for char in data])
print("\nEncoded string:")
print(encoded_data)



# Huffman Encoding is a lossless data compression algorithm based on frequency of characters.
# It assigns shorter binary codes to more frequent characters and longer codes to less frequent ones.
# The algorithm uses a greedy strategy, repeatedly combining the two least frequent symbols into a new node until one tree remains.
# The final binary tree (Huffman Tree) ensures a prefix-free code, meaning no code is a prefix of another.
# It is widely used in file compression formats such as ZIP, JPEG, and MP3.

# Algorithm
# Count frequency of each character.
# Create leaf nodes and insert into a min-heap.
# While heap has more than one node:
# Remove two smallest frequency nodes.
# Create new internal node with their sum.
# Push back into heap.
# Generate binary codes (0 for left, 1 for right).
# Print Huffman codes for each character.

# Enter string: abbcda
# Huffman Codes:
# a: 11
# b: 10
# c: 00
# d: 01
# Encoded string: 1110100111

# Step	            Time	         Space
# Frequency count	 O(n)	          O(k)
# Build heap/tree	 O(k log k)	      O(k)
# Code generation	 O(k)	          O(k)
# Total	             O(n + k log k)	  O(k)
