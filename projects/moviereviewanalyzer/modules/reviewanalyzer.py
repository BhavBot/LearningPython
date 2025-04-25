import math
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
         summ.append(f"{review["movie_title"]}-{review["rating"]}/5: {review["review"]}\n-{review["reviewer"]}\n\n")
    print(len(summ))
    print(type(summ))
    return summ
    
    
if __name__=="__main__":
    print("Yharon the Jungle Dragon")
    
    