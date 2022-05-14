import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from,file_to):
        dbx= dropbox.Dropbox(self.access_token)
        f= open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token='sl.BFy0iUPY4pztUa3Azrg2UShgBQzIsoxG_SUr36hzcpaIQGLTIzUnf85kXyTjQ7QvU11_Sx3vkJthKJEpeft8xd4uaI-3hMYm1q-T3POksXAJc6sRAxKUDfrfNetNwvwzNV03sUbnDkBQ'
    transferData=TransferData(access_token)

    file_from=input("enter the file path to transfer ")
    file_to=input("enter the full path to dropbox")

    transferData.upload_file(file_from,file_to)
    print("file has been moved")

main()

