import os


def open_relative(path, flag="r"):
    relative_path = os.path.join(os.path.dirname(__file__), path)

    return open(relative_path, flag)
