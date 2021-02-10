#Caesar Cipher

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)

#
# def encrypt(plain_text, shift_amount):
#     encrypted_message = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         encrypted_message += str(alphabet[new_position])
#     print(encrypted_message)
#
# def decrypt(plain_text, shift_amount):
#     decrypted_message = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         decrypted_message += str(alphabet[new_position])
#     print(decrypted_message)

def ceasar(text, shift, direction):
    finall_text = ""
    if direction == "decode":
        shift *= -1
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift
            if new_position > len(alphabet) or new_position < 0:
                new_position %= 25
            finall_text += alphabet[new_position]
        else:
            finall_text += char
    print(f"Your {direction}d text is: {finall_text}")

reboot_prog = True

while reboot_prog:
    user_direction = input("Type \"encode\" to encrypt, type \"decode\" to decrypt your message\n").lower()
    user_text = input("Type your text: \n").lower()
    user_shift = int(input("Type the shift number: \n"))
    ceasar(text=user_text, shift=user_shift, direction=user_direction)
    end_quest = input("Do you wanna cipher more? Type \"yes\" or \"no\":\n")
    if end_quest == "no":
        reboot_prog = False
        print("Goodbye!")