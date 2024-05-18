import math
import os
import collections
import xml.etree.ElementTree as ET
import warnings
warnings.filterwarnings("ignore")
def text_reader(path):
    with open(path, 'r') as f:
        text = f.read().lower()
    return text

def letters_dict(text):
    letters_dict = collections.defaultdict(int)
    for char in text:
        if char.isalpha() or char.isdigit():
            letters_dict[char] += 1
    return letters_dict

def probs(text):
    letter_dict = letters_dict(text)
    letters_probs = {}
    for char, count in letter_dict.items():
        letters_probs[char] = count / sum(letter_dict.values())
    return letters_probs

def count_chars_in_text(text):
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def entropy(text):
    entropy = 0
    letters_probs = probs(text)
    for prob in letters_probs.values():
        entropy += prob * math.log(prob, 2)
    return -entropy

def convert_to_ascii(text):
    ascii_text = ''
    for char in text:
        if char.isalpha():
            ascii_text += bin(ord(char))[2:]
    return ascii_text

def serialize(path, probs):
    if os.path.exists(path):
        os.remove(path)
    with open(path, 'wb') as f:
        tree = ET.ElementTree(ET.Element('probs'))
        for char, prob in probs.items():
            sub_elem = ET.SubElement(tree.getroot(), 'char')
            sub_elem.set('name', char)
            sub_elem.text = str(prob)
        tree.write(f)

def quantity_of_information(entropy, text):
    return entropy * len(text)

def mistake_quantity(mistake_prob, text, entropy):
    return len(text) * (entropy - (-mistake_prob * math.log(mistake_prob, 2) - (1 - mistake_prob) * math.log(1 - mistake_prob, 2)))
