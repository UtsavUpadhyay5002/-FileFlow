import os
import time
import shutil

#getting path of system's downaload folder
downloadPath = os.path.expanduser("~/Downloads")

def reportLog(line):
    #Note: You will need to create a file named logs.txt in the same directory as this script
    file = open("logs.txt", "a")
    file.write(line + "\n")
    file.close()

def detectDownloadsChange():
    list = os.listdir(downloadPath)    #initial list of files
    while True:
        #this code will run every 5 seconds 
        newList = os.listdir(downloadPath)
        flg = 0
        
        for file in newList:
            if file not in list:
                if ".png" in file or ".jpeg" in file or ".jpg" in file:
                    shutil.move(downloadPath + "/" + file, os.path.expanduser("~/Pictures"))
                    print(time.strftime("%H:%M:%S: ")+ file + " moved to Pictures")
                    reportLog(time.strftime("%H:%M:%S: ")+ file + " moved to Pictures")
                elif ".txt" in file:
                    shutil.move(downloadPath + "/" + file, downloadPath + "/Downloaded_docs")
                    print(time.strftime("%H:%M:%S: ")+ file + " moved to " + downloadPath + "/Downloaded_docs")
                    reportLog(time.strftime("%H:%M:%S: ")+ file + " moved to " + downloadPath + "/Downloaded_docs")
                elif ".pdf" in file:
                    shutil.move(downloadPath + "/" + file, downloadPath + "/Downloaded_docs/PDFs")
                    print(time.strftime("%H:%M:%S: ")+ file + " moved to " + downloadPath + "/Downloaded_docs/PDFs")
                    reportLog(time.strftime("%H:%M:%S: ")+ file + " moved to " + downloadPath + "/Downloaded_docs/PDFs")
                elif ".docx" in file:
                    shutil.move(downloadPath + "/" + file, downloadPath + "/Downloaded_docs/MSword")
                    print(time.strftime("%H:%M:%S: ")+ file + " moved to " + downloadPath + "/Downloaded_docs/MSword")
                    reportLog(time.strftime("%H:%M:%S: ")+ file + " moved to " + downloadPath + "/Downloaded_docs/MSword")
                elif ".pptx" in file:
                    shutil.move(downloadPath + "/" + file, downloadPath + "/Downloaded_docs/PPTs")
                    print(time.strftime("%H:%M:%S: ")+ file + " moved to " + downloadPath + "/Downloaded_docs/PPTs")
                    reportLog(time.strftime("%H:%M:%S: ")+ file + " moved to " + downloadPath + "/Downloaded_docs/PPTs")
                elif ".csv" in file:
                    shutil.move(downloadPath + "/" + file, downloadPath + "/Downloaded_docs/CSVs")
                    print(time.strftime("%H:%M:%S: ")+ file + " moved to " + downloadPath + "/Downloaded_docs/CSVs")
                    reportLog(time.strftime("%H:%M:%S: ")+ file + " moved to " + downloadPath + "/Downloaded_docs/CSVs")
                elif ".mp4" in file or ".mkv" in file or ".mp3" in file:
                    shutil.move(downloadPath + "/" + file, os.path.expanduser("~/Videos"))
                    print(time.strftime("%H:%M:%S: ")+ file + " moved to Videos")
                    reportLog(time.strftime("%H:%M:%S: ")+ file + " moved to Videos")
                elif ".exe" in file:
                    shutil.move(downloadPath + "/" + file, downloadPath + "/executables")
                    print(time.strftime("%H:%M:%S: ")+ file + " moved to " + downloadPath + "/executables")
                    reportLog(time.strftime("%H:%M:%S: ")+ file + " moved to " + downloadPath + "/executables")
                elif ".zip" in file:
                    shutil.move(downloadPath + "/" + file, downloadPath + "/Zips")
                    print(time.strftime("%H:%M:%S: ")+ file + " moved to " + downloadPath + "/Zips")
                    reportLog(time.strftime("%H:%M:%S: ")+ file + " moved to " + downloadPath + "/Zips")
                elif ".drawio" in file:
                    shutil.move(downloadPath + "/" + file, downloadPath + "/drawios")
                    print(time.strftime("%H:%M:%S: ")+ file + " moved to " + downloadPath + "/drawios")
                    reportLog(time.strftime("%H:%M:%S: ")+ file + " moved to " + downloadPath + "/drawios")
                elif ".py" in file or ".java" in file or ".cpp" in file:
                    shutil.move(downloadPath + "/" + file, downloadPath + "/Downloaded_codes")
                    print(time.strftime("%H:%M:%S: ")+ file + " moved to " + downloadPath + "/Downloaded_codes")
                    reportLog(time.strftime("%H:%M:%S: ")+ file + " moved to " + downloadPath + "/Downloaded_codes")
                else:
                    x=0
        if flg == 0:
            print(time.strftime("%H:%M:%S: NO CHANGE"))
        else:
            list = os.listdir(downloadPath)    #list after making changes
        
        time.sleep(5)

detectDownloadsChange()
