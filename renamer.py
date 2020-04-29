import os
from os import path


def main():
    file_dir = input("Enter Images Directory:\n")
    if path.exists(file_dir):
        file_names = os.listdir(file_dir)
        jpeg_files_names = [_ for _ in file_names if _[-5:] == ".jpeg"]
        for file_name in jpeg_files_names:
            src_name = file_dir + "/" + file_name
            dest_name = file_dir + "/" + file_name.lower().replace(" ", "_")
            os.rename(src_name, dest_name)
    else:
        print("Directory Does Not Exist")


if __name__ == '__main__':
    main()
