import ast
import glob
import os
from pprint import pprint

# Map containing a list of metrics per repo --> [repo_name] = [file1metrics, file2metrics, etc...]
metricsList = {}


# Data class holding metric information
class Metrics:
    def __init__(self):
        self.file_name = ""
        self.typedFunctions = 0
        self.unTypedFunctions = 0
        self.typedAssignments = 0
        self.unTypedAssignments = 0

# AST class to visit each node and calculate metrics based on the node
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
        self.metrics.typedAssignments += 1

    def getMetrics(self):
        return self.metrics

# Returns a list of strings of the typed-repos generated by the script stored in "typed-repos"
def get_list_of_typed():
    content = None
    with open("./data/typed-repos-org") as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content

# Goes through each python file and records metrics
def calculate_repo_metrics(dir, repoName):
    for root, _, files in os.walk(dir):
        for file in files:
            if file.endswith(".py"):
                f = open(root + "/" + file)
                try:
                    a = Analyzer()
                    a.visit(ast.parse(f.read()))
                    metrics = a.getMetrics()
                    metrics.name = root + "/" + file
                    if repoName in metricsList.keys():
                        metricsList[repoName].append(metrics)
                    else:
                        metricsList[repoName] = [metrics]
                except:
                    continue

def safe_divide(n, d):
    return (n / d) * 100 if d else 0

def main():
    # Retreives all of the metrics
    repo_names = get_list_of_typed()
    folder = os.getcwd()
    folder = folder + "/repos/"
    i = 0
    for subfolder in repo_names:
        i += 1
        print(f"Visiting repo {i} out of {len(repo_names)}")
        calculate_repo_metrics(folder+subfolder, subfolder)

    # Iterate through the data collected and output statistics to a file
    total_functions = 0
    typed_functions = 0
    typed_assignments = 0
    total_assignments = 0
    f = open("./data/stats-per-repo-org", "w+")
    for repo in metricsList.keys():
        f.write(f"\nRepo: {repo}\n")
        f.write("------------------------------------\n")
        repo_functions = 0
        repo_typed_functions = 0
        repo_assignments = 0
        repo_typed_assignments = 0
        for x in metricsList[repo]:
            # Write file stats
            f.write(f"\tFile: {x.name}: \n")
            f.write(f"\t\tTotal functions {x.typedFunctions + x.unTypedFunctions}\n")
            f.write(f"\t\tTyped functions {x.typedFunctions}\n")
            f.write(f"\t\tTotal Assignments {x.typedAssignments + x.unTypedAssignments}\n")
            f.write(f"\t\tTyped Assignments {x.typedAssignments}\n\n")
            repo_functions += x.typedFunctions + x.unTypedFunctions
            repo_typed_functions += x.typedFunctions
            repo_assignments += x.typedAssignments + x.unTypedAssignments
            repo_typed_assignments += x.typedAssignments
        # Write repo stats
        f.write(f"Repository: {repo} statistics\n")
        f.write("------------------------------------\n")
        f.write(f"Total functions: {repo_functions}\n")
        f.write(f"Typed functions: {repo_typed_functions}\n")
        f.write(f"Percentage of functions typed: {safe_divide(repo_typed_functions, repo_functions):.2f}%\n")
        f.write(f"Total Assignments: {repo_assignments}\n")
        f.write(f"Typed Assignments: {repo_typed_assignments}\n")
        f.write(f"Percentage of assignments typed: {safe_divide(repo_typed_assignments, repo_assignments):.2f}%\n\n")
        total_functions += repo_functions
        typed_functions += repo_typed_functions
        typed_assignments += repo_typed_assignments
        total_assignments += repo_assignments

    f.write("\nGlobal stats\n")
    f.write("------------------------------------\n")
    f.write(f"Total functions: {total_functions}\n")
    f.write(f"Typed functions: {typed_functions}\n")
    f.write(f"Percentage of functions typed: {safe_divide(typed_functions, total_functions):.2f}%\n")
    f.write(f"Total Assignments: {total_assignments}\n")
    f.write(f"Typed Assignments: {typed_assignments}\n")
    f.write(f"Percentage of assignments typed: {safe_divide(typed_assignments, total_assignments):.2f}%\n")

if __name__ == "__main__":
    main()
