import struct

offset = 3


def find(adress, size, unpack, data):
    global offset
    s = data[adress - offset:adress - offset + size]
    s = struct.unpack(unpack, s)
    return s


def main(data):
    ans = {}
    data1 = data[offset:]
    a = 44
    b = 25
    c = 30
    d = 16
    a_str = find(3, a, '>4cIHQiHHHHHdI', data1)
    ans['A1'] = (a_str[0] +
                 a_str[1] +
                 a_str[2] +
                 a_str[3]).decode('utf-8')
    ans['A2'] = a_str[4]
    b_str = find(a_str[5], b, '>qbQhibB', data1)
    ans['A3'] = {'B1': b_str[0],
                 'B2': b_str[1],
                 'B3': b_str[2],
                 'B4': b_str[3],
                 'B5': b_str[4],
                 'B6': b_str[5],
                 'B7': b_str[6]}
    ans['A4'] = a_str[6]
    ans['A5'] = a_str[7]
    c_list = []
    for adress in a_str[8:11]:
        c_str = find(adress, c, '>QQQIH', data1)
        c_dict = {'C1': c_str[0],
                  'C2': c_str[1],
                  'C3': c_str[2],
                  'C4': list(find(c_str[4],
                                  c_str[3] * 2,
                                  f'>{c_str[3]}h',
                                  data1))}
        c_list.append(c_dict)
    ans['A6'] = c_list
    ans['A7'] = {'D1': list(find(a_str[-3],
                                 a_str[-4],
                                 a_str[-4] * 'B',
                                 data1)),
                 'D2': a_str[-2],
                 'D3': a_str[-1]}
    return ans


if __name__ == '__main__':
    import pprint

    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(main(b'KDPlkmf\x88b\x10\x06\x00/\xa4\xb9l\x96\xba,\xc6\x9f4dAY\x00N\x00'
                   b'p\x00\x92\x00\x07\x00\xb0?\xc8J\n&\xa0\x9c\x00\xe3\xc1_\x04a\x99Q(&'
                   b'\xb0pC\xb7\xefg\xcfUy\xdb\xe6<\xbf\xde\x02\xb9\xb6~8\xe4\x0b\xad\xd2f'
                   b'\x84\x16\x96\xcd4zd\xc2\x9c\xff\x89j\xb3\xc9\x81<\x05\xfa\x13\xb3\x9565\xd1'
                   b']\xc2\x00\x00\x00\x03\x00H\xe5\xeb"kT\x11GY\xb7!\x89\xc6\xe4l6\xa2'
                   b'\x06\xbe\xcff\xa8>\xfd\x87~\xa0,o\x00\x00\x00\x02\x00l\x8b\x8bS5\x95N'
                   b'D\xc6\x14\x1d7\xc8\x8b\xd0\xfd\xe3\x0e\xac\x84\xe9\xf2\x8c\xb8sx\x8a'
                   b'\x19\xb9\x00\x00\x00\x02\x00\x8e\x85u\xa7S\xed\x04\x0f'))