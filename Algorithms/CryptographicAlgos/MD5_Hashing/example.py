from hash import hash_string
from hash import hash_file

if __name__ == "__main__":
    input_string = "Hello, world!"
    print(f"MD5 hash of '{input_string}': {hash_string(input_string)}")

    file_path = 'exampleFile.txt'  # Replace with your file path
    hash_value = hash_file(file_path)
    if hash_value:
        print(f"MD5 hash of the file '{file_path}': {hash_value}")
