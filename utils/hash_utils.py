import hashlib

def calculate_hash(data):
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

