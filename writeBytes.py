import sys

def main():
    file = open(sys.argv[1], 'wb')
    i = 0
    arr = bytearray()
    while i < 5242880:
        byte = b'\x10'
        arr.extend(byte)
        i += 1
    file.write(arr)
    file.close()

main()    
