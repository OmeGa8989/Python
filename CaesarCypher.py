alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

from art import logo
print (logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number between 0 and 26:\n"))


# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def caesar(text, shift,direction):
    # for encyrption
    if direction == 'encode':
        word2 = ''
        for letter in text:
         if letter in alphabet:
             t2 = alphabet.index(letter)
             if t2 - len(alphabet) <= shift:
                t2 = shift - (len(alphabet) - t2)
                word2 += alphabet[t2]
             else:
                word2 += alphabet[t2 - shift]
         else:
             word2 += letter

    else:
     #    for decryption
     word2 = ''
     for letter in text:
        if letter in alphabet:
          t2 = alphabet.index(letter)
          if t2 - shift < 0:
           t2 = (t2 - shift) + len(alphabet)
           word2 += alphabet[t2]
          else:
           word2 += alphabet[t2 - shift]
        else:
            word2 += letter

    print(word2)
    print ("Do you want to restart?")
    restart = input("Type 'yes' to restart, 'No' to end the game.\n").lower()
    if restart == 'yes':
        caesar(text,shift,direction)
    else:
        print ('THanks for playing!')
    ##HINT: How do you get the index of an item in a list:
    # https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
if (direction == 'encode' or direction == 'decode'):
    caesar(text, shift,direction)
