import urllib.request
import urllib.parse
import re
import random

def search(tags):
    tagsAdd = ''
    for i in range(0, len(tags)):
        tagsAdd += tags[i] + "+"
    url = "https://www.youtube.com/results?search_query="+tagsAdd

    headers = {}
    headers[
        'User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecho) Chrome/24.0.1312.27 Safari/537.17'
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    pageInfo = re.findall(r'<a(.*?)/a>', str(respData))

    #print(pageInfo)

    videoData = []

    # Saves the urls in images list
    for body in pageInfo:
        if ('/watch?' in body):

            start = body.find("href")
            end = body.find("yt-ui",start)

            body = body[start+6:end-9]

            videoData.append('https://www.youtube.com'+body)

    return videoData[random.randint(0, len(videoData))]