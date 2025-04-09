# Diccionarios de palíndromos y no palíndromos
palindrome_map = {
    "single_chars": list("abcxyzABCXYZ0123456789"),  # Caracteres sueltos son palíndromos
    "words": [
        "madam", "racecar", "level", "radar", "rotor",
        "civic", "deified", "kayak", "reviver", "noon", "refer",
    ],
    "phrases": [
        "A man a plan a canal Panama",
        "Was it a car or a cat I saw",
        "No lemon no melon",
        "Eva can I see bees in a cave",
    ],
    "numbers": [121, 1331, 12321, 11, 0],
}

not_palindrome_map = {
    "words": ["hello", "python", "apple", "banana"],
    "phrases": ["This is not a palindrome", "Programming is fun"],
    "numbers": [123, 4567, 89],
}
def is_palindrome(s):
    if isinstance (s, int):
        s = str(s)
        s = ''.join(c for c in s if c.isalnum()).lower() 
    return s == s[::-1]

print("===Verificacion de palindromos===")
for word in palindrome_map["words"]:
    print(f"¿'{word}' es un palindromo {is_palindrome(word)}")

print("\n=== verificacion de no palindromos===")
for word in not_palindrome_map["words"]:
    print(f"¿'{word}' es palíndromo? {is_palindrome(word)}")
# Test avanzado (frases)
print("\n=== Frases palindrómicas ===")
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("Was it a car or a cat I saw?"))    # True
