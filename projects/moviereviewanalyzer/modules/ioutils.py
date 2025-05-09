import os
import json




def readpluralreview(reviewspath):
    with open(reviewspath, "r", encoding="utf-8") as file:
        reviews=json.load(file)
        return reviews
    
def wrtsum(summary):
    with open("moviereviewanalyzer/data/summary.txt","w",encoding="utf-8") as file:
        file.writelines(summary)
        file.close
    
        

if __name__=="__main__":
    print("Slime God")
    