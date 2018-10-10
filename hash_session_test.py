import hashlib

print("The hash for Python is: " + str(hashlib.sha256('Python'.encode('utf-8')).hexdigest()))