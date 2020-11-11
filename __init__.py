
from manager_installer import GoogleDriveDownloader

#id with password - 1Y1zAF9vT800S0hGPS4l1yGWIS0OjC40O
#id without password - 1MklJ-SbMx7oJQQXUUsZWqTSm0ObDKFgj
FILE_ID = '1MklJ-SbMx7oJQQXUUsZWqTSm0ObDKFgj'#file id should be fetched from database
DESTINATION_PATH = 'file/file.zip'
OVERWRITE = True
UNZIP = True
ZIPPASS = True

if __name__ == "__main__":
    GoogleDriveDownloader.download_file_from_google_drive(
        file_id=FILE_ID,
        overwrite=OVERWRITE,
        dest_path=DESTINATION_PATH,
        unzip=UNZIP,
        zippass=ZIPPASS
        )