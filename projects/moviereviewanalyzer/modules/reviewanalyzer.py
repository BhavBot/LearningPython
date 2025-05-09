import math
from modules.stringutils import replacewords
# from modules.ioutils import readpluralreview


def keyfunc(object):
    return object["rating"]
    

def computestats(reviews):
    reviews=sorted(reviews, key=keyfunc, reverse=True)
    ratings= [review["rating"] for review in reviews]
    avg= sum(ratings)/len(ratings)
    maxx=max(ratings)
    minn= min(ratings)
    print(avg)
    print(maxx)
    print(minn)
    return len(reviews), avg, reviews[0]

    
    
    
    
def gensum(reviews):
    summ=[]
    for review in reviews:
        censsum=replacewords(f"{review["movie_title"]}-{review["rating"]}/5: {review["review"]}\n-{review["reviewer"]}\n\n", r'\bhttps?://[^\s]+|\bwww\.[^\s]+', "XXXXXXXXXXXXXXXXXX")
        censsum=replacewords(censsum, r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b', "000000000000")
        censsum=replacewords(censsum, r'\b(?:\+1[-.\s]?|1[-.\s]?)?(?:\(?\d{3}\)?[-.\s]?)\d{3}[-.\s]?\d{4}\b', "[redacted]")     
        summ.append(censsum)
    # print(len(summ))
    # print(type(summ))
    return summ
    
    
if __name__=="__main__":
    print("Yharon the Jungle Dragon")
    
    