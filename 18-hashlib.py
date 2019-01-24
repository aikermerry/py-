import hashlib
import datetime

info = input("你想出入加密的语句:")

hash_lib = hashlib.md5()

hash_lib.update(info.encode("utf-8"))

print(hash_lib.hexdigest())

