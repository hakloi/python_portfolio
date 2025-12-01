shift = int(input())

with open("public.txt", "r", encoding="utf-8") as file:
    message = file.read()

new_message = []

for ch in message:
    if ch.islower():
        new_ch = chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
        new_message.append(new_ch) 
    elif ch.isupper():
        new_ch = chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
        new_message.append(new_ch) 
    else: 
        new_message.append(ch)
    
with open("private.txt", "w", encoding="utf-8") as fileout:
    fileout.write("".join(str(ch) for ch in new_message))
        
    
    
        
    
    # if ch.isupper: