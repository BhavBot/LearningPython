import os

current_dir = os.path.dirname(__file__)  # Get the directory of the current script
os.chdir(current_dir)

with open("./data/sampleoutput.txt",encoding='utf-8') as file:
    for line in file:
        print("line: ",line.strip())