import hashlib

def hash_string(input_string):
    # Create an MD5 hash object
    md5_hash = hashlib.md5()
    
    # Update the hash object with the bytes of the string
    md5_hash.update(input_string.encode('utf-8'))
    
    # Return the hexadecimal representation of the hash
    return md5_hash.hexdigest()

def hash_file(file_path):
    # Create an MD5 hash object
    md5_hash = hashlib.md5()
    
    try:
        # Open the file in binary mode
        with open(file_path, 'rb') as file:
            # Read the file in chunks
            for chunk in iter(lambda: file.read(4096), b""):
                md5_hash.update(chunk)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None
    
    # Return the hexadecimal representation of the hash
    return md5_hash.hexdigest()

