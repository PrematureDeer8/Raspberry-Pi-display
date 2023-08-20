import eel
import eel.browsers
import ctypes
import pathlib


# test c++ library
if __name__ == "__main__":
    libfile = list(pathlib.Path("build").glob("*/cmult*.so"))[0];
    c_lib = ctypes.CDLL(libfile);
    x,y = 6, 2.3;
    c_lib.cmult.restype = ctypes.c_float;
    ans = c_lib.cmult(x,ctypes.c_float(y));
    print(f"    In python : int {x} float {y} returning {round(ans,1)}");



eel.browsers.set_path('electron', 'node_modules/electron/dist/Electron.app/Contents/MacOS/Electron');


eel.init("web");

@eel.expose
def install_driver():
    print("Installing driver");

eel.start("index.html", mode="electron");