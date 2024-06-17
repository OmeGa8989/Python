alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.



def encrypt(text,shift):
    word2=''
    for letter in text:
     t2 = alphabet.index(letter)
     if t2-len(alphabet) <= shift:
        t2 = shift-(len(alphabet)-t2)
        word2 += alphabet[t2]
     else:
         word2 += alphabet[t2-shift]
    print(word2)

def decrypt(text,shift):
        word2=''
        for letter in text:
         t2 = alphabet.index(letter)
         if t2 -shift < 0 :
            t2 = (t2-shift)+len(alphabet)
            word2 += alphabet[t2]
         else:
            word2 += alphabet[t2 -shift]
        print(word2)




    # TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    # e.g.
    # plain_text = "hello"
    # shift = 5
    # cipher_text = "mjqqt"
    # print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    # https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛


# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
if (direction == 'encode' or direction == 'decode'):
    caesar(text, shift)
