with open("secret.txt", "r", encoding="utf-8") as filein:
    lines = filein.read()
    

convertion = [(ord(code) if ord(code) < 128 else ord(code) % 256) for code in lines]
conv_text = "".join(chr(code) for code in convertion)

print(conv_text)