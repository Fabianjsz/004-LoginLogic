import hashlib


# MD5 hash of "steveslist"

md5 = hashlib.md5(b"steveslist")
print(md5.hexdigest())



# SHA256 hash of "steveslist"

sha256 = hashlib.sha256(b"steveslist")
print(sha256.hexdigest())