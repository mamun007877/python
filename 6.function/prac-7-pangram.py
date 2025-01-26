# pangram is a sentence that contains every letter of the alphabet at least once

def pangram(phrase):
    letters={"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"}
    return set(phrase.lower())>=letters

print(pangram("The quick brown fox jumps over the lazy dog"))