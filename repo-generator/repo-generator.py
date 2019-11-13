import ast
import glob
import os
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

def find_all_files(dir):
    repoName = dir.split("/")[-1]
    for root, _, files in os.walk(dir):
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

def main():
    find_all_files("../repos")
    f = open("../data/typed-repos-test")
    for repo in typed:
        f.write(repo + "\n")

if __name__ == "__main__":
    main()
