import sys
import os


def test_rootDir0():
    project_dir = os.path.dirname(sys.argv[0])
    print(project_dir)
    print("====== project_dir:" + project_dir)
