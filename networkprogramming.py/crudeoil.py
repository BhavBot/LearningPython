import requests
# result=requests.get("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
# print(result.text)

result=requests.get("https://q8qmdclj-5001.use.devtunnels.ms/")
if result.status_code==200:
    print(result.text)
    with open("samplefile.html","w") as falie:
        falie.write(result.text)
else:
    print("fail")