from CLCC.RL.storage import Storage
from runInRemote import catStorage, runInRemote

localPath = f'/home/yinwenpei/RTCPython/localFiles/'
storage = Storage()
storage = catStorage(localPath,storage)
print(storage)