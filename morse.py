trns = {'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.',
'F':'..-.','G':'--.','H':'....','I':'..','J':'.---',
'K':'-.-','L':'.-..','M':'--','N':'-.','O':'---',
'P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-',
'U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--',
'Z':'--..', ' ':'.....'}

def to_text(morse):
    translation = ''

    d_encrypt = dict([(v, k) for k, v in trns.items()])
    morse = morse.split(' ')

    for x in morse:
        translation += d_encrypt.get(x)
    return translation

def to_morse(text):
    translation = ''

    txt = text.upper()
    for x in text:
        translation += trns.get(x) + ' '
    return translation

putin = input("Input the text you want to encrypy/ decrypt (if text, keep it in letters and spaces; other characters will be supported in later versions): ")
which_one = input("to morse or to text (indicate in lowercase as it was asked please): ")
if which_one == "morse" :
    print(to_morse(putin))
elif which_one == "text" :
    print(to_text(putin))