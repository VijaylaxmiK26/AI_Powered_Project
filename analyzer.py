import ast


def analyze_file(file_path):

    with open(file_path, "r") as f:
        source = f.read()

    tree = ast.parse(source)

    functions = []
    classes = []
    missing_docstrings = 0

    for node in ast.walk(tree):

        if isinstance(node, ast.FunctionDef):
            functions.append(node.name)

            if ast.get_docstring(node) is None:
                missing_docstrings += 1

        elif isinstance(node, ast.ClassDef):
            classes.append(node.name)

    lines = len(source.split("\n"))

    return {
        "functions": functions,
        "classes": classes,
        "lines": lines,
        "missing_docstrings": missing_docstrings
    }


def extract_functions(file_path):

    with open(file_path, "r") as f:
        source = f.read()

    tree = ast.parse(source)

    functions = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            functions.append(node.name)

    return functions


def get_docstring(file_path, func_name):

    with open(file_path, "r") as f:
        source = f.read()

    tree = ast.parse(source)

    for node in ast.walk(tree):

        if isinstance(node, ast.FunctionDef) and node.name == func_name:
            return ast.get_docstring(node)

    return None