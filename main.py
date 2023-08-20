import eel
import eel.browsers
import ctypes
import pathlib


# test c++ library
if __name__ == "__main__":
    libname = pathlib.Path("libcmult.so").absolute();
    c_lib = ctypes.CDLL(libname);
    answer = c_lib.cmult(6,2.3);
    print(answer);



eel.browsers.set_path('electron', 'node_modules/electron/dist/Electron.app/Contents/MacOS/Electron');


eel.init("web");

@eel.expose
def install_driver():
    print("Installing driver");

eel.start("index.html", mode="electron");