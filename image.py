# coding=utf-8
from PIL import Image

import shutil  
import os  

def resize(file, width=None, height=None):
	if width==None and height==None:
		return False
	image = Image.open(file);
	(x, y) = image.size
	if width!=None and height==None:
		height = int(float(width)/x*y)
	if width==None and height!=None:
		width = int(float(height)/y*x)

	out = image.resize((width, height), Image.ANTIALIAS)
	out.save(file);
	return True

if __name__ == '__main__':

	i = './images/58/' # 输入目录

	list = os.listdir(i)
	for item in list:
		file = "%s%s" % (i, item)
		resize(file, 800)
		print file