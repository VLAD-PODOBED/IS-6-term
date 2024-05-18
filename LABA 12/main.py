import hashlib
import time
from Crypto import Random
from Crypto.Util.number import getRandomRange
from Crypto.PublicKey import ElGamal, RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
import ecdsa

# Генерация ключевой пары RSA
rsa_key = RSA.generate(2048)
# print("Ключевая пара RSA:")
# print(rsa_key.export_key())

# Подписание сообщения RSA
message = b"hdkjflshkjkw'sdfls"
start_time = time.time()
hash_obj = SHA256.new(message)
rsa_signature = PKCS1_v1_5.new(rsa_key).sign(hash_obj)
end_time = time.time()
print(f"Время подписи сообщения RSA: {end_time - start_time} секунд")

# Проверка подписи RSA
try:
    PKCS1_v1_5.new(rsa_key.publickey()).verify(hash_obj, rsa_signature)
    print("Подпись RSA действительна.")
except (ValueError, TypeError):
    print("Подпись RSA недействительна.")

messageSH = b"887b2f31073ebbe81813ddf535bc7cddbcc9bcd051b7542d77093304f996a5ee"
# Генерация ключевой пары Шнорра
secp256k1_sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
# print("\nКлючевая пара Шнорра:")
# print(secp256k1_sk.to_string())

# Подписание сообщения Шнорра
start_time = time.time()
hash_obj = hashlib.sha256(messageSH).digest()
secp256k1_signature = secp256k1_sk.sign(hash_obj, sigencode=ecdsa.util.sigencode_der)
end_time = time.time()
print(f"Время подписи сообщения Шнорра: {end_time - start_time} секунд")

# Проверка подписи Шнорра
secp256k1_vk = secp256k1_sk.get_verifying_key()
if secp256k1_vk.verify(secp256k1_signature, hash_obj, sigdecode=ecdsa.util.sigdecode_der):
    print("Подпись Шнорра действительна.")
else:
    print("Подпись Шнорра недействительна.")

messageG =b"a429046e0249a29e58aaafc92a6040a4c82b8ab3e84016373bf1140d8e01f228"
# Генерация ключевой пары Эль-Гамаля
secp256k1_sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
# print("\nКлючевая пара Шнорра:")
# print(secp256k1_sk.to_string())

# Подписание сообщения Эль-Гамаля
start_time = time.time()
hash_obj = hashlib.sha256(messageG).digest()
secp256k1_signature = secp256k1_sk.sign(hash_obj, sigencode=ecdsa.util.sigencode_der)
end_time = time.time()
print(f"Время подписи сообщения Эль-Гамаля: {end_time - start_time} секунд")

# Проверка подписи Эль-Гамаля
secp256k1_vk = secp256k1_sk.get_verifying_key()
if secp256k1_vk.verify(secp256k1_signature, hash_obj, sigdecode=ecdsa.util.sigdecode_der):
    print("Подпись Эль-Гамаля действительна.")
else:
    print("Подпись Эль-Гамаля недействительна.")

# Генерация ключевой пары Эль-Гамаля
elgamal_key = ElGamal.generate(2048, Random.new().read)
print("\nКлючевая пара Эль-Гамаля:")
print(elgamal_key.export_key())

# Подписание сообщения Эль-Гамаля
start_time = time.time()
hash_obj = SHA256.new(message)
elgamal_signature = elgamal_key.sign(hash_obj, '')
end_time = time.time()
print(f"Время подписи сообщения Эль-Гамаля: {end_time - start_time} секунд")

# Проверка подписи Эль-Гамаля
if elgamal_key.verify(hash_obj, elgamal_signature):
    print("Подпись Эль-Гамаля действительна.")
else:
    print("Подпись Эль-Гамаля недействительна.")
