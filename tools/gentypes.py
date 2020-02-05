import sys
import os
import subprocess

def verify_args():
    if len(sys.argv) == 2:
        if os.path.exists(sys.argv[1]):
            return True
    return False

def main():
    if not verify_args():
        print("Usage: python3 ./gentypes <repo-folder>")
        sys.exit()
        
    for root, dirs, files in os.walk(sys.argv[1]):
        for file in files:
            if file.endswith(".py"): 
                tmp = ".pytype/pyi"
                subprocess.call(["pytype", f"{os.path.join(root, file)}"])
                subprocess.call(["retype", "-i", "-a", "-p", ".pytype/pyi", f"{os.path.join(root, file)}"])
                subprocess.call(["cp", "-r", "./typed-src", root])
    subprocess.call(["rm", "-rf", "./typed-src", ".pytype"])

                
if __name__ == "__main__":
    main()