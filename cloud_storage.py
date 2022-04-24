from copyreg import constructor
from lib2to3.pgen2 import token
import dropbox

Class Transfer_data():
    def __init__(self,access_token):
        self.access_token=access_token
    
    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)


        f=open(file_from,' rb ')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token=: