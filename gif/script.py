try:
    from PIL import Image
except ImportError:
    import Image

import numpy as np

def load_image( infilename ) :
    img = Image.open( infilename )
    img.load()
    data = np.asarray( img, dtype="int32" )
    return data

def save_image( npdata, outfilename ) :
    img = Image.fromarray( np.asarray( np.clip(npdata,0,255), dtype="uint8"), "L" )
    img.save( outfilename )
    
arr=load_image("orig.jpg")
arr[arr < 250] = 0
arr=np.roll(arr,-5,0)
save_image(arr, "0.jpg")
x=0
for i in range(2,129):
    arr=np.roll(arr,1)
    j=str(i)
    x+=1
    if(x%8<=3):
        arr=np.roll(arr,2,0)
    else:
        arr=np.roll(arr,-2,0)
    save_image(arr, j+".jpg")