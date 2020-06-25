with open('samplebinary', 'bw') as binary_file:
    # for i in range(17):
    #     binary_file.write(bytes([i]))
    binary_file.write(bytes(range(17)))

with open('samplebinary', 'br') as binary_file:
    for b in binary_file:
        print(b)