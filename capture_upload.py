import cv2
from cv2 import VideoCapture
import dropbox
import time
import random

start_time= time.time()

def take_snapshot():
    number=random.randint(0,100)
    #initializing cv2
    videoCaptureObject= cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame = videoCaptureObject.read()
        #cv2.imwrite() method is used to save an image to a storage place
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time
        result=False
    return img_name
    print("snapshot is taken")

    # releases the camera
    videoCaptureObject.release()
    #closes all the window that might be opened while this process
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token = "sl.BK9mx8rSHEBkrR6z1ISFjrZ3MY66to6fBxsiKTEd8ihvLlSchBRpSlVfaRjMPMjwHNYzkYBcUOalZdR0m7WQoQV7K2Mv8zM4togAEOuZK2wvrjR-Oz4rjlsnM-puyfgfSpsE-l0"
    file =img_name
    file_from = file
    file_to="/testFolder/"+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")


def main():
    while(True):
        if ((time.time() - start_time) >= 5):
            name = take_snapshot()
            upload_file(name)

main()