dictionnary_braille = {
    "a" : "O.....",
    "b" : "O.O...",
    "c" : "OO....",
    "d" : "OO.O..",
    "e" : "O..O..",
    "f" : "OOO...",
    "g" : "OOOO..",
    "h" : "O.OO..",
    "i" : ".OO...",
    "j" : ".OOO..",
    "k" : "O...O.",
    "l" : "O.O.O.",
    "m" : "OO..O.",
    "n" : "OO.OO.",
    "o" : "O..OO.",
    "p" : "OOO.O.",
    "q" : "OOOOO.",
    "r" : "O.OOO.",
    "s" : ".OO.O.",
    "t" : ".OOOO.",
    "u" : "O...OO",
    "v" : "O.O.OO",
    "w" : ".OOO.O",
    "x" : "OO..OO",
    "y" : "OO.OOO",
    "z" : "O..OOO",
    " " : "......",
    "A" : ".....O",
    "D" : ".O...O",
    "N" : ".O.OOO",
    "." : "..OO.O",
    "," : "..O...",
    "?" : "..O.OO",
    "!" : "..OOO.",
    ":" : "..OO..",
    ";" : "....OO",
    "-" : "....OO",
    "/" : ".O..O.",
    "<" : ".OO..O",
    ">" : "O..OO.",
    "(" : "O.O..O",
    ")" : ".O.OO.",
}

braille_number = {
    "1" : "O.....",
    "2" : "O.O...",
    "3" : "OO....",
    "4" : "OO.O..",
    "5" : "O..O..",
    "6" : "OOO...",
    "7" : "OOOO..",
    "8" : "O.OO..",
    "9" : ".OO...",
}

def convert_braille(sentence):
    new_text_converted = ""
    compteur = 0
    length_of_sentence = len(sentence)
    sub_srt_len = 6
    empty = ''
    destroy_char = []
    number_destory = dict()
    all_space = []
    for char in sentence:
        if char == 'O' or char == '.':
            compteur = compteur + 1
        if compteur > 6:
            break
    if compteur < 5:
        for char in sentence:
            word = dictionnary_braille[char] 
            new_text_converted += word
    else:
        for i in range(0, length_of_sentence, sub_srt_len):
            substring = sentence[i:i + sub_srt_len]
            letter = list(dictionnary_braille.keys())[list(dictionnary_braille.values()).index(substring)]
            if letter == "A":
                letter = list(dictionnary_braille.keys())[list(dictionnary_braille.values()).index(sentence[i+sub_srt_len:i + sub_srt_len*2])]
                letter = letter.upper()
                destroy_char.append(i/sub_srt_len+1)
            if letter == "N":
                letter = letter
                destroy_char.append(i/sub_srt_len)
                number_destory[i/sub_srt_len-1] = substring
            new_text_converted += letter
        for char in destroy_char[::-1]:
            char = int(char)
            new_text_converted = new_text_converted[:char] + empty + new_text_converted[char + 1:]
        for number in number_destory:
            number = int(number)
            print(number)
            letter = new_text_converted[number]
            braille_code = dictionnary_braille.get(letter)
            letter = list(braille_number.keys())[list(braille_number.values()).index(braille_code)]
            new_text_converted = new_text_converted[:number] + letter + new_text_converted[number+1:]
            print(letter)
        for check in all_space:
                print(check)
            #new_text_converted[:char] + str(letter) + new_text_converted[char + 1:]

    print(new_text_converted)

convert_braille(".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO")

#print(list(dictionnary_braille.keys())
    #[list(dictionnary_braille.values()).index("O.OO..")])

