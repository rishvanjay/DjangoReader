# import urllib2
# import json

# url = "https://docs.python.org/2/library/urllib2.html"


# # add a header to define a custon User-Agent
# headers = { 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36' }

# req = urllib2.Request(url, '', headers)
# try:
#     response = urllib2.urlopen(req).read()
# except urllib2.HTTPError as e:
#     # print "error"
#     response = ""

#     ContentJson = json.dumps({
#         'url':url, 
#         'errorNo':e.getcode(),
#         'errorMessage':e.reason,
#         'data': response
#     })

#     print ContentJson
# # print response

# else: 
#     ContentJson = json.dumps({
#         'url':url, 
#         'data':response,
#     })

#     print ContentJson


import urllib.request, urllib.error, urllib.parse
import json

# url = "https://www.google.co.in/"

def readMethod(url):
    # add a header to define a custon User-Agent
    HEADERS = { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' }
    contentJson = "a"

    req = urllib.request.Request(url, headers=HEADERS)
    try:
        response = urllib.request.urlopen(req).read()
    except urllib.error.HTTPError as e:
        # print("error")
        response = ""

        ContentJson = json.dumps({
            'url':url, 
            'errorNo':e.getcode(),
            'errorMessage':e.reason,
        })

        # print(ContentJson)
    # print response
    else: 
        ContentJson = json.dumps({
            'url':url, 
            'data':response.decode('utf-8'),
        })

        # print(ContentJson)

    return ContentJson

