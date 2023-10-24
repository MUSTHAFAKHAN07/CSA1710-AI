import itertools

def is_valid_solution(words, mapping):
    values = []
    for word in words:
        value = 0
        for letter in word:
            value = value * 10 + mapping[letter]
        values.append(value)
    
    return all(values[0] + values[1] == values[2] for values in itertools.permutations(values))

def solve_cryptarithmetic(words):
    unique_letters = set("".join(words))
    
    if len(unique_letters) > 10 or len(words[0]) < len(words[-1]):
           return None

    for perm in itertools.permutations("0123456789", len(unique_letters)):
        mapping = dict(zip(unique_letters, perm))
        if is_valid_solution(words, mapping):
           return mapping

    return None

if __name__ == "__main__":
    word1 = "SEND"
    word2 = "MORE"
    result_word = "MONEY"

    words = [word1, word2, result_word]
    solution = solve_cryptarithmetic(words)

    if solution:
        print("Solution found:")
        for word in words:
            print("".join(str(solution[letter]) for letter in word))
    else:
        print("No solution exists.")

