from PIL import Image
from PIL import ImageChops
from PIL import ImageStat
from stat import S_ISREG, ST_CTIME, ST_MODE
import os, sys, time


precision = 5
dir_path = r'C:\\python-youtube\\photos'



print("Reading folder...")
data = (os.path.join(dir_path, fn) for fn in os.listdir(dir_path))
data = ((os.stat(path), path) for path in data)
data = ((stat[ST_CTIME], path)
           for stat, path in data if S_ISREG(stat[ST_MODE]))

im1 = ""
i = 0
print("Processing images...")
for cdate, filename in sorted(data):
    if filename.endswith(".jpg") or filename.endswith(".png"):
    	if not im1 and i==0:
    		im1 = Image.open(os.path.join(dir_path, filename))
    		im1name = os.path.join(dir_path, filename)
    	else:
    		im2 = Image.open(os.path.join(dir_path, filename))
    		im2name = os.path.join(dir_path, filename)
    		print("Analyzing ", im2name)
    		diff = ImageChops.difference(im2, im1)
    		stat = ImageStat.Stat(diff)
    		diff_ratio = sum(stat.mean) / (len(stat.mean) * 255)
    		if (diff_ratio * 100 )>precision:
    			print("Un changement a été détecté : ", diff_ratio * 100)
    			print(im1name)
    			print(im2name)
    			# definition de la difference
    			im5 = ImageChops.subtract(im1, im2, scale=1.0, offset=0)
    			os.startfile(im1name)
    			os.startfile(im2name)
    			time.sleep(1) # wait for creation
    			im5.show()
    		im1 = im2
    		im1name = im2name
    else:
        continue
