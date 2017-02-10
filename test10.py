def char_freq(str):
    freq = {}
    for c in str:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    return freq



print char_freq("abbabcbdbabdbdbabababcbcbab")
print char_freq("pingwin7777")