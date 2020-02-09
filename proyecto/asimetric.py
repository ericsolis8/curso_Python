import Crypto
import binascii
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
#1er paso generar num random a traves de entropia
random_generator = Crypto.Random.new().read
#Generacion de llaves primero se debe hacer la privada
private_key = RSA.generate(1024, random_generator)
public_key = private_key.publickey()
#exportación
private_key = private_key.exportKey(format='DER')
public_key = public_key.exportKey(format='DER')
#transformación a utf-8 es Opcional
private_key = binascii.hexlify(private_key).decode('utf8')
public_key = binascii.hexlify(public_key).decode('utf8')
#proceso inverso
private_key = RSA.importKey(binascii.unhexlify(private_key))
public_key = RSA.importKey(binascii.unhexlify(public_key))
#Mensaje a Encriptar utilizando el objeto cipher
message = 'Esto es una fiesta de locos!!'
message = message.encode()
#para encriptar es Llave publica
cipher = PKCS1_OAEP.new(public_key)
encrypted_message = cipher.encrypt(message)
print(encrypted_message)
#para decifrar es Llave privada
cipher = PKCS1_OAEP.new(private_key)
message = cipher.decrypt(encrypted_message)
print(message)