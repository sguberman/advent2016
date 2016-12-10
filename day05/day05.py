from hashlib import md5


def crack_password(door_id, length=8, start=0):
    password = ''
    int_idx = start
    door_id = bytes(door_id, encoding='utf-8')
    while len(password) < length:
        idx = bytes(str(int_idx), encoding='utf-8')
        hash_hex = md5(door_id + idx).hexdigest()
        if hash_hex.startswith('00000'):
            password += hash_hex[5]
            print('{:<20}\t{} of {}'.format(password, len(password), length))
        int_idx += 1
    return password


def crack_password2(door_id, length=8, start=0):
    password = ['#'] * length
    int_idx = start
    door_id = bytes(door_id, encoding='utf-8')
    while '#' in password:
        idx = bytes(str(int_idx), encoding='utf-8')
        hash_hex = md5(door_id + idx).hexdigest()
        if hash_hex.startswith('00000'):
            pos = hash_hex[5]
            try:
                pos = int(pos)
            except ValueError:
                int_idx += 1
                continue
            value = hash_hex[6]
            if pos in range(length) and password[pos] == '#':
                password[pos] = value
                print(''.join(password))
        int_idx += 1
    return ''.join(password)


if __name__ == '__main__':
    #print(crack_password('uqwqemis'))
    print(crack_password2('uqwqemis'))
