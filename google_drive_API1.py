import requests
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import time

import data


class GoogleDrive11:
    def __init__(self, dir_id):
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()  # client_secrets.json need to be in the same directory as the script
        drive = GoogleDrive(gauth)

        self.drive = drive
        self.dir_id = dir_id

    def upload_file(self, file_path):
        # file1 = self.drive.CreateFile({"parents": [{"id": self.dir_id}]})
        file1 = self.drive.CreateFile()
        file1.SetContentFile(file_path)
        file1.Upload()

        return "https://drive.google.com/uc?export=view&id=" + str(file1['id'])

    def save_video(self, url):
        if url == '':
            return ''

        r = requests.get(url)
        name = str(time.time()) + '.mp4'
        path_to_file = 'media/' + name

        with open(path_to_file, 'wb') as f:
            f.write(r.content)

        return self.upload_file(path_to_file)

    def save_image(self, url):
        if url == '':
            return ''

        r = requests.get(url)
        name = str(time.time()) + '.jpg'
        path_to_file = 'media/' + name

        with open(path_to_file, 'wb') as f:
            f.write(r.content)

        return self.upload_file(path_to_file)


GoogleDriverSave11 = GoogleDrive11(data.google_drive_dir_id)

# GoogleDriverSave11.upload_file('/home/ser4/PycharmProjects/fasebook_parser/media/1628769162.8013887.jpg')

