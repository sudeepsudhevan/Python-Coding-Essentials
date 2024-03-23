import os
import shutil
import datetime
import time
import schedule

source_dir = "C:/Users/sudeepp/Desktop/cele"
destination_dir = "D:/backups"


def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    des_dir = os.path.join(dest, str(today))

    try:
        shutil.copytree(source, des_dir)
        print(f"Folder copied to: {des_dir}")
    except FileExistsError as e:
        print(f"Folder already exist in:{dest}")


schedule.every().day.at("11:44").do(
    lambda: copy_folder_to_directory(source_dir, destination_dir)
)

while True:
    schedule.run_pending()
    time.sleep(60)
