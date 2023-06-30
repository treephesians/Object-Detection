import os
import shutil

def make_set_folder(path):
    os.makedirs(f"{path}/train/images")
    os.makedirs(f"{path}/train/labels")
        
    os.makedirs(f"{path}/valid/images")
    os.makedirs(f"{path}/valid/labels")

    os.makedirs(f"{path}/test/images")
    os.makedirs(f"{path}/test/labels")
    
    print("Success : Made Folder")
    print("===========================")
    return

def make_yaml(path):
    data_name = input("Data Name : ")
    folder_name = path.split("\\")[-1]
    print(f"Folder = {folder_name}")
    print("===========================")
    f = open(f"{path}\\data.yaml", 'w')
    f.write("names:\n")
    f.write(f"- {data_name}\n")
    f.write("nc: 1\n")
    f.write(f"test: ../test/images\n")
    f.write(f"train: images/{folder_name}/train/images\n")
    f.write(f"val: images/{folder_name}/valid/images\n")
    return

def make_set(path, data_size, data_arr):
    train, valid, test = 0, 0, 0
    for i in range(data_size):
        seq = i % 10
        # train
        if seq < 7:
            train += 1
            shutil.move(f"{path}\\images\\{data_arr[i]}.jpg", f"{path}\\train\\images")
            shutil.move(f"{path}\\labels\\{data_arr[i]}.txt", f"{path}\\train\\labels")
        # valid
        elif seq < 9:
            valid += 1
            shutil.move(f"{path}\\images\\{data_arr[i]}.jpg", f"{path}\\valid\\images")
            shutil.move(f"{path}\\labels\\{data_arr[i]}.txt", f"{path}\\valid\\labels")
        # test
        else:
            test += 1
            shutil.move(f"{path}\\images\\{data_arr[i]}.jpg", f"{path}\\test\\images")
            shutil.move(f"{path}\\labels\\{data_arr[i]}.txt", f"{path}\\test\\labels")
    os.remove(f"{path}\\labels\\classes")
    os.rmdir(f"{path}\\images")
    os.rmdir(f"{path}\\labels")
    print(f"train {train}\nvalid {valid}\ntest  {test}")
    print("===========================")
    return

def make_zip(path):
    folder_name = path.split("\\")[-1]
    folder_location = f"{path}"
    zip_location = f"{path}/{folder_name}"
    shutil.make_archive(zip_location,"zip",folder_location)
    return zip_location