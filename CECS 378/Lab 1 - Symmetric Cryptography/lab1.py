import collections
from collections import Counter

# returns the key for a value
def get_key(val, dictionary): 
    for key, value in dictionary.items(): 
         if val == value: 
             return key 

def main():
    # alphabet and their numeric values
    letter_values = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, 
    "i": 8, "j": 9, "k": 10, "l": 11, "m": 12, "n": 13, "o": 14, "p": 15, "q": 16, 
    "r": 17, "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23, "y": 24, "z": 25}

    phrase_one = "fqjcb rwjwj vnjax bnkhj whxcq nawjv nfxdu mbvnu ujbbf nnc"
    phrase_two = "oczmz vmzor jocdi bnojv dhvod igdaz admno ojbzo rcvot jprvi oviyv aozmo cvooj ziejt dojig toczr dnzno jahvi fdiyv xcdzq zoczn zxjiy"
    phrase_three = "ejitp spawa qleji taiul rtwll rflrl laoat wsqqj atgac kthls iraoa twlpl qjatw jufrh lhuts qataq itats aittk stqfj cae"
    phrase_four = "iyhqz ewqin azqej shayz niqbe aheum hnmnj jaqii yuexq ayqkn jbeuq iihed yzhni ifnun sayiz yudhe sqshu qesqa iluym qkque aqaqm oejjs hqzyu jdzqa diesh niznj jayzy uiqhq vayzq shsnj jejjz nshna hnmyt isnae sqfun dqzew qiead zevqi zhnjq shqze udqai jrmtq uishq ifnun siiqa suoij qqfni syyle iszhn bhmei squih nimnx hsead shqmr udquq uaqeu iisqe jshnj oihyy snaxs hqihe lsilu ymhni tyz"
    
    phrase = phrase_one
    print("Encrypted phrase:", phrase)
    phrase = phrase.replace(' ', '') # get rid of spaces
    most_common_letter = collections.Counter(phrase).most_common(1)[0] # find the most common letter

    #print("most common letter:", most_common_letter[0])
    #print("integer associated with", most_common_letter[0], ":", letter_values[most_common_letter[0]])

    vowels = set("aeiouAEIOU")
    x = Counter(c for c in phrase_one if c in vowels)
    #print("most common vowel:", x.most_common()[0])

    # assume that the most frequent letter is the encrypted letter for 'e'
    shift = letter_values[most_common_letter[0]] - letter_values['a']
        # 1) most common letter: j; 'a'
            # most common vowel: 
        # 2) most common letter: o, 't'
        # 3) most common letter: t; 't' - not like the first two (sherlock)
        # 4) most commom letter: q; 'e'
    #print("shift:", shift)
    #print("\n")

    decrypted_phrase = ""
    for character in phrase:
        #print("character:", character)
        #print("character's number:", letter_values[character])

        #print("letter_values['e']:", letter_values['e'])
        #print("shift:", shift)
        decrypted_letter_value = (letter_values[character] - shift) % 26
        #print("decrypted letter value:", decrypted_letter_value)
        decrypted_letter = get_key(decrypted_letter_value, letter_values)

        #print("decrypted letter:", decrypted_letter)
        decrypted_phrase += decrypted_letter
        #print("\n")

    decrypted_phrase = ' '.join(decrypted_phrase[i:i+5] for i in range(0, len(decrypted_phrase), 5)) # re-adding spaces


    print("Decrypted phrase:", decrypted_phrase)

main()