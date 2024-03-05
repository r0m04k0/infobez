from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

def load_key_from_file(filename):
	with open(filename, 'rb') as f:
		return serialization.load_pem_private_key(f.read(), password=None)

def encrypt_file(public_key, input_file, output_file):
	with open(input_file, 'rb') as f:
		data = f.read()
	
	ciphertext = public_key.encrypt(
		data,
		padding.OAEP(
			mgf=padding.MGF1(algorithm=hashes.SHA256()),
			algorithm=hashes.SHA256(),
			label=None
		)
	)
	
	with open(output_file, 'wb') as f:
		f.write(ciphertext)

def decrypt_file(private_key, input_file, output_file):
	with open(input_file, 'rb') as f:
		ciphertext = f.read()
	
	plaintext = private_key.decrypt(
		ciphertext,
		padding.OAEP(
			mgf=padding.MGF1(algorithm=hashes.SHA256()),
			algorithm=hashes.SHA256(),
			label=None
		)
	)
	
	with open(output_file, 'wb') as f:
		f.write(plaintext)


private_key = rsa.generate_private_key(
	public_exponent=65537,
	key_size=2048
)

with open('./rsa/private_key.pem', 'wb') as f:
	pem = private_key.private_bytes(
		encoding=serialization.Encoding.PEM,
		format=serialization.PrivateFormat.TraditionalOpenSSL,
		encryption_algorithm=serialization.NoEncryption()
	)
	f.write(pem)

public_key = private_key.public_key()

with open('./rsa/public_key.pem', 'wb') as f:
	pem = public_key.public_bytes(
		encoding=serialization.Encoding.PEM,
		format=serialization.PublicFormat.SubjectPublicKeyInfo
	)
	f.write(pem)

encrypt_file(public_key, './rsa/input.txt', './rsa/encrypted.txt')
decrypt_file(private_key, './rsa/encrypted.txt', './rsa/decrypted.txt')

# 1. Разработать консольное приложение для шифрования/дешифрования 
# произвольных файлов с помощью алгоритма RSA.
# 2. Разработать консольное приложение для генерации ключей.
# 3. Реализовать программу для шифрования / дешифрования текстов, 
# работающую по алгоритму RSA. Программа должна уметь работать с 
# текстом произвольной длины. 