import os
import time
import shutil

#getting path of system's downaload folder
downloadPath = os.path.expanduser("~/Downloads")

list = os.listdir(downloadPath)    #initial list of files

while True:
    newList = os.listdir(downloadPath)
    
    for file in newList:
        if file not in list:
            if ".png" in file or ".jpeg" in file or ".jpg" in file:
                shutil.move(downloadPath + "/" + file, os.path.expanduser("~/Pictures"))
            elif ".mp4" in file or ".mkv" in file or ".mp3" in file:
                shutil.move(downloadPath + "/" + file, os.path.expanduser("~/Videos"))
            elif ".txt" in file:
                shutil.move(downloadPath + "/" + file, downloadPath + "/Downloaded_docs")
            elif ".pdf" in file:
                shutil.move(downloadPath + "/" + file, downloadPath + "/Downloaded_docs/PDFs")
            elif ".docx" in file:
                shutil.move(downloadPath + "/" + file, downloadPath + "/Downloaded_docs/MSword")
            elif ".pptx" in file:
                shutil.move(downloadPath + "/" + file, downloadPath + "/Downloaded_docs/PPTs")
            elif ".csv" in file:
                shutil.move(downloadPath + "/" + file, downloadPath + "/Downloaded_docs/CSVs")
            elif ".exe" in file:
                shutil.move(downloadPath + "/" + file, downloadPath + "/executables")
            elif ".zip" in file:
                shutil.move(downloadPath + "/" + file, downloadPath + "/Zips")
            elif ".drawio" in file:
                shutil.move(downloadPath + "/" + file, downloadPath + "/drawios")
            elif ".py" in file or ".java" in file or ".cpp" in file:
                shutil.move(downloadPath + "/" + file, downloadPath + "/Downloaded_codes")
            else:
                pass

    list = os.listdir(downloadPath)    #list after making changes
    
    #this code will run every 10 seconds
    time.sleep(10)