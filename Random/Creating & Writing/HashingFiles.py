import hashlib

hasher = hashlib.md5()
with open('chapter.mp3', 'rb') as theFile:
    aFile = theFile.read()
    hasher.update(aFile)
#     a8d6ef977090e0af9ce0dadba1bdab2e

hashmeister = hashlib.md5()
with open('zipped_file.zip', 'rb') as theFile:
    aFile = theFile.read()
    hashmeister.update(aFile)
    print hashmeister.hexdigest()
#     0a6d97a9c8bc3803cb4352c6e827ae7d NOT gb
#     fc6c9b0197db2c076befa63f201c0b46 gb
## Interesting...

if hasher.hexdigest() != hashmeister.hexdigest():
    print "NOT The same file"