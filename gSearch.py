import urllib.request
import urllib.parse
import re
import random

def search(tags):
    tagsAdd = ''
    for i in range(0, len(tags)):
        tagsAdd += tags[i]
    tagsAdd = tagsAdd.replace(" ","+")
    url = "https://www.google.co.in/search?q="+tagsAdd+"&source=lnms&tbm=isch"
    print(url)

    headers = {}
    headers[
        'User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecho) Chrome/24.0.1312.27 Safari/537.17'
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    pageInfo = re.findall(r'<a(.*?)/a>', str(respData))

    #print(pageInfo)

    imageData = []

    #Saves the urls in images list
    for body in pageInfo:
        if('ou' in body and len(body) < 500):
            imageData.append(body)

    imageData = imageData[15:]
    print(imageData)

    #List of image links
    images = []

    #Reformats the data to only image links
    for imageLink in  imageData:
        if('data-src' in imageLink):
            print(imageLink)
            start = imageLink.find('data-src')
            end = imageLink.find('jsaction',start)

            images.append(imageLink[start+10:end-2])

    print(images)

    return images[random.randint(0,len(images))]
