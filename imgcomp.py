from PIL import Image
import requests
from io import BytesIO
import imagehash
img1url=input("FIRST IMAGE URL > ")
img2url=input("SECONDIMAGE URL > ")

dcord1 = requests.get(img1url)
img1 = Image.open(BytesIO(dcord1.content))
hash = imagehash.average_hash(img1)
                                                                                                                                     
dcord2= requests.get(img2url)
img2 = Image.open(BytesIO(dcord2.content))
otherhash = imagehash.average_hash(img2)
print(hash-otherhash)
        