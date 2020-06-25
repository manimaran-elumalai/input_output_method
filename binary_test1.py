a = 65534               # FF FE
b = 65535               # FF FF
c = 65536               # 00 01 00 00
d = 2998382             # 02 2D C0 1E

with open('sample1_binary', 'bw') as binary_file:
    binary_file.write(a.to_bytes(2, 'big'))
    binary_file.write(b.to_bytes(2, 'big'))
    binary_file.write(c.to_bytes(4, 'big'))
    binary_file.write(d.to_bytes(4, 'big'))
    binary_file.write(d.to_bytes(4, 'little'))

with open('sample1_binary', 'br') as binary_file:
    e = int.from_bytes(binary_file.read(2), 'big')
    print(e)
    f = int.from_bytes(binary_file.read(2), 'big')
    print(f)
    g = int.from_bytes(binary_file.read(4), 'big')
    print(g)
    h = int.from_bytes(binary_file.read(4), 'big')
    print(h)
    i = int.from_bytes(binary_file.read(4), 'big')
    print(i)