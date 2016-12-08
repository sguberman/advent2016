import re


def count_tls(filename):
    with open(filename, 'r') as ip_addresses:
        return sum(supports_tls(address) for address in ip_addresses)


def supports_tls(address):
    hypernets = find_hypernets(address)
    abba_in_hypernet_sequences = any(has_abba(seq) for seq in hypernets)
    return has_abba(address) and not abba_in_hypernet_sequences


def has_abba(sequence):
    potential_abbas = re.findall(r'(.)(.)\2\1', sequence)
    #print(potential_abbas)
    actual_abbas = [abba for abba in potential_abbas if abba[0] != abba[1]]
    return len(actual_abbas) > 0


def find_hypernets(address):
    return re.findall(r'\[(.*?)\]', address)


def find_supernets(address):
    return list(address)


def find_abas(sequences):
    return sequences


def supports_ssl(address):
    return True


def count_ssl(filename):
    return 1


if __name__ == '__main__':
    print(count_tls('input.txt'))
