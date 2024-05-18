import random

def encode_text(text, secret_message):
    space_modification = random.randint(1, 1)  # Модификация числа пробелов
    kerning_modification = random.randint(1, 1)  # Модификация кернинга
    encoded_message = " ".join(secret_message)
    
    encoded_text = ""
    text_index = 0
    message_index = 0
    
    while text_index < len(text):
        if text[text_index] == ' ':
            for _ in range(space_modification):
                encoded_text += ' '
            text_index += 1
        else:
            for _ in range(kerning_modification):
                encoded_text += ' '
            encoded_text += text[text_index]
            text_index += 1
            
            if message_index < len(encoded_message):
                encoded_text += encoded_message[message_index]
                message_index += 1
    
    encoded_text += text[text_index:]
    
    return encoded_text

def decode_text(encoded_text):
    space_modification = 0
    kerning_modification = 0
    
    for char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
        if " " + char in encoded_text:
            expected_space_width = len(char)
            actual_space_width = len(" " + char)
            space_modification = actual_space_width - expected_space_width
            break
    
    for char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
        if " " + char in encoded_text:
            expected_width = len(char)
            actual_width = len(" " + char)
            kerning_modification = actual_width - expected_width - space_modification
            break
    
    decoded_message = ""
    index = 0
    
    while index < len(encoded_text):
        if encoded_text[index] == ' ':
            index += space_modification + 1
        else:
            decoded_message += encoded_text[index]
            index += 1
    
    return decoded_message

text = "I just returned from the greatest summer vacation! It was so fantastic, I never wanted it to end. I spent eight days in Paris, France. My best friends, Henry and Steve, went with me. We had a beautiful hotel room in the Latin Quarter, and it wasn’t even expensive. We had a balcony with a wonderful view."
secret_message = "Podobed"
encoded_text = encode_text(text, secret_message)
decoded_message = decode_text(encoded_text)

print("Оригинальный текст:", text)
print("Закодированный текст:", encoded_text)
#print("Декодированный текст:", decoded_message)