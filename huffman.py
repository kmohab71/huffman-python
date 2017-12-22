
import csv
import heapq
import pickle
import zipfile
import operator
import binascii
import requests


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
        return hex_list


def create_dictionary(hexdata) -> object:
    code = {}
    for hex in hexdata:
        if hex in code:
            code[hex] += 1
        else:
            code[hex] = 1
 
    return code


class HuffmanNode( object ):
    def __init__(self, freq, char=None, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __repr__(self):
        return "HuffmanNode(char=%s, freq=%s)" % (self.char, self.freq)
    def __lt__(self, other):
        return self.freq < other.freq

    def isLeaf(self):
        return (self.left == None and self.right == None)





def buildHTree(freqData) -> object:
    huffmanNodes = []
    for char in freqData:
        huffmanNodes.append( HuffmanNode(freqData[char], char ) )
    heapq.heapify( huffmanNodes )
    while (len( huffmanNodes ) > 1):
        child1 = heapq.heappop( huffmanNodes )
        child2 = heapq.heappop( huffmanNodes )
        parent = HuffmanNode( child1.freq + child2.freq, left=child1, right=child2 )
        heapq.heappush( huffmanNodes, parent )
    return None if huffmanNodes == [] else heapq.heappop( huffmanNodes )




def hTreeToHCode(hTree) -> object:
    code = dict()

    def getCode(hNode, curCode=""):
        if (hNode == None): return
        if (hNode.left == None and hNode.right == None):
            code[hNode.char] = curCode
        getCode( hNode.left, curCode + "0" )
        getCode( hNode.right, curCode + "1" )

    getCode( hTree )
    print(code,'\n')
    with open("dict_code.pickle",'wb') as pickle_code:
        pickle.dump(code,pickle_code)

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

        b = bytearray()
        for i in range(0, len(code), 8):
            byte = code[i:i + 8]
            b.append(int(byte, 2))
        pikapo.write(b)
        

def remove_padding(padded_encoded_text):
        padded_info = padded_encoded_text[:8]
        extra_padding = int(padded_info, 2)

        padded_encoded_text = padded_encoded_text[8:]
        encoded_text = padded_encoded_text[:-1 * extra_padding]

        return encoded_text




def decode():
    with open("dict_code.pickle",'rb') as oreo, open("compressed.bin",'rb') as dul, open("decompressed.txt",'w')as tictoc :
        muak=""

        byte = dul.read(1)
        while len(byte) !=0:
            byte = ord(byte)
            bits = bin(byte)[2:].rjust(8, '0')
            muak += bits
            byte = dul.read(1)

        muak_decompressed=remove_padding(muak)
        print(muak_decompressed)
        temp_dict=pickle.load(oreo)
        hoho={y:x for x,y in temp_dict.items()}
        print(hoho)
        decodedStr = ""
        searching_list=""
        k=0
        while k != len(muak_decompressed):
          searching_list+=(muak_decompressed[k])
        
          if searching_list in hoho:

              decodedStr+=hoho[searching_list]
              searching_list=''
              decodedStr=binascii.unhexlify(decodedStr)
              tictoc.write(decodedStr.decode('windows-1252'))
              decodedStr=''
          k=k+1



frequency =create_dictionary(start('test2.txt'))
print(frequency)
string=start('test2.txt')
code=encode(string,frequency)
compress(code)
decode()

