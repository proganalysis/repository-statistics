import ast
import astunparse
f = open('/home/daniel/Documents/College/Semester7/Research/type-analyzer/allrepo/original/(5j9)wikitextparser*tests*test_config.pyi')

class Analyzer(ast.NodeVisitor):
    def visit_FunctionDef(self, node):
        for arg in node.args.args:
            if arg.annotation != None:
                q = astunparse.unparse(arg.annotation)
                print(q)

a = Analyzer()
a.visit(ast.parse(f.read()))