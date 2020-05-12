import ast
import glob
import astunparse
import os
from pprint import pprint
from collections import OrderedDict

assignment_types = {}
function_return_types = {}
param_types = {}
total_func = 0
total_assign = 0
total_param = 0
functions_analyzed = {}
assignments_analyzed = {}


# Data class holding metric information
class Metrics:
    def __init__(self, file_name):
        self.file_name = file_name
        self.assignments = 0
        self.functions = 0
        self.params = 0
        self.assignment_type_map = {}
        self.function_return_type_map = {}
        self.param_type_map = {}


def add_to_functions(file_name, function_name):
    global functions_analyzed
    if file_name in functions_analyzed.keys():
        if function_name not in functions_analyzed[file_name]:
            functions_analyzed[file_name].append(function_name)
    else:
        functions_analyzed[file_name] = [function_name]


def add_to_assign(file_name, assignment_name):
    global assignments_analyzed
    if file_name in assignments_analyzed.keys():
        if assignment_name not in assignments_analyzed[file_name]:
            assignments_analyzed[file_name].append(assignment_name)
    else:
        assignments_analyzed[file_name] = [assignment_name]


# AST class to visit each node and calculate metrics based on the node
class Analyzer(ast.NodeVisitor):
    def __init__(self, file_name, functions, assignments):
        self.functions = functions
        self.assignments = assignments
        self.metrics = Metrics(file_name)

    def visit_FunctionDef(self, node):
        if self.metrics.file_name in self.functions.keys(
        ) and node.name in self.functions[self.metrics.file_name]:
            add_to_functions(self.metrics.file_name, node.name)
            if node.returns is not None:
                q = astunparse.unparse(node.returns)
                q = q.strip()
                if q in self.metrics.function_return_type_map.keys():
                    self.metrics.function_return_type_map[q] += 1
                else:
                    self.metrics.function_return_type_map[q] = 1
            for arg in node.args.args:
                if arg.annotation != None:
                    q = astunparse.unparse(arg.annotation)
                    q = q.strip()
                    if q in self.metrics.param_type_map.keys():
                        self.metrics.param_type_map[q] += 1
                    else:
                        self.metrics.param_type_map[q] = 1
                    self.metrics.params += 1
            self.metrics.functions += 1

    def visit_Assign(self, node):
        if self.metrics.file_name in self.assignments.keys():
            for tgt in node.targets:
                if hasattr(tgt, 'id'):
                    if tgt.id in self.assignments[self.metrics.file_name]:
                        self.metrics.assignments += 1

    def visit_AnnAssign(self, node):
        if self.metrics.file_name in self.assignments.keys():
            q = astunparse.unparse(node.annotation)
            q = q.strip()
            if q in self.metrics.assignment_type_map.keys():
                self.metrics.assignment_type_map[q] += 1
            else:
                self.metrics.assignment_type_map[q] = 1
            self.metrics.assignments += 1

    def getMetrics(self):
        return self.metrics


def parse(data):
    funcs = {}
    f = open(data, "r")
    lines = f.readlines()
    for line in lines:
        line = line.split(":")
        file_name = line[0]
        func_name = line[1].strip()
        if file_name in funcs.keys():
            funcs[file_name].append(func_name)
        else:
            funcs[file_name] = [func_name]
    return funcs


def get_list_of_files(root_dir):
    files = [
        f for f in os.listdir(root_dir)
        if os.path.isfile(os.path.join(root_dir, f))
    ]
    paths = []
    for file in files:
        repo = file[file.index("(") + 1:file.index(")")]
        inner_path = file[file.index(")") + 1:]
        inner_path = inner_path.replace("*", "/")
        paths.append(repo + '/' + inner_path[:len(inner_path) - 1])
    return paths


if __name__ == "__main__":
    functions_analyzed = parse(
        "/home/daniel/Documents/College/Semester7/Research/type-analyzer/tools/dataset/functions"
    )
    assignments_analyzed = parse(
        "/home/daniel/Documents/College/Semester7/Research/type-analyzer/tools/dataset/assignments"
    )
    list_of_files = get_list_of_files(
        "/home/daniel/Documents/College/Semester7/Research/type-analyzer/allrepo/original"
    )
    files_found = 0
    files_not_found = 0
    for file in list_of_files:
        if file in functions_analyzed.keys(
        ) or file in assignments_analyzed.keys():
            a = Analyzer(file, functions_analyzed, assignments_analyzed)
            if os.path.exists(
                    "/home/daniel/Documents/College/Semester7/Research/type-analyzer/typed-repos-new/"
                    + file):
                files_found += 1
                try:
                    f = open(
                        "/home/daniel/Documents/College/Semester7/Research/type-analyzer/typed-repos-new/"
                        + file)
                    a.visit(ast.parse(f.read()))
                    metrics = a.getMetrics()
                    total_func += metrics.functions
                    total_assign += metrics.assignments
                    total_param += metrics.params
                    for k in metrics.assignment_type_map.keys():
                        if k in assignment_types.keys():
                            assignment_types[k] += metrics.assignment_type_map[
                                k]
                        else:
                            assignment_types[k] = metrics.assignment_type_map[
                                k]
                    for k in metrics.function_return_type_map.keys():
                        if k in function_return_types.keys():
                            function_return_types[
                                k] += metrics.function_return_type_map[k]
                        else:
                            function_return_types[
                                k] = metrics.function_return_type_map[k]
                    for k in metrics.param_type_map.keys():
                        if k in param_types.keys():
                            param_types[k] += metrics.param_type_map[k]
                        else:
                            param_types[k] = metrics.param_type_map[k]
                except Exception as e:
                    print(file, e)
            else:
                files_not_found += 1

    print("\n------ Function return types ------\n")
    print(f"Total func: {total_func}")
    sorted_func = OrderedDict(
        sorted(function_return_types.items(), key=lambda x: x[1],
               reverse=True))
    for k in sorted_func.keys():
        print(f"{k}: {sorted_func[k]}")

    sorted_assign = OrderedDict(
        sorted(assignment_types.items(), key=lambda x: x[1], reverse=True))
    print("\n------ Assignment types ------\n")
    print(f"Total assignments: {total_assign}")
    for k in sorted_assign.keys():
        print(f"{k}: {sorted_assign[k]}")

    sorted_param = OrderedDict(
        sorted(param_types.items(), key=lambda x: x[1], reverse=True))
    print("\n------ Parameter types ------\n")
    print(f"Total parameters: {total_param}")
    for k in sorted_param.keys():
        print(f"{k}: {sorted_param[k]}")
    '''
    function_output = open("functions-analyzed", "w+")
    for k in functions_analyzed.keys():
        for v in functions_analyzed[k]:
            function_output.write("%s:%s\n" % (k, v))
    function_output.close()

    assign_output = open("assign-analyzed", "w+")
    for k in assignments_analyzed.keys():
        for v in assignments_analyzed[k]:
            assign_output.write("%s:%s\n" % (k, v))
    assign_output.close()
    '''
