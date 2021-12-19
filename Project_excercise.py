# ทำรหัสลับ โดยการเลื่อนตำแหน่งของตัวอักษรในข้อความที่ได้รับมา

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import logo

# กำหนด function ในการเลื่อนตำแหน่งของตัวอักษรในข้อความที่ได้รับมา

def caesar(word, number, code):
    new_text = ""
    # กำหนด if ตรงนี้เพื่อประหยัด บรรทัดการเขียน แทนที่จะเขียน if 2 ครั้งก็ใช้หลักการคูณเลข -1 เข้าไปแทน
    if code == "decode":
        number *= -1
    # กำหนดให้ L วน loop ใน Text
    for L in word:
        # L ใน loop แต่ละรอบก็จะแทน  ตัวอักษรของ text แต่ละตัว
        # เมื่อ L แทนตัวอักษรแต่ละตัวแล้ว ก็ให้ไปตรวจสอบใน alphabet list 
        if L in alphabet:
            # ตรวจสอบว่า L เป็นข้อมูลตำแหน่งที่เท่าไรของ alphabet.list โดยให้ position_word = ตำแหน่งของ L ใน list
            position_word = alphabet.index(L)
            # กำหนด new_position_word ที่ต้องการจะเลื่อนตำแหน่งตัวอักษรของข้อความเดิมที่ใส่ลงไป
            new_position_word = position_word + number
            new_text += alphabet[new_position_word]
        else:
            # เนื่องจาก new_text = "" ซึ่งไม่มีข้อความอื่นเลย เพราะฉะนั้นแล้วในกรณี else ถ้า L ไม่ตรงกับข้อมูลอะไรเลยใน list ก็จะเป็นการเพิ่ม L เข้าไปใน
            # new_text แทนเพราะ เราไม่ได้แทนใน text ที่มีตัวอักษรอยู่แล้ว เลยไม่จำเป็นต้องใช้ == ในการแทนที่
            new_text += L
    # กำหนดให้หลังจบ loop ของ L ใน text แล้วให้ print ข้อมูลเหล่านี้     
    print(f"Here's the {code} result: {new_text}")
    
print(logo)

# กำหนดค่าให้กับ function while เพื่อให้วน loop จนกว่าหาที่กำหนดให้จะเป็น false
end_of_program = True
while end_of_program:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    # ใช้งาน function caesar โดยที่ไม่ต้องกด print("")
    caesar(word=text, number=shift, code=direction)
    continue_play = input("Try 'yes' if you want to go again. Otherwise type 'no'. ").lower()
    # ถ้าหากไม่ต้องการเล่นต่อแล้วให้เลือก "no" เพื่อจะทำให้เงื่อนไขของ while = false แล้วหยุดการวน loop 
    if continue_play == "no":
        end_of_program = False
        print("Goodbye")



