import hashlib
from class_pregunta import Pregunta

print("The hash for Python is: " + str(hashlib.sha256('Python'.encode('utf-8')).hexdigest()))
