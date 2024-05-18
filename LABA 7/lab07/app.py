from flask import Flask, request, render_template, jsonify
from Crypto.Cipher import DES
import time

app = Flask(__name__)

ALGORITHM_KEY = b"podobedv"

def encryption(plain_text):
    cipher = DES.new(ALGORITHM_KEY, DES.MODE_ECB)
    padded_text = plain_text + ' ' * (8 - len(plain_text) % 8)
    encrypted_text = cipher.encrypt(padded_text.encode())
    return encrypted_text.hex()

def decrypt(encrypted_text):
    cipher = DES.new(ALGORITHM_KEY, DES.MODE_ECB)
    decrypted_text = cipher.decrypt(bytes.fromhex(encrypted_text)).decode().strip()
    return decrypted_text

def avalanche_effect(original_text):
    changed_bits = 0
    encrypted_text1 = encryption(original_text)
    stringWithOneBitChanged = original_text[:-1] + ('1' if original_text[-1] == '0' else '0')
    encrypted_text2 = encryption(stringWithOneBitChanged)

    for char1, char2 in zip(encrypted_text1, encrypted_text2):
        if char1 != char2:
            changed_bits += 1

    return changed_bits / len(encrypted_text1) * 100

@app.route("/")
def index():
    return render_template('des.html')

@app.route("/encryption", methods=["POST"])
def encrypt_route():
    start_time = time.perf_counter()
    encrypted_text = encryption(request.json["enc_text"])
    end_time = time.perf_counter()
    encoding_time = round((end_time - start_time) * 1000, 4)

    avalanche = avalanche_effect(request.json["enc_text"])

    return jsonify({
        "result": encrypted_text,
        "avalanche": avalanche,
        "encodingTime": encoding_time
    })

@app.route("/decrypt", methods=["POST"])
def decrypt_route():
    start_time = time.perf_counter()
    decrypted_text = decrypt(request.json["dec_text"])
    end_time = time.perf_counter()
    decoding_time = round((end_time - start_time) * 1000, 4)

    return jsonify({
        "result": decrypted_text,
        "decodingTime": decoding_time
    })

if __name__ == "__main__":
    app.run(debug=True)
