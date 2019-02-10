import hashlib
hash = hashlib.sha1()
hash.update(b'jkshjqwjjk')

print(hash.hexdigest())
