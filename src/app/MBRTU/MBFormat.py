import struct
import time


def ReadFloat(*args):
    for n, m in args:
        n, m = '%04x' % n, '%04x' % m
    v = n + m
    y_bytes = v.decode('hex')
    y = struct.unpack('!f', y_bytes)[0]
    y = round(y, 6)
    return y


def WriteFloat(value):
    y_bytes = struct.pack('!f', value)
    y_hex = y_bytes.encode('hex')
    n, m = y_hex[:-4], y_hex[-4:]
    n, m = int(n, 16), int(m, 16)
    v = [n, m]
    return v


def ReadDint(*args):
    for n, m in args:
        n, m = '%04x' % n, '%04x' % m
    v = n + m
    y_bytes = v.decode('hex')
    y = struct.unpack('!i', y_bytes)[0]
    return y


def WriteDint(value):
    y_bytes = struct.pack('!i', value)
    y_hex = y_bytes.encode('hex')
    n, m = y_hex[:-4], y_hex[-4:]
    n, m = int(n, 16), int(m, 16)
    v = [n, m]
    return v


def ReadInt(*args):
    for v in args:
        v = '%d' % v
    return int(v)


def WriteInt(value):
    v = [value]
    return v


#print(ReadFloat((15729, 16458)))
# print(WriteFloat(3.16))
#print(ReadDint((1734, 6970)))
# print(WriteDint(456787654))
def str_to_hex(s):
    return ' '.join([hex(ord(c)).replace('0x', '').zfill(2).upper() for c in s])


def hex_to_str(s):
    return ''.join([chr(i) for i in [int(b, 16) for b in s.split(' ')]])


def str_to_bin(s):
    return ' '.join([bin(ord(c)).replace('0b', '') for c in s])


def bin_to_str(s):
    return ''.join([chr(i) for i in [int(b, 2) for b in s.split(' ')]])


def currtime():
    return ':'.join(str(i).zfill(2) for i in time.localtime()[3:6])
