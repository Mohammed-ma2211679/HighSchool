try:
    import time

    def cipher(txt, key):
        cipher_txt = []
        for l in txt:
            po = ord(l)
            new = chr(po + key)
            cipher_txt.append(new)
            # print(cipher_txt)
        for j in cipher_txt:
            print(j, end='')
        input('\nPress Enter to end...')


    def b_cipher(ci):
        print('All keys: ')
        for n in range(1100000):
            broken_cipher = []
            for c in ci:
                po = ord(c)
                old = chr((po - n) % 1100000)
                broken_cipher.append(old)
            for j in broken_cipher:
                print(j, end='')
            print(', The number of the key is:', n)
            time.sleep(0.5)
        input('\nPress Enter to end...')
    # main program:
    print('Instructions: ')
    print('Enter 1 for turn text to caesar cipher')
    print('Enter 2 for turn caesar cipher to text')
    print('---------------------------------------')
    t = True
    while t is True:
        i = int(input('Enter 1 or 2: '))
        if i == 1:
            t = list(input('Enter the Text: '))
            k = int(input('Enter the key between 0 - 1100000: '))
            cipher(t, k)
            break
        elif i == 2:
            t = list(input('Enter the caesar cipher: '))
            b_cipher(t)
            break
        elif i is float:
            print('!!! You enter a Letter, Try again with 1 or 2!!!')
        else:
            print('!!! You enter a wrong number, Try again !!!')
except Exception as e:
    print('Error:', e)
except OverflowError:
    print('You have exceeded the limit, Try again')
finally:
    print('')
    print('Thank you for using my program <3')
