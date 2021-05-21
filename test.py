import hashlib

m = hashlib.new('sha512_256')
m.update(b"random words")
print(m.hexdigest())
