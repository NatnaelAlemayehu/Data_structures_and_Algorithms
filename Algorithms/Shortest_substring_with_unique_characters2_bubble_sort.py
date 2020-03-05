# Write your code here
def func(coins):
    inputstring = coins
    pattern_string = "".join(list(set(inputstring)))
    array_length = 256
    string_array = [0] * array_length
    pattern_array = [0] * array_length

    count = 0
    window_length = 0
    start = 0
    min_len = float('inf')

    for i in range(0, len(pattern_string)):
            pattern_array[ord(pattern_string[i])] += 1
    for a in range(len(inputstring)):
        string_array[ord(inputstring[a])] += 1
        if (pattern_array[ord(inputstring[a])] != 0 and string_array[ord(inputstring[a])] <= pattern_array[ord(inputstring[a])]):
            count += 1
        if count == len(pattern_string):
            while (string_array[ord(inputstring[start])] > pattern_array[ord(inputstring[start])] or pattern_array[ord(inputstring[start])] == 0):
                if (string_array[ord(inputstring[start])] > pattern_array[ord(inputstring[start])]):
                    string_array[ord(inputstring[start])] -= 1
                start += 1
            window_length = a - start + 1
            if min_len > window_length:
                min_len = window_length

    return len(inputstring[start: start + min_len])
