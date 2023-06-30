import match_img_label as MIL
import make as M

path = ""

if path == "":
    path = input("Input Folder Path : ")

is_match, data_size, data_arr = MIL.match(path)

if is_match == True:
    try:
        M.make_set_folder(path)
        M.make_yaml(path)
        M.make_set(path, data_size, data_arr)
        M.make_zip(path)
    except OSError as exc:
        print(exc)
