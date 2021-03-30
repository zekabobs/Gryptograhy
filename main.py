from cryptography.fernet import Fernet

file_path = 'data.txt'
key_path = 'crypto.key'

def main():
    key = read_key()
    print('Ключ шифрования: ', key)
    write_text(key)
    data = read_text(key)
    print('Расшифрованный текст: ', data)

def generate_key():
    key = Fernet.generate_key()
    with open(key_path, 'wb') as f:
        f.write(key)

def read_key():
    return open(key_path, 'rb').read()


def read_text(key):
    f = Fernet(key)
    with open(file_path, 'rb') as file:
        data = file.read()
        decrypted_data = (f.decrypt(data)).decode('utf-8')
        return decrypted_data

def write_text(key):
    f = Fernet(key)
    data = input('Исходный текст: ')
    encrypted_data = f.encrypt(data.encode('utf-8'))
    print('Зашифрованный текст: ', encrypted_data)

    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

if __name__ == '__main__':
    main()
