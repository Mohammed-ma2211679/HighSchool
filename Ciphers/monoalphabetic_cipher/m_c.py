try:
    D_C = {
        'A': 'q', 'B': 'w', 'C': 'e', 'D': 'r', 'E': 't', 'F': 'y', 'G': 'u',
        'H': 'i', 'I': 'o', 'J': 'p', 'K': 'a', 'L': 's', 'M': 'd', 'N': 'f',
        'O': 'g', 'P': 'h', 'Q': 'j', 'R': 'k', 'S': 'l', 'T': 'z', 'U': 'x',
        'V': 'c', 'W': 'v', 'X': 'b', 'Y': 'n', 'Z': 'm', ' ': ' '
    }
    D_C_R = {value: key for (key, value) in D_C.items()}

    # function that turn text to monoalphabetic cipher
    def e(txt):
        print('The cipher is: ', end='')
        for l in txt:
            print(D_C.get(l), end='')

    # function that turn monoalphabetic cipher to text
    def b_e(cipher):
        print('The text is: ', end='')
        for l in cipher:
            print(D_C_R.get(l), end='')

    # main program
    print('Instructions: ')
    print('Enter 1 to turn text to monoalphabetic cipher')
    print('Enter 2 to turn monoalphabetic cipher to text')
    print('-----------------------------------------------')
    while True:
        n = int(input('Enter 1 or 2: '))
        if n == 1:
            t = str.upper(input('Enter the text: '))
            e(t)
            break
        elif n == 2:
            c = str.lower(input('Enter the monoalphabetic cipher: '))
            b_e(c)
            break
        else:
            print('You Enter a wrong number,Try again')

except ValueError:
    print('Do not enter a letter')

except Exception as e:
    print('Unexpected error:', e)

finally:
    print('')
    print('Thank you for using my program <3')
