MORSE_TO_ALPHA = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",
}
morse_code_words = input().split('|')

new_word = ''

for word in morse_code_words:
    split_by_space = word.split(' ')
    for letter in split_by_space:
        if letter in MORSE_TO_ALPHA:
            new_word += MORSE_TO_ALPHA[letter]
    new_word += ' '

print(new_word)