import os

current_dir = os.path.dirname(__file__)  # Get the directory of the current script
os.chdir(current_dir)

with open("./data/sampleoutput.txt","a",encoding='utf-8') as file:
    file.write("""hmmmm yes
this is interesting""")
    file.write("""THIS IS THE NEW AGE
ICE AGE
""")