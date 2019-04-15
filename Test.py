import os

path = os.getcwd()
fileList = os.listdir(path)
count = 0
for file in fileList:
    stringfile = path + "\ ".strip() + file;
    suffix = ".srt"
    if (file.endswith(suffix)):
        count = count + 1;
        fileSrt = file
if (count == 0):
    print("This directory has not srt files!")
    os.system("PAUSE")
elif (count == 1):
    from mtranslate import translate
    import pysrt
    errorOccure=0
    # Loading the Subtitle
    subs = pysrt.open(fileSrt)
    fileName = fileSrt + "-el.srt"
    fileToWrite = open(fileName, 'w')
    for i in range(0, len(subs)):
        try:
            id = i + 1
            if (id == len(subs)):
                break
            print(str(id) + "/" + str(len(subs)))
            sub = subs[i]

            # Subtitle text
            text = sub.text
            text_without_tags = sub.text_without_tags

            # Start and End time
            start = sub.start.to_time()
            end = sub.end.to_time()
            fileToWrite.write(id.__str__() + "\n")
            start = str(start)
            start = start.replace(".", ",")
            start = start[:-3].strip()
            end = str(end)
            end = end.replace(".", ",")
            end = end[:-3].strip()
            fileToWrite.write(start.__str__() + " --> " + end.__str__() + "\n")
            text = text.replace("\u266a", "")
            text = translate(text, 'el')
            fileToWrite.write(text.__str__() + "\n\n")
        except:
            print("An exception occurred")
            print(text)
            fileToWrite.write(" " + "\n\n")
            errorOccure=errorOccure+1

    fileToWrite.close()
    print("We have "+str(errorOccure)+" exception occured")
    print("Everything works Great!")
    os.system("PAUSE")
else:
    print("You only can convert one srt file at a time. Please leave one srt file")
os.system("PAUSE")
