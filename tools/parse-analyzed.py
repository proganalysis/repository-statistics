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

print(parse("functions-analyzed"))