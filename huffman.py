'''
from bs4 import BeautifulSoup
import operator
import requests


# Create a list of words
def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code,"lxml")
    # loop through each post and get text
    for post_text in soup.findAll('a', {'class': 'my3columns ua-wk ua-mac ua-wk604 ua-safari l-in Pos-r https fp fp-v2 rc1 fp-default mini-uh-on viewer-right two-col ntk-wide ltr T5002 stream-dense'}):
        content = post_text.string
        # break each post up into a list of words
        words = content.lower().split()
        for each_word in words:
            word_list.append(each_word)
    clean_up_list(word_list)




# Lowercase and remove odd symbols
def clean_up_list(word_list):
    clean_word_list = []
    for word in word_list:
        symbols = "!@#$%^&*()_+{}|:<>?,./;'[]\=-\""
        for i in range(0, len(symbols)):
            word = word.replace(symbols, "")
        if len(word) > 0:
            clean_word_list.append(word)
    create_dictionary(clean_word_list)


# Create dictionary with word counts
def create_dictionary(clean_word_list):
    word_count = {}
    for word in clean_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    # sort this dictionary by (0 for key, 1 for values)
    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print(key, value)

#help('re.findall')
start('https://en-maktoob.yahoo.com')
'''

import csv
import heapq
import zipfile
import operator
import requests


# Create a list of words
def start(file) -> object:
        with open( file, 'r' ) as bello:

            byte = bello.read( 1 )
            banana = ""
            hex_list = []
            while (byte != ""):
                byte = ord( byte )
                bits = bin( byte )[2:].rjust( 8, '0' )
                banana += bits
                hex_list.append( "{:02X}".format( byte ) )
                byte = bello.read( 1 )
           # print( hex_list )
        return hex_list
    # create_dictionary(banana)
    # Create dictionary with word counts


def create_dictionary(hexdata) -> object:
    code = {}
    for hex in hexdata:
        if hex in code:
            code[hex] += 1
        else:
            code[hex] = 1

    # sort this dictionary by (0 for key, 1 for values)
    #for key, value in sorted( code.items(), key=operator.itemgetter( 1 ) ):
        #print( key, value )
    return code





class HuffmanNode( object ):
    def __init__(self, freq, char=None, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    # used mainly for debugging purposes
    def __repr__(self):
        return "HuffmanNode(char=%s, freq=%s)" % (self.char, self.freq)

    # needed for node comparison. Utilized to order the nodes appropriately
    # in the priority queue
    def __lt__(self, other):
        return self.freq < other.freq

    def isLeaf(self):
        return (self.left == None and self.right == None)





def buildHTree(freqData) -> object:
    """

    :rtype: object
    """
    huffmanNodes = []
    for char in freqData:
        huffmanNodes.append( HuffmanNode(freqData[char], char ) )
    # the list of huffmanNodes is transformed into a priority queue to keep
    # track of the minimum-frequency Huffman Nodes
    heapq.heapify( huffmanNodes )
    while (len( huffmanNodes ) > 1):
        # obtain the two minimum-frequency Huffman nodes
        child1 = heapq.heappop( huffmanNodes )
        child2 = heapq.heappop( huffmanNodes )
        parent = HuffmanNode( child1.freq + child2.freq, left=child1, right=child2 )
        heapq.heappush( huffmanNodes, parent )
    return None if huffmanNodes == [] else heapq.heappop( huffmanNodes )




def hTreeToHCode(hTree) -> object:
    code = dict()

    # a left edge represents a 0 bit, a right edge represents a 1 bit, and
    # the path from the root to a leaf gives the code word for the character
    # stored at that leaf.
    def getCode(hNode, curCode=""):
        if (hNode == None): return
        if (hNode.left == None and hNode.right == None):
            code[hNode.char] = curCode
        getCode( hNode.left, curCode + "0" )
        getCode( hNode.right, curCode + "1" )

    getCode( hTree )

    w = csv.dictwriter( open( "output.csv", "w" ),fieldnames=(ke) )
    for key, val in code.items():
        w.writerow( [key, val] )
    return code


def pad_encoded_text(encoded_text)-> object:
        extra_padding = 8 - len(encoded_text) % 8
        for i in range(extra_padding):
            encoded_text += "0"

        padded_info = "{0:08b}".format(extra_padding)
        encoded_text = padded_info + encoded_text
        return encoded_text

def encode(s, freqData) -> object:
    hTree = buildHTree( freqData )
    hCode = hTreeToHCode( hTree )
    hEncoded = ""
    for char in s:
        hEncoded += hCode[char]
    return hEncoded.strip()




def compress(code) -> object:
    code=pad_encoded_text(code)
    with open("compressed.bin",'wb') as pikapo:
        #papples = ""

        '''
        for key, val in code.items():
            if (bananonina.index(key) > -1):
                papples+=val
        '''
        b = bytearray()
        for i in range(0, len(code), 8):
            byte = code[i:i + 8]
            b.append(int(byte, 2))
        pikapo.write(b)

   #print('yey')





def decode():
    with open ("output.csv",'r') as hana, open("compressed.bin",'rb') as dul :
        muak=bytearray(dul.read(1))
        gelato = dict(csv.DictReader(hana,fieldnames=("key","value")))
        for row in gelato:
            print(row['key'],row['value'])
        print(gelato)
        hTree = buildHTree(gelato)
        decodedStr = ""
        curTreeNode = hTree
        for charCode in muak:
            if (charCode == "0"):
                curTreeNode = curTreeNode.left
            else:
                curTreeNode = curTreeNode.right
            if (curTreeNode.isLeaf()):
                decodedStr += curTreeNode.char
                curTreeNode = hTree
    return decodedStr


frequency =create_dictionary(start('test2.txt'))
print(frequency)
string=start('test2.txt')
print(string)
code=encode(string,frequency)
#hamada =create_dictionary( start() )
print( code )
compress(code)
print(decode())

"""
import heapq
import os


class HeapNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __cmp__(self, other):
        if (other == None):
            return -1
        if (not isinstance(other, HeapNode)):
            return -1
        return self.freq > other.freq


class HuffmanCoding:
    def __init__(self, path):
        self.path = path
        self.heap = []
        self.codes = {}
        self.reverse_mapping = {}

    # functions for compression:

    def make_frequency_dict(self, text):
        frequency = {}
        for character in text:
            if not character in frequency:
                frequency[character] = 0
            frequency[character] += 1
        return frequency

    def make_heap(self, frequency):
        for key in frequency:
            node = HeapNode(key, frequency[key])
            heapq.heappush(self.heap, node)

    def merge_nodes(self):
        while (len(self.heap) > 1):
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)

            merged = HeapNode(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2

            heapq.heappush(self.heap, merged)

    def make_codes_helper(self, root, current_code):
        if (root == None):
            return

        if (root.char != None):
            self.codes[root.char] = current_code
            self.reverse_mapping[current_code] = root.char
            return

        self.make_codes_helper(root.left, current_code + "0")
        self.make_codes_helper(root.right, current_code + "1")

    def make_codes(self):
        root = heapq.heappop(self.heap)
        current_code = ""
        self.make_codes_helper(root, current_code)

    def get_encoded_text(self, text):
        encoded_text = ""
        for character in text:
            encoded_text += self.codes[character]
        return encoded_text

    def pad_encoded_text(self, encoded_text):
        extra_padding = 8 - len(encoded_text) % 8
        for i in range(extra_padding):
            encoded_text += "0"

        padded_info = "{0:08b}".format(extra_padding)
        encoded_text = padded_info + encoded_text
        return encoded_text

    def get_byte_array(self, padded_encoded_text):
        if (len(padded_encoded_text) % 8 != 0):
            print("Encoded text not padded properly")
            exit(0)

        b = bytearray()
        for i in range(0, len(padded_encoded_text), 8):
            byte = padded_encoded_text[i:i + 8]
            b.append(int(byte, 2))
        return b

    def compress(self):
        text, txt = os.path.splitext(self.path)
        output_path = text.txt + ".bin"

        with open(self.path, 'r+') as file, open(output_path, 'wb') as output:
            text = file.read()
            text = text.rstrip()

            frequency = self.make_frequency_dict(text)
            self.make_heap(frequency)
            self.merge_nodes()
            self.make_codes()

            encoded_text = self.get_encoded_text(text)
            padded_encoded_text = self.pad_encoded_text(encoded_text)

            b = self.get_byte_array(padded_encoded_text)
            output.write(bytes(b))

        print("Compressed")
        return output_path

    functions for decompression: 

    def remove_padding(self, padded_encoded_text):
        padded_info = padded_encoded_text[:8]
        extra_padding = int(padded_info, 2)

        padded_encoded_text = padded_encoded_text[8:]
        encoded_text = padded_encoded_text[:-1 * extra_padding]

        return encoded_text

    def decode_text(self, encoded_text):
        current_code = ""
        decoded_text = ""

        for bit in encoded_text:
            current_code += bit
            if (current_code in self.reverse_mapping):
                character = self.reverse_mapping[current_code]
                decoded_text += character
                current_code = ""

        return decoded_text

    def decompress(self, input_path):
        filename, file_extension = os.path.splitext(self.path)
        output_path = filename + "_decompressed" + ".txt"

        with open(input_path, 'rb') as file, open(output_path, 'w') as output:
            bit_string = ""

            byte = file.read(1)
            while (byte != ""):
                byte = ord(byte)
                bits = bin(byte)[2:].rjust(8, '0')
                bit_string += bits
                byte = file.read(1)

            encoded_text = self.remove_padding(bit_string)

            decompressed_text = self.decode_text(encoded_text)

            output.write(decompressed_text)

        print("Decompressed")
        return output_path"""

'''
import heapq

class HuffmanNode(object):
    def __init__(self, freq, char=None, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    # used mainly for debugging purposes
    def __repr__(self):
        return "HuffmanNode(char=%s, freq=%s)" % (self.char, self.freq)

    # needed for node comparison. Utilized to order the nodes appropriately
    # in the priority queue
    def __lt__(self, other):
        return self.freq < other.freq

    def isLeaf(self):
        return (self.left == None and self.right == None)

def buildHTree(freqData):
    huffmanNodes = []
    for char in freqData:
        huffmanNodes.append(HuffmanNode(freqData[char], char))
    # the list of huffmanNodes is transformed into a priority queue to keep
    # track of the minimum-frequency Huffman Nodes
    heapq.heapify(huffmanNodes)
    while (len(huffmanNodes) > 1):
        # obtain the two minimum-frequency Huffman nodes 
        child1 = heapq.heappop(huffmanNodes)
        child2 = heapq.heappop(huffmanNodes)
        parent = HuffmanNode(child1.freq + child2.freq, left=child1, right=child2)
        heapq.heappush(huffmanNodes, parent)
    return None if huffmanNodes == [] else heapq.heappop(huffmanNodes)

def hTreeToHCode(hTree):
    code = dict()
    # a left edge represents a 0 bit, a right edge represents a 1 bit, and
    # the path from the root to a leaf gives the code word for the character 
    # stored at that leaf.
    def getCode(hNode, curCode=""):
        if (hNode == None): return
        if (hNode.left == None and hNode.right == None):
            code[hNode.char] = curCode
        getCode(hNode.left, curCode + "0")
        getCode(hNode.right, curCode + "1")
    getCode(hTree)
    return code

def encode(s, freqData):
    hTree = buildHTree(freqData)
    hCode = hTreeToHCode(hTree)
    hEncoded = ""
    for char in s:
        hEncoded += hCode[char]
    return hEncoded.strip()

def decode(s, freqData):
    hTree = buildHTree(freqData)
    decodedStr = ""
    curTreeNode = hTree
    for charCode in s:
        if (charCode == "0"):
            curTreeNode = curTreeNode.left
        else:
            curTreeNode = curTreeNode.right
        if (curTreeNode.isLeaf()):
            decodedStr += curTreeNode.char
            curTreeNode = hTree
    return decodedStr

freqData = {"e":5, "o":2, "m":1, "c":1, "r":2, "f":3}
encodedStr = encode("morefreecofee", freqData)
print("encodedStr", encodedStr)
decodedStr = decode(encodedStr, freqData)
print("decodedStr", decodedStr)
'''
