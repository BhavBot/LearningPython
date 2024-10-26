import os

current_dir = os.path.dirname(__file__)  # Get the directory of the current script
os.chdir(current_dir)

with open("./data/sampleoutput.txt","+r",encoding='utf-8') as file: #magic time
    file.seek(13,0)   #if second parameter is 0 it relates to the begining of the file 
                      #if 1 it is related to the current position
                      #if 2 it is related to the end of file
    cnt=file.read(10)
    print(cnt)
    file.seek(13,0) 
    file.write("bhavesh is me")