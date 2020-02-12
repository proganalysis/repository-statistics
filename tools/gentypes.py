import sys
import os
import subprocess

PYI_FOLDER = ".pytype/pyi"

def verify_args():
    if len(sys.argv) == 2:
        if os.path.exists(sys.argv[1]):
            return True
    return False

def main():
    if not verify_args():
        print("Usage: python3 ./gentypes <repo-folder>")
        sys.exit()

    folder = os.path.abspath(sys.argv[1])

    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".py.stripped.py"): 
                file_path = f"{os.path.join(root, file)}"
                pyi = f"{os.path.join(root, PYI_FOLDER)}/{file}i"
                gen_file = open(file_path.split(".py.stripped.py")[0] + "-gen.py", "w+")
                subprocess.call(["pytype", file_path], cwd=root)
                subprocess.call(["merge-pyi", file_path, pyi], stdout=gen_file)
                #subprocess.call(["retype", "-i", "-a", "-p", ".pytype/pyi", f"{os.path.join(root, file)}"], cwd=root)
                # subprocess.call(["cp", "-r", "./typed-src", root])
    # subprocess.call(["rm", "-rf", "./typed-src", ".pytype"])

                
if __name__ == "__main__":
    main()