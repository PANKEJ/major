import hashlib

def hashfunction(candidateID,mac0="qwertyuipasdfghjklzxcvbnm"):
    mac1=hashlib.sha512(str(mac0+candidateID).encode()).hexdigest()[:16]
    return mac1
