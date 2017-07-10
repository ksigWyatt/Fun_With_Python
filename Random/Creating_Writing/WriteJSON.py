import urllib2
import json
import io

# which URL should we cache?
url = 'http://td.unfoldingword.org/exports/langnames.json'
response = urllib2.urlopen(url)

#obtain jsonfile from webscraping
webFile = json.loads(response.read())

# create a new JSON file called 'languages'
#jsonFile = open("languages.json", "w")
# write all the web content that was read from it to the file
#jsonFile.write(webFile)
#close the file writer
#jsonFile.close()

# with io.open('languages.json', 'w', encoding='utf-8') as outfile:
#    outfile.write(json.dump(webFile, ensure_ascii=False))
# language = ""
# #find language
# languages = open('languages.json', 'r')

print "Opening"

with open("languages.json") as jsonFile:
    jsonData = json.load(jsonFile)
    for values in jsonData:
        if values["lc"] == "aag":

            print "FOUND"
            print values["ln"]

print "did it work?"

# for dicti in languages:
#     print dicti
#    if dicti["lc"] == "aag":
#        print "lc = aag"
#        #print(dicti["lc"])
#        language = dicti["ln""]
#        break