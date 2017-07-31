encode = {'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.',

        "." : ".-.-.-",  "," : "--..--",  ":" : "---...",
        "?" : "..--..",  "'" : ".----.",  "-" : "-....-",
        "/" : "-..-.",  "@" : ".--.-.",  "=" : "-...-"
        }


decode = {value:key for key,value in encode.items()}

def encoder(message):
    try:
        return ' '.join(encode.get(letter.upper()) for letter in message)
    except TypeError:
        return "[Error]: Unsupported characters"

def decoder(code):
    try:
        return ''.join(decode.get(sequence) for sequence in code.split())
    except TypeError:
        return "[Error]: No space between characters / Unsupported characters"
