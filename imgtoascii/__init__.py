#!/usr/bin/env python
# coding:utf-8
# Code by : Yasser BDJ
# E-mail  : yasser.bdj96@gmail.com
"""
#set:usage.py,examples.py,changelog.txt
##################################################################
# USAGE :
#s
from imgtoascii import imgtoascii

imgtoascii("<IMAGE_PATH>","<OPTION>").view()
#e
##################################################################
# EXAMPLES :
#s
from imgtoascii import imgtoascii

# Example:1
imgtoascii("test.png").view()

# Example:2
p1=imgtoascii("test.png",False).view()

for i in range(len(p1)):
    print(p1[i])
#e
##################################################################
# CHANGELOG :
#s
## 0.0.2
- Fix Bugs.

## 0.0.1
- First public release.
#e
##################################################################
"""
# VALUES :
__version__="0.0.2"
__name__="imgtoascii"
__author__="Yasser Bdj (Boudjada Yasser)"
__author_email__="yasser.bdj96@gmail.com"
__github_user_name__="yasserbdj96"
__title__="image to ascii."
__description__="Convert images to ascii."
__author_website__=f"https://{__github_user_name__}.github.io/"
__source_code__=f"https://github.com/{__github_user_name__}/{__name__}"
__keywords__=[__github_user_name__,'python']
__keywords__.extend(__title__.split(" "))
__keywords__.extend(__description__.split(" "))
__install_requires__=['pipincluder']
__Installation__="pip install "+__name__+"=="+__version__
__license__='MIT License'
__copyright__='Copyright © 2008->Present, '+__author__+"."
__license_text__=f'''MIT License

{__copyright__}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

You also agree that if you become very rich you will give me 1% of your wealth.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''
##################################################################
#s
from pipincluder import pipincluder

#import pakages by pipincluder:
exec(pipincluder("from PIL import Image",
                 "from hexor import hexor").modules())

#start imgtoascii class:
class imgtoascii:
    #__init__:
    def __init__(self,img,oki=True):
        self.oki=oki
        art="██"
        im=Image.open(img)
        width,height=im.size
        pixels=list(im.getdata())
        allpi=[]
        linepi=[]
        k=1
        p1=hexor(True,"rgb")
        for i in range(len(pixels)):
            if k<width:
                linepi.append(p1.c(art,f"{pixels[i][0]},{pixels[i][1]},{pixels[i][2]}",f"{pixels[i][0]},{pixels[i][1]},{pixels[i][2]}"))
            elif k==width:
                allpi.append(linepi)
                linepi=[]
                k=0
            k+=1
        self.allpi=allpi

    #view:
    def view(self):
        allart=self.allpi
        image_art=[]
        for i in range(len(allart)):
            line=""
            for j in range(len(allart[i])):
                line=line+allart[i][j]
            image_art.append(line)
        if self.oki==True:
            for i in range(len(image_art)):
                print(image_art[i])
        else:
            return image_art
#e