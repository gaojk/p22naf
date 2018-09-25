import os

def createJsonFile():
    # 获取当前夹子（getcwd）下的路径文件夹和文件
    for root, dirs, files in os.walk(os.getcwd()):
        # 遍历当前文件夹子下的文件们
        for file in files:
            # 如果该问件是txt文件才去执行下面的操作
            if '.txt' in file.lower():
                # 通过root和file来组成该文件打开路径，并打开
                txt_file_path = root + '\\' + file
                # 每一次open一个文件，如果用这个打开的文件搞了任何.readlines()或者啥操作，就需要把当前的关闭，然后再打开一下。
                fileTxts = open(txt_file_path, 'r')
                allLines = len(fileTxts.readlines())
                fileTxts.close()
                fileTxts = open(txt_file_path, 'r')
                # 通过root和splitext创造json文件，并打开
                json_file_path = root + '\\' + os.path.splitext(file)[0] + '.json'
                fileJson = open(json_file_path, 'w')
                # 把当前获取的txt里面的一行行的数据都写到当前创建的Json文件里面去
                # 加左大括号（｛）
                fileJson.write("{\n")
                # 通过formatJsonContent方法生成voidAll键值对，并赋值给strTemp，这里原本没有设置strTemp的，
                # 但是后来发现第一次传了fileTxts后，第二次就不能再次把fileTxts进行下一次传参了。
                strTemp =formatJsonContent("voidAll", fileTxts, allLines)
                # 将strTemp写入fileJson文件
                fileJson.write(strTemp)
                # 这里的allLines用来判断当前的txt文件里面是否有内容，
                # 有内容的话才需要去再生成一套参数，要不然的话就只要一套voidAll的就够了
                if allLines > 0:
                    fileJson.write("\n")
                    # 将strTemp里面的voidAll替换成空之后再复制一遍（用来保存其他的键值对操作）
                    fileJson.write(strTemp.replace("voidAll", ""))
                # 加右大括号（｛）
                fileJson.write("\n}")
                # 永远记得开启文件就关闭文件
                fileJson.close()
                fileTxts.close()
            else:
                continue

# 生成符合需求格式的json字符串
def formatJsonContent(stringFirstKey, fileTxts, allLines):
    # 这里的allLines用来判断当前的txt文件里面是否有内容，
    # 如果有的话就走流程1，如果没有的话就走流程2，殊途同归总之是在处理格式

    # 流程1
    if allLines > 0:
        print(allLines)
        print(type(allLines))
        print("In ner")
        stringList = []
        # 用来输出后面这个东西→→→→    "voidAll": {
        stringFirstKey = '\t"{}": {{\n'.format(stringFirstKey)
        stringList.append(stringFirstKey)
        for fileTxt in fileTxts:
            stringTemp = '\t\t"{}": "",\n'.format(fileTxt.strip("\n"))
            stringList.append(stringTemp)
        # 修改当前数组中最后一个元素的内容（去掉逗号）, -2是因为要去掉回车和逗号，所以还要在最后加上一个\n
        stringList[len(stringList)-1] = stringList[len(stringList)-1][:-2] + "\n"
        # 用来输出后面这个东西→→→→    	},
        rightBracket = '\t},'
        stringList.append(rightBracket)
        # 通过.join方法遍历列表，然后将首-身体-尾连起来，并return
        connectAll = "".join(stringList)
        return connectAll
    # 流程2
    else:
        print(allLines)
        print(type(allLines))
        print("outer")
        stringList = []
        # 用来输出后面这个东西→→→→    "voidAll": {
        stringFirstKey = '\t"{}": {{\n'.format(stringFirstKey)
        stringList.append(stringFirstKey)
        stringBody = '\t\t"{}": "{}",\n'.format("none", "none")
        stringList.append(stringBody)
        # 修改当前数组中最后一个元素的内容（去掉逗号）, -2是因为要去掉回车和逗号，所以还要在最后加上一个\n
        stringList[len(stringList)-1] = stringList[len(stringList)-1][:-2] + "\n"
        # 用来输出后面这个东西→→→→        },
        rightBracket = '\t},'
        stringList.append(rightBracket)
        # 通过.join方法遍历列表，然后将首-身体-尾连起来，并return
        connectAll = "".join(stringList)
        # 去掉最后一个逗号用的代码，想确定就运行一下看看吧
        connectAll = connectAll[:-1]
        return connectAll


def createJsonFile2():
    # 获取当前夹子（getcwd）下的路径文件夹和文件
    for root, dirs, files in os.walk(os.getcwd()):
        # 遍历当前文件夹子下的文件们
        for file in files:
            # 如果该问件是txt文件才去执行下面的操作
            if '.txt' in file.lower():
                # 通过root和file来组成该文件打开路径，并打开
                txt_file_path = root + '\\' + file
                fileTxts = open(txt_file_path, 'r')
                allLinesOfTheTxt = len(fileTxts.readlines())
                # 通过root和splitext创造json文件，并打开
                json_file_path = root + '\\' + os.path.splitext(file)[0] + '.json'
                fileJson = open(json_file_path, 'w')
                # 把当前获取的txt里面的一行行的数据都写到当前创建的Json文件里面去
                countLine = 1
                for fileTxt in fileTxts:
                    fileJson.write(fileTxt)
                    countLine+=1

                # 永远记得开启文件就关闭文件
                fileJson.close()
                fileTxts.close()
            else:
                continue
def createJsonFile3():
    # 获取当前夹子（getcwd）下的路径文件夹和文件
    for root, dirs, files in os.walk(os.getcwd()):
        # 遍历当前文件夹子下的文件们
        for file in files:
            # 如果该问件是txt文件才去执行下面的操作
            if '.txt' in file.lower():
                # 通过root和file来组成该文件打开路径，并打开
                txt_file_path = root + '\\' + file
                fileTxts = open(txt_file_path, 'r')
                # 把当前获取的txt里面的一行行的数据都写到当前创建的Json文件里面去
                countLine = 1
                for fileTxt in fileTxts:
                    print(fileTxt)
                    countLine+=1
                # 永远记得开启文件就关闭文件
                fileTxts.close()
            else:
                continue




createJsonFile()
# createJsonFile2()
# createJsonFile3()


# for root, dirs, files in os.walk(os.getcwd()):
#     print(root)
#     print(dirs)
#     print(files[0])
