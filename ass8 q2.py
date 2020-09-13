from io import UnsupportedOp

try:
    with open("f.txt", "r") as f:
        f.write ('This is python.')
except UnsupportedOperation:
    print("Cannot write to a file in read only mode")