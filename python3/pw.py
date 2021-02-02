plain_text="Kyonggi University Turtle Project Pype Team"

encrypted_text=""
for c in plain_text:
    x=ord(c)
    x=x+1
    cc=chr(x)
    encrypted_text=encrypted_text+cc
print(encrypted_text)
