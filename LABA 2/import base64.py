from base64 import b64encode
import base64
from collections import Counter
import math

# 1-Функция для кодирования содержимого файла в формат Base64
def encode_file_to_base64(file_path, output_file_path):
    with open(file_path, "rb") as file:
        file_content = file.read()
        base64_bytes = b64encode(file_content)
        base64_message = base64_bytes.decode('ascii')
        with open(output_file_path, "w") as output_file:
            output_file.write(base64_message)
file_path = "text.txt"
output_file_path = "output.txt"
encode_file_to_base64(file_path, output_file_path)
print("Файл успешно закодирован в формат BASE64 и сохранен в", output_file_path)
#2
def calculate_frequency_distribution(text):
    total_count = len(text)
    frequency_distribution = {char: count / total_count for char, count in Counter(text).items()}
    return frequency_distribution
def calculate_entropy_hartley(frequency_distribution):
    alphabet_size = len(frequency_distribution)
    return math.log2(alphabet_size)
def calculate_entropy_shannon(frequency_distribution):
    probabilities = list(frequency_distribution.values())
    return -sum(p * math.log2(p) for p in probabilities)
def calculate_redundancy(frequency_distribution):
    entropy_hartley = calculate_entropy_hartley(frequency_distribution)
    entropy_shannon = calculate_entropy_shannon(frequency_distribution)
    return ((entropy_hartley - entropy_shannon)/entropy_hartley) * 100

def read_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text
document_a_path = "text.txt"
document_b_path = "output.txt"

document_a = read_text_from_file(document_a_path)
document_b = read_text_from_file(document_b_path)

frequency_distribution_a = calculate_frequency_distribution(document_a)
frequency_distribution_b = calculate_frequency_distribution(document_b)

entropy_hartley_a = calculate_entropy_hartley(frequency_distribution_a)
entropy_shannon_a = calculate_entropy_shannon(frequency_distribution_a)
redundancy_a = calculate_redundancy(frequency_distribution_a)

entropy_hartley_b = calculate_entropy_hartley(frequency_distribution_b)
entropy_shannon_b = calculate_entropy_shannon(frequency_distribution_b)
redundancy_b = calculate_redundancy(frequency_distribution_b)

# Вывод результатов
print("Документ A:")
print("Частотное распределение:", frequency_distribution_a)
print("Энтропия Хартли:", entropy_hartley_a)
print("Энтропия Шеннона:", entropy_shannon_a)
print("Избыточность:", redundancy_a)

print("\nДокумент B:")
print("Частотное распределение:", frequency_distribution_b)
print("Энтропия Хартли:", entropy_hartley_b)
print("Энтропия Шеннона:", entropy_shannon_b)
print("Избыточность:", redundancy_b)
#3
def convert_to_base64(input_text):
    import base64
    base64_result = base64.b64encode(input_text.encode('utf-8')).decode('utf-8')
    return base64_result

def xor_buffers(a, b):
    result = ""
    length = max(len(a), len(b))

    for i in range(length):
        a_value = int(a[i], 2) if i < len(a) else 0
        b_value = int(b[i], 2) if i < len(b) else 0
        xor_value = a_value ^ b_value
        result += f"{xor_value:08b} "  # Добавляем ведущие нули до 8 бит

    return result.strip()

def ascii_to_buffer(string):
    buffer = []
    for char in string:
        buffer.append(f"{ord(char):08b} ")
    return buffer

def base64_to_buffer(string):
    import base64
    binary = base64.b64decode(string.encode('utf-8'))
    buffer = []
    for byte in binary:
        buffer.append(f"{byte:08b} ")
    return buffer

a = ascii_to_buffer('PODOBED')
aa = ascii_to_buffer('VLADISLAV')
b = base64_to_buffer('UE9ET0JFRA==')
bb = base64_to_buffer('VkxBRElTTEFW')

print("Name ASCII:", a)
print("Sname ASCII:", aa)
print("XOR ASCII:", xor_buffers(a, aa))

print("Name base64:", b)
print("Sname base64:", bb)
print("XOR base64:", xor_buffers(b, bb))
