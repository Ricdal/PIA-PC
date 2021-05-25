import hashlib

def hash_archivo(file):
    ss = hashlib.sha1()
    with open(file, 'rb') as File:
        chunk = 0
        while chunk != b'':
            chunk = File.read(1024)
            ss.update(chunk)
            
    print (ss.hexdigest())        
    return ss.hexdigest()
 
