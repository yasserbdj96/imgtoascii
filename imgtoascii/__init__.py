#!/usr/bin/env python
# coding:utf-8
"""
#set:usage,examples,changelog
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
"""
# VALUES :
#s
__version__="0.0.1"
__name__="imgtoascii"
__author__="Yasser BDJ (Ro0t96)"
__author_email__="by.root96@gmail.com"
__github_user_name__="byRo0t96"
__title__="image to ascii."
__description__="Convert images to ascii."
__author_website__="https://byro0t96.github.io/"
__source_code__=f"https://github.com/{__github_user_name__}/{__name__}"
__keywords__=['python','image','ascii']
__install_requires__=['pipincluder']
__Installation__="pip install "+__name__+"=="+__version__
__license__='Apache Software License'
__license_text__=f'''Copyright (c) 2008->Present, {__author__}
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.'''
__copyright__='Copyright 2008 -> Present, '+__author__

__changelog__='## 0.0.1\n- First public release.\n'
##################################################################
#e

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