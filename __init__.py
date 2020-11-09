#from manager_installer import GoogleDriveDownloader
from manager_installer import GoogleDriveDownloader

FILE_ID = '1MklJ-SbMx7oJQQXUUsZWqTSm0ObDKFgj'
DESTINATION_PATH = 'file/file.zip'
UNZIP = True

if __name__ == "__main__":
    GoogleDriveDownloader.download_file_from_google_drive(
        file_id=FILE_ID,
        dest_path=DESTINATION_PATH,
        unzip=UNZIP
        )