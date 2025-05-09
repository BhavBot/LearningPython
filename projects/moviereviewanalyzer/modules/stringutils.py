from modules.ioutils import readpluralreview
import re




def srchrevs(reviews,keyword):
    results=[]
    for review in reviews:
        result=re.findall(keyword,review["review"],re.IGNORECASE)
        if len(result)>=1:
            results.append(review)
    return results

def replacewords(reviewtext, wordtobereplaced, replacement):
    return re.sub(wordtobereplaced, replacement, reviewtext)
        
    
if __name__=="__main__":
    print("Perforators")
    