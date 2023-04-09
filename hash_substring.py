# python3
def read_input():
    choice = input()
    
    pattern = None
    text = None
    
    if choice == 'I':
        pattern = input()
        text = input()
    elif choice == 'F':
        with open("/home/runner/work/string-pattern-judolido/string-pattern-judolido/tests/06", 'r') as file:
            pattern = file.readline().rstrip()
            text = file.readline().rstrip()
    return pattern, text

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    p = 31  # prime number used for hashing
    m = 10**9 + 9  # modulo used for hashing to avoid integer overflow

    n = len(text)
    m = len(pattern)

    p_powers = [1]
    for i in range(1, n):
        p_powers.append((p_powers[-1] * p) % m)


    pattern_hash = 0
    window_hash = 0
    for i in range(m):
        pattern_hash = (pattern_hash * p + ord(pattern[i])) % m
        window_hash = (window_hash * p + ord(text[i])) % m

    occurrences = []
    for i in range(n - m + 1):
        if pattern_hash == window_hash:
            if pattern == text[i:i+m]:
                occurrences.append(i)
        if i < n - m:
            # update the hash of the current window
            window_hash = ((window_hash - p_powers[m-1] * ord(text[i])) * p + ord(text[i+m])) % m
            window_hash = (window_hash + m) % m  # to avoid negative numbers

    return occurrences


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

