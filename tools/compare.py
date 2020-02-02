import ast
import glob
import os
import sys
from pprint import pprint

class TypeHints:
    def __init__(self, offset):
        self.functions = {}
        self.assignments = {}
        self.offset = offset
    
    def buildID(self, line, col, name):
        line = line + self.offset
        return f"{line}_{col}_{name}"
    
    

class Analyzer(ast.NodeVisitor):
    def visit_FunctionDef(self, node):
        id = self.typehints.buildID(node.lineno, node.col_offset, node.name)
        if node.returns == None or not hasattr(node.returns, 'id'):
            self.typehints.functions[id] = None
        else:
            self.typehints.functions[id] = node.returns.id

    def visit_Assign(self, node):
        id = self.typehints.buildID(node.lineno, node.col_offset, node.targets[0].id)
        self.typehints.assignments[id] = None

    def visit_AnnAssign(self, node):
        id = self.typehints.buildID(node.lineno, node.col_offset, node.target.id)
        self.typehints.assignments[id] = node.annotation.id

def scan(f, _typehints):
    f = open(f)
    a = Analyzer()
    a.typehints = _typehints
    a.visit(ast.parse(f.read()))


def main():
    n = sys.argv[1]
    count = len(open(f"../micro-cases/{n}.py").readlines(  ))
    countGen = len(open(f"../micro-cases/{n}-gen.py").readlines(  ))
    offset = 0
    if countGen > count:
        offset = countGen - count
    handwritten = TypeHints(offset)
    generated = TypeHints(0)
    scan(f"../micro-cases/{n}.py", handwritten)
    scan(f"../micro-cases/{n}-gen.py", generated)
    functions_correct = 0
    functions_incorrect = 0
    assignments_correct = 0
    assignments_incorrect = 0
    for k in handwritten.functions.keys():
        if k not in generated.functions.keys():
            print(f"Key wasn't found in generated: {k}")
        else:
            if handwritten.functions[k] != generated.functions[k]:
                functions_incorrect += 1
            else:
                functions_correct += 1
    
    for k in handwritten.assignments.keys():
        if k not in generated.assignments.keys():
            print(f"Key wasn't found in generated: {k}")
        else:
            if handwritten.assignments[k] != generated.assignments[k]:
                assignments_incorrect += 1
            else:
                assignments_correct += 1
    
    print(f"Correct functions: {functions_correct}")
    print(f"Incorrect functions: {functions_incorrect}")
    print(f"Correct assignments: {assignments_correct}")
    print(f"Incorrect assignments: {assignments_incorrect}")
if __name__ == "__main__":
    main()
