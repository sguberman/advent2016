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
    hypernets = set(find_hypernets(address))
    allnets = set(re.split(r'\[(.*?)\]', address))
    return allnets - hypernets


def find_abas(sequences):
    potential_abas = []
    for seq in sequences:
        for i in range(len(seq) - 1):
            for r in re.finditer(r'(.).\1', seq[i:]):
                potential_abas.append(r.group())
    actual_abas = [aba for aba in potential_abas if aba[0] != aba[1]]
    return set(actual_abas)


def supports_ssl(address):
    hypernets = find_hypernets(address)
    supernets = find_supernets(address)
    abas = find_abas(supernets)
    for aba in abas:
        bab = aba[1] + aba[0] + aba[1]
        if any(bab in hypernet for hypernet in hypernets):
            return True
    return False


def count_ssl(filename):
    with open(filename, 'r') as ip_addresses:
        return sum(supports_ssl(address) for address in ip_addresses)


if __name__ == '__main__':
    print(count_tls('input.txt'))
    print(count_ssl('input.txt'))
