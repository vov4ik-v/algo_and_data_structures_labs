def get_unique_chars_from_string(pattern):
    return list(set(pattern))


def get_next_state(pattern, length_pattern, state, x):
    if state < length_pattern and x == pattern[state]:
        return state + 1
    matches = 0
    for suffix_length in range(state, 0, -1):
        while matches < suffix_length - 1:
            if pattern[matches] != pattern[state - suffix_length + 1 + matches]:
                break
            matches += 1
        if matches == suffix_length - 1:
            return suffix_length

    return 0


def build_table_of_pattern(pattern):
    chars = get_unique_chars_from_string(pattern)
    table = [[0 for _ in chars] for _ in range(len(pattern) + 1)]
    for state in range(len(pattern) + 1):
        for x in range(len(chars)):
            table[state][x] = get_next_state(pattern, len(pattern), state, chars[x])
    return table


def find_the_indices_of_all_occurrences(pattern, text):
    table = build_table_of_pattern(pattern)
    chars = get_unique_chars_from_string(pattern)
    state = 0
    result_list = []
    for i in range(len(text)):
        if text[i] in chars:
            state = table[state][chars.index(text[i])]
            if state == len(pattern):
                result_list.append(i - len(pattern) + 1)
    return result_list


if __name__ == '__main__':
    print(find_the_indices_of_all_occurrences("ababaca", "ababacababacabbb"))
