import os
import time
import sys
import urllib.request
from socket import timeout
from urllib.error import HTTPError
from bs4 import BeautifulSoup,Tag,NavigableString,Comment
import shutil
import re
import io

fileName = "cmake-env-variables.7.html"
remotePath = "https://cmake.org/cmake/help/latest/manual/cmake-env-variables.7.html"

urlMain = "https://cmake.org/cmake/help/latest/manual/"


currentPath = ""
mainMdFileName = "cmake-env-variables.7.md"
mainMdFilePath = ""
mainMDFileDir = "manual"

tempDir = "temp"


allsubUrl = []


def download(url,filePath):
    try:
        # headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        headers = {'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
        urlStream = urllib.request.urlopen(url,timeout=100)
        data = urlStream.read()
        with open(filePath,'wb') as f:
            f.write(data)
    except timeout:
        print('socket timed out - URL %s', url)
    except:
        print("download from %s save to %s error" % (url,filePath))

def writeFile(content,filePath):
    opened_file = open(filePath, 'a')
    opened_file.write("%s\n" % content)
    opened_file.close()

def parseContent(section,prefix):
    for tag in list(section.children):
        if type(tag) is Tag:
            name = tag.name
            newprefix = prefix
            if name in "h1":
                newprefix = "# "
            elif name in "h2":
                newprefix = "## "
            elif name in "ul":
                newprefix = "   %s" % newprefix
            if tag.has_attr("class"):
                # 特殊字符不解释
                if ("headerlink" in tag["class"]):
                    continue
            global mainMdFilePath
            if name in "a":
                
                global allsubUrl
                text = tag.get_text()
                herf = tag["href"]
                oldherf = (herf + '.')[:-1]
                herf = herf.replace(".html",".md")
                herf = herf.replace("#","")
                text = text.replace("<","```<")
                text = text.replace(">",">```")
                if ("   " in prefix):
                    if (".." in herf):
                        writeFile("%s- [%s](%s)" % (prefix,text,herf),mainMdFilePath)
                        allsubUrl.append([herf,oldherf])
                    else:
                        writeFile("%s- [%s](#%s)" % (prefix,text,herf),mainMdFilePath)
                elif ("## " in prefix):
                    writeFile("%s<h2 id = \"%s\">%s</h2>" % (prefix,herf,text),mainMdFilePath)
                elif ("# " in prefix):
                    writeFile("%s<h1 id = \"%s\">%s</h1>" % (prefix,herf,text),mainMdFilePath)  
            elif name in "p":
                text = tag.get_text()
                text = text.replace("<","```<")
                text = text.replace(">",">```")
                writeFile("%s\n" % (text),mainMdFilePath)
            else:
                parseContent(tag,newprefix)
    

def parseMain(filePath):
    content = ''
    with open(filePath,'rb') as fstream:
        content = fstream.read().decode('utf-8')
    soup = BeautifulSoup(content,'html.parser')
    body = soup.find('body')
    section = body.find("div",class_="section")
    parseContent(section,"")

def has_class_name_headerlink(tag):
    return tag.has_attr('class') and "headerlink" in tag["class"] 

def parseSub(readFilePath,writeFilePath):
    content = ''
    with open(readFilePath,'rb') as fstream:
        content = fstream.read().decode('utf-8')
    soup = BeautifulSoup(content,'html.parser')
    body = soup.find('body')
    section = body.find("div",class_="section")
    for tag in list(section.children):
        if type(tag) is Tag:
            name = tag.name
            prefix = ""
            if name in "h1":
                prefix = "# "
            elif name in "h2":
                prefix = "## "
            for tag2 in tag.find_all(has_class_name_headerlink):
                tag2.string.replace_with('')
            text = tag.get_text()
            text = text.replace("<","```<")
            text = text.replace(">",">```")
            text = text.replace(u'\xa0', u'')
            
            if ("## " in prefix):
                writeFile("%s%s  " % (prefix,text),writeFilePath)
            elif ("# " in prefix):
                writeFile("%s%s  " % (prefix,text),writeFilePath)  
            else:
                writeFile("%s  \n" % text,writeFilePath)


def parseSubUrl(mdFileName,oneUrl):
    print(mdFileName,oneUrl)
    global tempDir
    global urlMain
    global mainMDFileDir
    splits = oneUrl.split('/')
    fileName = splits[len(splits) - 1]
    downFileName = "%s" % fileName
    downFilePath = os.path.join(tempDir,downFileName)
    if not os.path.exists(downFilePath):
        download("%s%s" % (urlMain,oneUrl),downFilePath)
        print("down %s success form %s%s" % (downFilePath,urlMain,oneUrl))
        try:
            time.sleep(0.1)
        except KeyboardInterrupt:
            print('\n\nKeyboard exception received. Exiting.')
            exit()
    else:
        print("already down %s form %s%s" % (downFilePath,urlMain,oneUrl))

    mdFilePath = "%s/%s" % (mainMDFileDir,mdFileName)
    if os.path.exists(mdFilePath):
        os.remove(mdFilePath)
        print("移除文件")
    else:
        mdFileDir = os.path.dirname(mdFilePath)
        if not os.path.exists(mdFileDir):
            print("创建目录")
            os.makedirs(mdFileDir)
    print(downFilePath,mdFilePath)
    parseSub(downFilePath,mdFilePath)
    


if __name__ == '__main__':
    currentPath = sys.path[0]
    os.chdir(currentPath)
    # create temp dir
    tempDir = os.path.join(currentPath,tempDir)
    if not os.path.exists(tempDir):
        os.makedirs(tempDir)

    filePath = os.path.join(tempDir,fileName)
    if not os.path.exists(filePath):
        download(remotePath,filePath)

    mainMDFileDir = os.path.join(currentPath,"../%s" % mainMDFileDir)
    print(mainMDFileDir)
    if not os.path.exists(mainMDFileDir):
        os.makedirs(mainMDFileDir)
    mainMdFilePath = os.path.join(mainMDFileDir,mainMdFileName)
    if os.path.exists(mainMdFilePath):
        os.remove(mainMdFilePath)
    parseMain(filePath)
    for one in allsubUrl:
        parseSubUrl(one[0],one[1])
        
