import ast
import glob
import os
import sys
from pprint import pprint

typed = set()
not_typed = set()
python_2 = set()

class Metrics:
    def __init__(self):
        self.typedFunctions = 0
        self.unTypedFunctions = 0
        self.typedAssignments = 0
        self.unTypedAssignments = 0

class Analyzer(ast.NodeVisitor):
    def __init__(self):
        self.metrics = Metrics()
    def visit_FunctionDef(self, node):
        typed = False
        if node.returns != None:
            typed = True
        for arg in node.args.args:
            if arg.annotation != None:
                typed = True
        if typed:
            self.metrics.typedFunctions += 1
        else:
            self.metrics.unTypedFunctions += 1

    def visit_Assign(self, node):
        self.metrics.unTypedAssignments += 1

    def visit_AnnAssign(self, node):
        self.metrics.typedAssignments += 2

    def getMetrics(self):
        return self.metrics

def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

def get_all_repos(rootFolder, flag=False):
    if flag:
        return get_immediate_subdirectories(rootFolder)
    orgs = get_immediate_subdirectories(rootFolder)
    repos = {}
    for org in orgs:
        repos[org] = get_all_repos(rootFolder + "/" + org, True)
    return repos

def scan_all_files(repo, repoName):
    for root, _, files in os.walk(repo):
        typed_status = False
        python_2_status = False
        for file in files:
            if file.endswith(".py"):
                f = open(root + "/" + file)
                try:
                    a = Analyzer()
                    a.visit(ast.parse(f.read()))
                    metrics = a.getMetrics()
                    if metrics.typedAssignments > 0 or metrics.typedFunctions > 0:
                        typed_status = True
                except:
                    python_2_status = True
                    python_2.add(repoName)
        if typed_status == True:
            typed.add(repoName)
        elif python_2_status == False:
            not_typed.add(repoName)

def verify_args():
    if len(sys.argv) == 2:
        if os.path.exists(sys.argv[1]):
            return True
    return False
    
def main():
    if not verify_args():
        print("Usage: python3 ./repo-generator <repo-folder>")
        sys.exit()
        
    folder = sys.argv[1]
    repos = get_all_repos(folder)
    for org in repos.keys():
        for repo in repos[org]:
            repoName = org+"/"+repo
            scan_all_files(folder+repoName, repoName) 
    f = open("../data/typed-repos-org", "w+")
    for repo in typed:
        if repo not in python_2:
            f.write(repo + "\n")

if __name__ == "__main__":
    main()
