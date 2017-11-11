import ctypes
import os
import time

# Snippet von http://anothergisblog.blogspot.de/2012/05/checking-hard-drive-space-using-python.html
# Funktions Anfang


def get_free_space(folder, format="GB"):
    fConstants = {"GB": 1073741824,
                  "MB": 1048576,
                  "KB": 1024,
                  "B": 1
                  }
    free_bytes = ctypes.c_ulonglong(0)
    ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(folder), None, None, ctypes.pointer(free_bytes))
    return int(free_bytes.value / fConstants[format.upper()])


# Funktions Ende

# Irgentwat mit Main oder so xD
def get_old_file():
    high = 0
    for filename in os.listdir(r"e:/aufnahmen"):
        if os.path.getmtime(os.path.join(r"e:/aufnahmen", filename)) < high or high == 0:
            high = os.path.getmtime(os.path.join(r"e:/aufnahmen", filename))
            datei = filename
    return "E:/Aufnahmen/"+datei

if __name__ == "__main__":
    while True:
        byteformat = "gb"
        free_gb = get_free_space(r"e:", byteformat)
        if free_gb < 50:
            while free_gb < 50:
                os.remove(get_old_file())
                free_gb = get_free_space(r"e:", byteformat)
        time.sleep(600)