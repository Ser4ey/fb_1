from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


class GoogleDrive11:
    def __init__(self, dir_id):
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()  # client_secrets.json need to be in the same directory as the script
        drive = GoogleDrive(gauth)

        self.drive = drive
        self.dir_id = dir_id

    def upload_file(self, file_path):
        file1 = self.drive.CreateFile({"parents": [{"id": self.dir_id}]})
        file1.SetContentFile(file_path)
        file1.Upload()

        return file1['id']



g1 = GoogleDrive11('1xgxlthzG8xC2tIlQuoC5geeq3_Om9q-1')
r1 = g1.upload_file('/home/ser4/PycharmProjects/fasebook_parser/key_words.txt')
print(r1)
r2 = g1.upload_file('/home/ser4/PycharmProjects/fasebook_parser/geckodriver.log')
print(r2)