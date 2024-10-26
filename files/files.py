import os

current_dir = os.path.dirname(__file__)  # Get the directory of the current script
os.chdir(current_dir)

with open("./data/sampleinput.txt") as file:
    content=file.read()
print(content)
with open("./data/sampleoutput.txt","w",encoding='utf-8') as file:
    file.write("""HELOLO WHATS A9HUN UP
I AM ME AND YOU ARE YOIU
BUT WE ARE WE
WKONDN9FWXKCWIEFCIONZ""")
    

