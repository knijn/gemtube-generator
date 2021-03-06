import os
import sys
import json
def findUser(targetUser):
    userIndexFileHandle = open("/home/debian/gemtube-generator/userindex.json","r")
    userIndexFile = userIndexFileHandle.read()
    userIndexFileHandle.close()
    #print(userIndexFile)
    userIndexJSON = json.loads(userIndexFile)
    for o in userIndexJSON["users"]:
        #print(o)
        if o["username"] == targetUser:
            return o

def printHeader():
    #print("% gem_header 20 'text/gemini; charset=utf-8; lang=en'")
    print("=> / ↩ Home")
    print("=> ./ ⬆ Up")
if sys.argv[1] == "page":
    user = findUser(sys.argv[2])
    #print(user["uri"])
    command = 'gemget ' + user["uri"] + " -o- -q"
    stream = os.popen(command)
    indexFile = stream.read()
    indexJSON = json.loads(indexFile)
    printHeader()
    print("# Gemtube user: " + indexJSON["user"])
    for o in indexJSON["videos"]:
        print("## " + o["title"])
        print(o["description"])
        print("> Downloads:")
        for qo in o["downloads"]:
            print("=> " + qo["uri"] + " " + qo["quality"] + " (" + qo["filesize"] + ")")
    
if sys.argv[1] == "list":
    printHeader()
    print("# List of users on gemtube")
    userIndexFileHandle = open("/home/debian/gemtube-generator/userindex.json","r")
    userIndexFile = userIndexFileHandle.read()
    userIndexFileHandle.close()
    #print(userIndexFile)
    userIndexJSON = json.loads(userIndexFile)
    for o in userIndexJSON["users"]:
        print("=> gemini://knijn.ga/videos/gemtube/page/" + o["username"] + ".bliz " + o["username"] )