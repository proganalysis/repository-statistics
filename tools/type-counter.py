import ast
import glob
import os
from pprint import pprint


assignment_types = {}
function_return_types = {}
total_func = 0
total_assign = 0
# Data class holding metric information
class Metrics:
    def __init__(self):
        self.file_name = ""
        self.assignments = 0
        self.functions = 0
        self.assignment_type_map = {}
        self.function_return_type_map = {}

# AST class to visit each node and calculate metrics based on the node
class Analyzer(ast.NodeVisitor):
    def __init__(self):
        self.metrics = Metrics()
    def visit_FunctionDef(self, node):
        if node.returns != None:
            if node.returns.id in self.metrics.function_return_type_map.keys():
                self.metrics.function_return_type_map[node.returns.id] += 1
            else:
                self.metrics.function_return_type_map[node.returns.id] = 1
        for arg in node.args.args:
            if arg.annotation != None:
                if arg.annotation.id in self.metrics.assignment_type_map.keys():
                    self.metrics.assignment_type_map[arg.annotation.id] += 1
                else:
                    self.metrics.assignment_type_map[arg.annotation.id] = 1
        self.metrics.functions += 1

    def visit_Assign(self, node):
        self.metrics.assignments += 1

    def visit_AnnAssign(self, node):
        # node
        if node.annotation.id in self.metrics.assignment_type_map.keys():
            self.metrics.assignment_type_map[node.annotation.id] += 1
        else:
            self.metrics.assignment_type_map[node.annotation.id] = 1
        self.metrics.assignments += 1

    def getMetrics(self):
        return self.metrics

def get_list_of_files(root_dir):
    files = [f for f in os.listdir(root_dir) if os.path.isfile(os.path.join(root_dir, f))]
    paths = []
    for file in files:
        repo = file[file.index("(")+1:file.index(")")]
        inner_path = file[file.index(")")+1:]
        inner_path = inner_path.replace("*", "/")
        paths.append(repo+'/'+inner_path[:len(inner_path)-1])
    return paths 

if __name__ == "__main__":
    list_of_files = get_list_of_files("../allrepo/original")
    files_found = 0
    files_not_found = 0
    a = Analyzer()
    for file in list_of_files:
        if os.path.exists("../typed-repos-new/" + file):
            files_found += 1
            try:
                f = open("../typed-repos-new/" + file)
                a.visit(ast.parse(f.read()))
                metrics = a.getMetrics()
                for k in metrics.assignment_type_map.keys():
                    total_assign += metrics.assignment_type_map[k]
                    if k in assignment_types.keys():
                        assignment_types[k] += metrics.assignment_type_map[k]
                    else:
                        assignment_types[k] = metrics.assignment_type_map[k]
                for k in metrics.function_return_type_map.keys():
                    total_func += metrics.function_return_type_map[k]
                    if k in function_return_types.keys():
                        function_return_types[k] += metrics.function_return_type_map[k]
                    else:
                        function_return_types[k] = metrics.function_return_type_map[k]
            except:
                continue
        else:
            files_not_found += 1
    
    print("\n------ Function return types ------\n")
    print(f"Total func: {total_func}")
    for k in function_return_types.keys():
        print(f"{k}: {function_return_types[k]}")

    print("\n------ Assignment types ------\n")
    print(f"Total assignments: {total_assign}")
    for k in assignment_types.keys():
        print(f"{k}: {assignment_types[k]}")
    
