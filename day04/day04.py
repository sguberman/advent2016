from collections import Counter, defaultdict, deque
from string import ascii_lowercase


def parse_room(room):
    *encrypted_name, after = room.strip().split('-')
    encrypted_name = '-'.join(encrypted_name)
    sector_id, checksum = after.strip(']').split('[')
    sector_id = int(sector_id)
    return encrypted_name, sector_id, checksum


def is_real(encrypted_name, checksum):
    encrypted_name = ''.join(encrypted_name.split('-'))
    letter_counts = Counter(encrypted_name)
    count_letters = defaultdict(list)
    for k, v in letter_counts.items():
        count_letters[v].append(k)
    for key in count_letters:
        count_letters[key].sort()
    true_checksum = []
    for count, letters in sorted(count_letters.items(), reverse=True):
        if len(true_checksum) == 5:
            break
        #print(count, letters)
        for letter in letters:
            true_checksum.append(letter)
            if len(true_checksum) == 5:
                break
    true_checksum = ''.join(true_checksum)
    #print(true_checksum)
    return true_checksum == checksum


def real_rooms(filename):
    with open(filename, 'r') as roomfile:
        for room in roomfile:
            encrypted_name, sector_id, checksum = parse_room(room)
            if is_real(encrypted_name, checksum):
                yield encrypted_name, sector_id


def sector_id_sum(filename):
    return sum(sector_id for _, sector_id in real_rooms(filename))


def decrypt(encrypted_name, sector_id):
    keys = ascii_lowercase
    values = deque(ascii_lowercase)
    values.rotate(-1 * sector_id)
    rotate = dict(zip(keys, values))
    rotate['-'] = ' '
    decrypted = [rotate[letter] for letter in encrypted_name]
    return ''.join(decrypted)


def sector_id_from_keywords(filename, keywords):
    keywords = keywords.split()
    for encrypted_name, sector_id in real_rooms(filename):
        if all(keyword in decrypt(encrypted_name, sector_id) for keyword in keywords):
            return sector_id


if __name__ == '__main__':
    print(sector_id_sum('input.txt'))
    print(sector_id_from_keywords('input.txt', 'north pole object'))
