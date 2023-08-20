import subprocess
import pathlib

def clean():
    cwd = pathlib.Path(".");
    for file_pattern in (
        "*.o",
        "*.so",
        "*.obj",
        "*.dll",
        "*.exp",
        "*.lib",
        "*.pyd"):
        for file in cwd.glob(file_pattern):
            file.unlink();

# not windows (:
def build(file: str,objectfile=None, capture_output=True):
    print("="*10);
    print("Building C/C++ library");
    # without extension
    file_name = file[:file.find(".")]
    # if None do this
    if(not objectfile):
        objectfile = file_name;
    cmd = f"clang++ -c -fPIC {file} -o {objectfile}.o".split(" ");
    ret = subprocess.run(cmd,capture_output=capture_output);
    print(ret);
    # print("Successfully built {}".format(file));