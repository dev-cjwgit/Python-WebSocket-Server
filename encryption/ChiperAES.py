from Crypto import Random
from Crypto.Cipher import AES

BS = AES.block_size


def pad(m):
    # return m + ((BS - len(m) % BS) * chr(BS - len(m) % BS)).encode()
    return m + bytes([BS - len(m) % BS] * (BS - len(m) % BS))


def unpad(m):
    return m[:-int(m[-1])]


class AEScipher:
    def __init__(self, s_key = Random.new().read(32)):
        self.s_key = s_key

    def encrypt(self, plain):
        plain = pad(plain.encode())
        iv = Random.new().read(BS)
        cipher = AES.new(self.s_key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(plain)

    def decrypt(self, e):
        try:
            iv = e[:BS]
            cipher = AES.new(self.s_key, AES.MODE_CBC, iv)
            return unpad(cipher.decrypt(e[BS:])).decode()
        except Exception:
            return None



