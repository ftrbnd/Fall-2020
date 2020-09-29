from random import shuffle

def encrypt(phrase, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_key = dict(zip(alphabet, key))

    encrypted_phrase = ""
    for letter in phrase: # iterate through the given phrase
        if letter.lower() in alphabet: # encrypt if it's a letter
            if letter.isupper(): # if the letter in the phrase is uppercase, keep the uppercase
                encrypted_phrase += alphabet_key[letter.lower()].upper()
            else: # if lowercase, add as lowercase
                encrypted_phrase += alphabet_key[letter.lower()]
        else: # add any spaces or punctuation marks
            encrypted_phrase += letter
    
    print("ORIGINAL PHRASE:", phrase)
    print("ENCRYPTED PHRASE:", encrypted_phrase)
    print()

    return encrypted_phrase

def decrypt(phrase, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_key = dict(zip(key, alphabet))

    decrypted_phrase = ""
    for letter in phrase: # iterate through the given phrase
        if letter.lower() in key: 
            if letter.isupper(): # if the letter in the phrase is uppercase, keep the uppercase
                decrypted_phrase += alphabet_key[letter.lower()].upper()
            else: # if lowercase, add as lowercase
                decrypted_phrase += alphabet_key[letter.lower()]
        else: # add any spaces or punctuation marks
            decrypted_phrase += letter
    
    print("ENCRYPTED PHRASE:", phrase)
    print("DECRYPTED PHRASE:", decrypted_phrase)
    print()

def main():
    # given phrases to encrypt
    phrase_one = "He who fights with monsters should look to it that he himself does not become a monster. And if you gaze long into an abyss, the abyss also gazes into you."
    phrase_two = "There is a theory which states that if ever anybody discovers exactly what the Universe is for and why it is here, it will instantly disappear and be replaced by something even more bizarre and inexplicable. There is another theory which states that this has already happened."
    phrase_three = "Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul; whenever I find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every funeral I meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street, and methodically knocking people’s hats off - then, I account it high time to get to sea as soon as I can."

    key = "mudkvecytjohxabrfzplnwgiqs"
    encrypted_phrase_one = encrypt(phrase_one, key)
    encrypted_phrase_two = encrypt(phrase_two, key)
    encrypted_phrase_three = encrypt(phrase_three, key)
    
    print("\n")

    decrypt(encrypted_phrase_one, key)
    decrypt(encrypted_phrase_two, key)
    decrypt(encrypted_phrase_three, key)

main()