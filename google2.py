from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth() # client_secrets.json need to be in the same directory as the script
drive = GoogleDrive(gauth)

fileList = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for file in fileList:
  print('Title: %s, ID: %s' % (file['title'], file['id']))
  # Get the folder ID that you want
  if(file['title'] == "fb_test"):
      fileID = file['id']

# print(fileID)
file_metadata = {
    'name': '1.csv',
    'parents': [fileID]
}

file1 = drive.CreateFile({"parents": [{"id": fileID}]})
file1.SetContentFile("results/сало1628760019.csv")
file1.Upload()

#
# file1 = drive.CreateFile({'name': name, "parents": fileID})
# file1.SetContentFile("results/сало1628760019.csv")
# file1.Upload()
print('Created file %s with mimeType %s' % (file1['title'], file1['mimeType']))
print(file1['id'])


class GoogleDrive:
    def __init__(self, dir_id):
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()  # client_secrets.json need to be in the same directory as the script
        drive = GoogleDrive(gauth)

        self.drive = drive