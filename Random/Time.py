import datetime
import time
import uuid


ts = time.time()
stamp = datetime.datetime.fromtimestamp(ts).strftime('%Y.%m.%d-%H.%M.%S')

value = uuid.uuid4()
#print(stamp)
print 'Upload_%s_%1.5s' %(stamp, value)
