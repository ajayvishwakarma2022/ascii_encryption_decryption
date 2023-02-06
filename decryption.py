encrypt_text=input("enter the encrypted data")
key = int(input("enter the key in integer number:"))
def decryption():
    decrypt_data =""
    for i in encrypt_text :
        decrypt_data +=chr(ord(i ) +key)
        print("decryption using ASCII value:" ,decrypt_data)

decryption()