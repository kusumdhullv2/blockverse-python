import os
import shutil

from_dir = r"C:\kusum-python\All_document"
to_dir = r"C:\kusum-python\organised"

list_files = os.listdir(from_dir)
print(list_files)

for name_file in list_files:
    name, extension = os.path.splitext(name_file)

    if extension =="":
        continue
    if extension.lower() in ['.jpg','.png','.gif']:
        folder_name = "image_files"
    elif extension.lower() in [ '.mov','mp4']:
        folder_name = "video_files"
    elif extension.lower() in ['.wav','mp3']:
        folder_name = "audio_files"
    elif extension.lower() == '.py':
        folder_name = "python_files"
    else:
        folder_name = "others"

    final_folder = os.path.join(to_dir,folder_name)

    if not os.path.exists(final_folder):
        os.mkdir(final_folder)

    src_path = os.path.join(from_dir , name_file)
    dest_path = os.path.join(final_folder, name_file)

    print(f"moving {name_file} to {final_folder}")
    shutil.move(src_path, dest_path)
    print(f"{name_file} moved successfully!")

    





