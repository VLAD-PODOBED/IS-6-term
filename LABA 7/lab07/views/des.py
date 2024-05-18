from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/encrypt", methods=["POST"])
def encrypt():
    text = request.json.get("enc_text")
    # Здесь должен быть код для шифрования текста DES
    encrypted_text = "Зашифрованный текст"
    encoding_time = 100  # Время шифрования в миллисекундах
    avalanche = 50  # Процент эффекта лавины
    return jsonify(result=encrypted_text, encodingTime=encoding_time, avalanche=avalanche)

@app.route("/decrypt", methods=["POST"])
def decrypt():
    text = request.json.get("dec_text")
    # Здесь должен быть код для расшифрования текста DES
    decrypted_text = "Расшифрованный текст"
    decoding_time = 120  # Время расшифрования в миллисекундах
    return jsonify(result=decrypted_text, decodingTime=decoding_time)

if __name__ == "__main__":
    app.run(debug=True)
