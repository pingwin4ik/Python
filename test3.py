def reverse(string):
    result = []
    for word in string.split()[::-1]:
        result.append(word[::-1])
    return " ".join(result)


print reverse("I am a pingwin")