import os
import csv

def convert_gandhari_to_unicode(sentence: str):


    unicode_mapping = {}
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gandhari2uni.csv'), 'r', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            unicode_hex, converted_string = row
            unicode_mapping["0x" + unicode_hex] = converted_string
    
    sentence_unicode = ""
    for c in sentence:
        hex_char = hex(ord(c))
        try:
            sentence_unicode += unicode_mapping[hex_char]
        except:
            sentence_unicode += c
    
    return(sentence_unicode)

if __name__ == '__main__':
    sentence = "(1.1:1.2) pyāyadhvam aghnyā devabhāgáṃ prajvatīr ana(OP.1.1:1.3)mīv ayakṣmḥ //"
    s = convert_gandhari_to_unicode(sentence)
    print(s)