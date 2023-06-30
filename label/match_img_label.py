import os
import module

def match(path):
    img_arr = module.remove_extension(os.listdir(path + "/images"))
    label_arr = module.remove_extension(os.listdir(path + "/labels"))
    label_arr.remove("classes")
    label_arr.remove("desktop")

    li = [f for f in img_arr if f not in label_arr]
    ll = [f for f in label_arr if f not in img_arr]

    if len(li):
        print("\n===========================")
        print("In Image Folder :")
        print(li)
        print("===========================\n")

    if len(ll):
        print("\n===========================")
        print("In Label Folder :")
        print(ll)
        print("===========================\n")

    if len(ll) == 0 and len(li) == 0:
        print("\n===========================")
        print("Success : Match img-label!")
        print("===========================")
        return True, len(img_arr), img_arr
       
    return False, 0, []