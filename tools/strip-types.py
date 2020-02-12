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
        print("Usage: python3 ./strip-types <repo-folder>")
        sys.exit()
    
    folder = os.path.abspath(sys.argv[1])
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".py"): 
                file = f"{os.path.join(root, file)}"
                subprocess.call(["./strip.sh", file])
                
if __name__ == "__main__":
    main()