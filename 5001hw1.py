#!/bin/python3
import re
import xml.dom.minidom as xmldom
dom=xmldom.parse('./blocklist.xml')
root = dom.documentElement
def printbockID(Tagname):
    num = 0
    re_blockID = re.compile(r'^(i|g)\d*$')
    itemlist = root.getElementsByTagName(Tagname)
    for i in range(len(itemlist)):
        item = itemlist[i]
        id=item.getAttribute("blockID")
        if re.match(re_blockID, id) :
            print(item.toxml().split('\n')[0])
            num +=1
    return num
def printemail(Tagname):
    num_email = 0
    re_email = re.compile(r'''(
                        [a-zA-Z0-9._%+-]+
                        @
                        [a-zA-Z0-9.-]+
                        (\.[a-zA-Z])    
                        )''', re.VERBOSE)
    itemlist = root.getElementsByTagName(Tagname)
    for i in range(len(itemlist)):
        item = itemlist[i]
        email = item.getAttribute("id")
        if re.match(re_email, email):
            print(item.toxml().split('\n')[0])
            num_email +=1
    return num_email

aa=printbockID('emItem')+printbockID('pluginItem')+printbockID('gfxBlacklistEntry')
bb=printemail('emItem')+printemail('pluginItem')+printemail('gfxBlacklistEntry')

print('the whole num of lines in Question a is %d'%aa)
print('the whole num of lines in Question b is %d'%bb)
