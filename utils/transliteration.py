from argparse import ArgumentParser
import sys

# International Alphabet of Sanskrit Transliteration
iast = [
    r"aí",  # ai with udatta
    r"aì",  # ai with svarita
    r"ai",  # ai
    r"aú",  # au with udatta
    r"aù",  # au with svarita
    r"au",  # au
    r"ā́",  # long a with udatta,\u+0101\u+0301
    r"ā̀",  # long a with svarta,\u+0101\u+0300
    r"á",  # a with udatta,\u+00E1
    r"à",  # a with svarta,\u+00E0
    r"ā",  # long a,\u+0101
    r"ī́",  # long i with udatta,\u+012B\u+0301
    r"ī̀",  # long i with svarta,\u+012B\u+0300
    r"í",  # i with udatta,\u+00ED
    r"ì",  # i with svarta,\u+00EC
    r"ī",  # long i,\u+012B
    r"ū́",  # long u with udatta,\u+016B\u+0301
    r"ū̀",  # long u with svarta,\u+016B\u+0300
    r"ú",  # u with udatta,\u+00FA
    r"ù",  # u with svarta,\u+00F9
    r"ū",  # long u,\u+0016B
    r"r̥̄́",  # long vowel r with udatta,\u+0072\u+0325\u+0304\u+0301
    r"r̥̄̀",  # long vowel r with svarta,\u+0072\u+0325\u+0304\u+0300
    r"ŕ̥",  # vowel r with udatta,\u+0072\u
    r"r̥̀",  # vowel r with svarta
    r"r̥̄",  # long vowel r
    r"r̥",  # vowel r
    # r"l̥̄́",  # long vowel l with udatta
    # r"l̥̄̀",  # long vowel l with svarta
    r"ĺ̥",  # vowel l with udatta
    r"l̥̀",  # vowel l with svarta
    # r"l̥̄",  # long vowel l
    r"l̥",  # vowel l
    r"é",  # e with udatta
    r"è",  # e with svarta
    r"e",  # e
    r"ó",  # e with udatta
    r"ò",  # o with svarta
    r"o",  # o
    r"kh",  # aspirated k
    r"gh",  # aspirated g
    r"ch",  # aspirated c
    r"jh",  # aspirated j
    r".th",  # aspirated retroflex t
    r".dh",  # aspirated retroflex d
    r";lh",  # aspirated retroflex l
    r"th",  # aspirated t
    r"dh",  # aspirated d
    r"ph",  # aspirated p
    r"bh",  # aspirated B
    r"ṅ",  # velar nasal
    r"ñ",  # palatal nasal
    r"ṇ",  # retroflex nasal
    r"j",  # palatal plosive
    r"ṭ",  # retroflex t
    r"ḍ",  # retroflex d
    r"ḷ",  # retroflex l
    r"y",  # semivowel y
    r"ś",  # palatal sibilant
    r"ṣ",  # retroflex sibilant
    r"ḫ",  # upadhmaniya
    r"ẖ",  # jihvamuliya
    r"ṃ",  # anusvara
    r"ṁ",  # anusvara
    r"m̐",  # anunasika
    r"ḥ"  # visarga
]

# International Phonetic Alphabet
ipa = [
    r"aí",  # ai with udatta
    r"aì",  # ai with svarita
    r"ai",  # ai
    r"aú",  # au with udatta
    r"aù",  # au with svarita
    r"au",  # au
    r"áː",  # long a with udatta
    r"àː",  # long a with svarta
    r"á",  # a with udatta
    r"à",  # a with svarta
    r"aː",  # long a
    r"íː",  # long i with udatta
    r"ìː",  # long i with svarta
    r"í",  # i with udatta
    r"ì",  # i with svarta
    r"iː",  # long i
    r"úː",  # long u with udatta
    r"ùː",  # long u with svarta
    r"ú",  # u with udatta
    r"ù",  # u with svarta
    r"uː",  # long u
    r"ŕ̩ː",  # long vowel r with udatta
    r"r̩̀ː",  # long vowel r with svarta
    r"ŕ̩",  # vowel r with udatta
    r"r̩̀",  # vowel r with svarta
    r"r̩ː",  # long vowel r
    r"r̩",  # vowel r
    # r"ĺ̩ː",  # long vowel l with udatta
    # r"l̩̀ː",  # long vowel l with svarta
    r"ĺ̩",  # vowel l with udatta
    r"l̩̀",  # vowel l with svarta
    # r"l̩ː",  # long vowel l
    r"l̩",  # vowel l
    r"éː",  # e with udatta
    r"èː",  # e with svarta
    r"eː",  # e
    r"óː",  # e with udatta
    r"òː",  # o with svarta
    r"oː",  # o
    r"kʰ",  # aspirated k
    r"gʰ",  # aspirated g
    r"cʰ",  # aspirated c
    r"jʰ",  # aspirated j
    r"ʈʰ",  # aspirated retroflex t
    r"ɖʰ",  # aspirated retroflex d
    r";lh",  # aspirated retroflex l
    r"tʰ",  # aspirated t
    r"dʰ",  # aspirated d
    r"pʰ",  # aspirated p
    r"bʰ",  # aspirated B
    r"ŋ",  # velar nasal
    r"ɲ",  # palatal nasal
    r"ɳ",  # retroflex nasal
    r"ɟ",  # palatal plosive
    r"ʈ",  # retroflex t
    r"ɖ",  # retroflex d
    r";l",  # retroflex l
    r"j",  # semivowel y
    r"ś",  # palatal sibilant
    r"ʂ",  # retroflex sibilant
    r"ḫ",  # upadhmaniya
    r"ẖ",  # jihvamuliya
    r"ṃ",  # anusvara
    r"ṁ",  # anusvara
    r"m̐",  # anunasika
    r"h"  # visarga
]

# Tokunaga-Fujii
tf = [
    r";ai",  # ai with udatta
    r":ai",  # ai with svarita
    r"ai",  # ai
    r";au",  # au with udatta
    r":au",  # au with svarita
    r"au",  # au
    r";aa",  # long a with udatta
    r":aa",  # long a with svarta
    r";a",  # a with udatta
    r":a",  # a with svarta
    r"aa",  # long a
    r";ii",  # long i with udatta
    r":ii",  # long i with svarta
    r";i",  # i with udatta
    r":i",  # i with svarta
    r"ii",  # long i
    r";uu",  # long u with udatta
    r":uu",  # long u with svarta
    r";u",  # u with udatta
    r":u",  # u with svarta
    r"uu",  # long u
    r";..rr",  # long vowel r with udatta
    r":..rr",  # long vowel r with svarta
    r";.r",  # vowel r with udatta
    r":.r",  # vowel r with svarta
    r"..rr",  # long vowel r
    r".r",  # vowel r
    # r";..ll",  # long vowel l with udatta
    # r":..ll",  # longvVowel l with svarta
    r";.l",  # vowel l with udatta
    r":.l",  # vowel l with svarta
    # r"..ll",  # long vowel l
    r".l",  # vowel l
    r";e",  # e with udatta
    r":e",  # e with svarta
    r"e",  # e
    r";o",  # e with udatta
    r":o",  # o with svarta
    r"o",  # o
    r"kh",  # aspirated k
    r"gh",  # aspirated g
    r"ch",  # aspirated c
    r"jh",  # aspirated j
    r".th",  # aspirated retroflex t
    r".dh",  # aspirated retroflex d
    r";lh",  # aspirated retroflex l
    r"th",  # aspirated t
    r"dh",  # aspirated d
    r"ph",  # aspirated p
    r"bh",  # aspirated B
    r":n",  # velar nasal
    r";n",  # palatal nasal
    r".n",  # retroflex nasal
    r"j",  # palatal plosive
    r".t",  # retroflex t
    r".d",  # retroflex d
    r";l",  # retroflex l
    r"y",  # semivowel y
    r";s",  # palatal sibilant
    r".s",  # retroflex sibilant
    r".f",  # upadhmaniya
    r".x",  # jihvamuliya
    r".m",  # anusvara
    r":m",  # anusvara
    r";m",  # anunasika
    r".h"  # visarga
]

# Kyoto-Harvard
kh = [
    r";ai",  # ai with udatta
    r":ai",  # ai with svarita
    r"ai",  # ai
    r";au",  # au with udatta
    r":au",  # au with svarita
    r"au",  # au
    r";A",  # long a with udatta
    r":A",  # long a with svarta
    r";a",  # a with udatta
    r":a",  # a with svarta
    r"A",  # long a
    r";I",  # long i with udatta
    r":I",  # long i with svarta
    r";i",  # i with udatta
    r":i",  # i with svarta
    r"I",  # long i
    r";U",  # long u with udatta
    r":U",  # long u with svarta
    r";u",  # u with udatta
    r":u",  # u with svarta
    r"U",  # long u
    r";RR",  # long vowel r with udatta
    r":RR",  # long vowel r with svarta
    r";R",  # vowel r with udatta
    r":R",  # vowel r with svarta
    r"RR",  # long vowel r
    r"R",  # vowel r
    # r";LL",  # long vowel l with udatta
    # r":LL",  # long vowel l with svarta
    r";L",  # vowel l with udatta
    r":L",  # vowel l with svarta
    # r"LL",  # long vowel l
    r"L",  # vowel l
    r";e",  # e with udatta
    r":e",  # e with svarta
    r"e",  # e
    r";o",  # e with udatta
    r":o",  # o with svarta
    r"o",  # o
    r"kh",  # aspirated k
    r"gh",  # aspirated g
    r"ch",  # aspirated c
    r"jh",  # aspirated j
    r".th",  # aspirated retroflex t
    r".dh",  # aspirated retroflex d
    r";lh",  # aspirated retroflex l
    r"th",  # aspirated t
    r"dh",  # aspirated d
    r"ph",  # aspirated p
    r"bh",  # aspirated B
    r"G",  # velar nasal
    r"J",  # palatal nasal
    r"N",  # retroflex nasal
    r"j",  # palatal plosive
    r"T",  # retroflex t
    r"D",  # retroflex d
    r";l",  # retroflex l
    r"y",  # semivowel y
    r"z",  # palatal sibilant
    r"S",  # retroflex sibilant
    r"f",  # upadhmaniya
    r"x",  # jihvamuliya
    r"M",  # anusvara
    r":m",  # anusvara
    r";m",  # anunasika
    r"H"  # visarga
]

# SLP1
slp1 = [
    r";E",  # ai with udatta
    r":E",  # ai with svarita
    r"E",  # ai
    r";O",  # au with udatta
    r":O",  # au with svarita
    r"O",  # au
    r";A",  # long a with udatta
    r":A",  # long a with svarta
    r";a",  # a with udatta
    r":a",  # a with svarta
    r"A",  # long a
    r";I",  # long i with udatta
    r":I",  # long i with svarta
    r";i",  # i with udatta
    r":i",  # i with svarta
    r"I",  # long i
    r";U",  # long u with udatta
    r":U",  # long u with svarta
    r";u",  # u with udatta
    r":u",  # u with svarta
    r"U",  # long u
    r";F",  # long vowel r with udatta
    r":F",  # long vowel r with svarta
    r";f",  # vowel r with udatta
    r":f",  # vowel r with svarta
    r"F",  # long vowel r
    r"f",  # vowel r
    # r";LL",  # long vowel l with udatta
    # r":LL",  # long vowel l with svarta
    r";x",  # vowel l with udatta
    r":X",  # vowel l with svarta
    # r"LL",  # long vowel l
    r"x",  # vowel l
    r";e",  # e with udatta
    r":e",  # e with svarta
    r"e",  # e
    r";o",  # e with udatta
    r":o",  # o with svarta
    r"o",  # o
    r"K",  # aspirated k
    r"G",  # aspirated g
    r"C",  # aspirated c
    r"J",  # aspirated j
    r"W",  # aspirated retroflex t
    r"Q",  # aspirated retroflex d
    r"Q",  # aspirated retroflex l
    r"T",  # aspirated t
    r"D",  # aspirated d
    r"P",  # aspirated p
    r"B",  # aspirated B
    r"N",  # velar nasal
    r"Y",  # palatal nasal
    r"R",  # retroflex nasal
    r"j",  # palatal plosive
    r"w",  # retroflex t
    r"q",  # retroflex d
    r"q",  # retroflex l
    r"y",  # semivowel y
    r"S",  # palatal sibilant
    r"z",  # retroflex sibilant
    r"H",  # upadhmaniya
    r"H",  # jihvamuliya
    r"M",  # anusvara
    r"M",  # anusvara
    r"M",  # anunasika
    r"H"  # visarga
]


# Tsukagoshi
tsu = [
    r";E",  # ai with udatta
    r":E",  # ai with svarita
    r"E",  # ai
    r";O",  # au with udatta
    r":O",  # au with svarita
    r"O",  # au
    r";A",  # long a with udatta
    r":A",  # long a with svarta
    r";a",  # a with udatta
    r":a",  # a with svarta
    r"A",  # long a
    r";I",  # long i with udatta
    r":I",  # long i with svarta
    r";i",  # i with udatta
    r":i",  # i with svarta
    r"I",  # long i
    r";U",  # long u with udatta
    r":U",  # long u with svarta
    r";u",  # u with udatta
    r":u",  # u with svarta
    r"U",  # long u
    r";Q",  # long vowel r with udatta
    r":Q",  # long vowel r with svarta
    r";q",  # vowel r with udatta
    r":q",  # vowel r with svarta
    r"Q",  # long vowel r
    r"q",  # vowel r
    # r";LL",  # long vowel l with udatta
    # r":LL",  # long vowel l with svarta
    r";L",  # vowel l with udatta
    r":L",  # vowel l with svarta
    # r"LL",  # long vowel l
    r"L",  # vowel l
    r";e",  # e with udatta
    r":e",  # e with svarta
    r"e",  # e
    r";o",  # e with udatta
    r":o",  # o with svarta
    r"o",  # o
    r"K",  # aspirated k
    r"G",  # aspirated g
    r"C",  # aspirated c
    r"J",  # aspirated j
    r"W",  # aspirated retroflex t
    r"X",  # aspirated retroflex d
    r"X",  # aspirated retroflex l
    r"T",  # aspirated t
    r"D",  # aspirated d
    r"P",  # aspirated p
    r"B",  # aspirated B
    r"V",  # velar nasal
    r"Y",  # palatal nasal
    r"N",  # retroflex nasal
    r"j",  # palatal plosive
    r"w",  # retroflex t
    r"x",  # retroflex d
    r"x",  # retroflex l
    r"y",  # semivowel y
    r"z",  # palatal sibilant
    r"S",  # retroflex sibilant
    r"f",  # upadhmaniya
    r"F",  # jihvamuliya
    r"M",  # anusvara
    r"M",  # anusvara
    r"M",  # anunasika
    r"H"  # visarga
]

# URW Palladio CSX+ (Classical Sanskrit Extended Plus)
csx = [
    0,  # ai with udatta
    0,  # ai with svarita
    0,  # ai
    0,  # au with udatta
    0,  # au with svarita
    0,  # au
    181,  # long a with udatta
    182,  # long a with svarta
    158,  # a with udatta
    133,  # a with svarta
    224,  # long a
    183,  # long i with udatta
    184,  # long i with svarta
    161,  # i with udatta
    141,  # i with svarta
    227,  # long i
    189,  # long u with udatta
    190,  # long u with svarta
    163,  # u with udatta
    151,  # u with svarta
    229,  # long u
    179,  # long vowel r with udatta
    0,  # logn vowel r wihg svarta
    198,  # or 177#vowel r with udatta
    199,  # or 178#vowel r with svarta
    233,  # or 174#long vowel r
    231,  # or 157#vowel r
    # 0,  # long vowel l with udatta
    # 0,  # long Vvwel l with svarta
    0,  # vowel l with udatta
    0,  # vowel l with svarta
    # 237,  # or 176#long vowel l
    235,  # or 175#vowel l
    130,  # e with udatta
    138,  # e with svarta
    101,  # e
    162,  # e with udatta
    149,  # o with svarta
    111,  # o
    107104,  # aspirated k
    103104,  # aspirated g
    99104,  # aspirated c
    106104,  # aspirated j
    241104,  # aspirated retroflex t
    243104,  # aspirated retroflex d
    0,  # aspirated retroflex l
    116104,  # aspirated t
    100104,  # aspirated d
    112104,  # aspirated p
    98104,  # aspirated B
    239,  # velar nasal
    164,  # palatal nasal
    245,  # retroflex nasal
    106,  # palatal plosive
    241,  # retroflex t
    243,  # retroflex d
    0,  # retroflex l
    121,  # semivowel y
    247,  # palatal sibilant
    249,  # retroflex sibilant
    220,  # upadhmaniya
    219,  # jihvamuliya
    252,  # anusvara
    167,  # anusvara
    193,  # anunasika
    254  # visarga
]


# class Transliteration:

#     sentence = None
#     input_trans = None
#     output_trans = None

#     def __init__(self, sentence, input_trans='kh', output_trans='iast'):
#         self.sentence = sentence
#         self.input = input_trans
#         self.output = output_trans
#         # self.transliterated = ''
#         print(self.sentence)
    
#     def transliterate(self):
#         lst1 = ["kh", "iast", "tf", "ipa", "slp1", "tsu"]
#         lst2 = [kh, iast, tf, ipa, slp1, tsu]

#         try:
#             lst_ip = lst2[lst1.index(self.input)]
#         except:
#             print('Input method error.')
#             sys.exit()
        
#         try:
#             lst_op = lst2[lst1.index(self.output)]
#         except:
#             print('Output method error')
#             sys.exit()
        
#         translit = self.sentence
#         print(self.sentence)
#         for i in range(len(lst_ip)):
#             translit = translit.replace(lst_ip[i], lst_op[i])
        
#         return translit



def transliterate(sent, ip, op):
    lst1 = ["kh", "iast", "tf", "ipa", "slp1", "tsu"]
    lst2 = [kh, iast, tf, ipa, slp1, tsu]
    # print('ip', ip)
    try:
        lst_ip = lst2[lst1.index(ip)]
    except:
        print("Input method error")
        sys.exit()
    try:
        lst_op = lst2[lst1.index(op)]
    except:
        print("Output method error")
        sys.exit()

    translit = sent
    for i in range(len(lst_ip)):
        translit = translit.replace(lst_ip[i], lst_op[i])
    return translit
