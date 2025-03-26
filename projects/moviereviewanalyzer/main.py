from modules.ioutils import readpluralreview, wrtsum
from modules.reviewanalyzer import computestats, gensum
from modules.stringutils import srchrevs, replacewords

reviews="KGF 2"
minrating="terrarrariarararaira"
maxreviews="i"
keywords={"good":"great"}
def main():
    print("Movie Review Analyzer")
    
    # readpluralreview()
    # wrtsum()
    # computestats(reviews)
    # gensum(reviews,minrating,maxreviews)
    # srchrevs(reviews,keywords)
    # replacewords()
    
    while True:
        print("1. Generate Summary Report")
        print("2. Search for Keywords in Reviews")
        print("3. Replace Words in Reviews")
        print("4. Compute Statistics")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            summary = gensum(reviews)
            wrtsum(summary)
            print("Summary generated and saved!")

        elif choice == "2":
            keyword = input("Enter keyword to search: ")
            results = srchrevs(reviews, keyword)
            print(f"Found {len(results)} reviews containing '{keyword}':")
            for r in results:
                print(f"{r['movie_title']} - {r['review']}")

        elif choice == "3":
            word_to_replace = input("Enter word to replace: ")
            replacement_word = input("Enter replacement word: ")
            for r in reviews:
                r['review'] = replacewords(r['review'], {word_to_replace: replacement_word})
            print("Word replacements completed.")

        elif choice == "4":
            total_reviews, avg_rating, best_movie = computestats(reviews)
            print(f"Total Reviews: {total_reviews}")
            print(f"Average Rating: {avg_rating:.1f}")
            print(f"Best Movie: {best_movie[0]} ({best_movie[1]}/5)")

        elif choice == "5":
            print("Terraria")
            break

        else:
            print("Invalid choice. Try again."  )
        




if __name__=="__main__":
    print("Supreme Calamitas")
    main()