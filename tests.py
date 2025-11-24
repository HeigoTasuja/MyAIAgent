from functions.get_files_info import write_file, run_python_file

def test():
    print("----- Testing write_file -----")
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(result)

    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(result)

    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(result)

    print("\n----- Testing run_python_file -----")
    print(f"Test 1 (main.py): {run_python_file('calculator', 'main.py')}")
    print(f"Test 2 (main.py args): {run_python_file('calculator', 'main.py', ['3 + 5'])}")
    print(f"Test 3 (tests.py): {run_python_file('calculator', 'tests.py')}")
    print(f"Test 4 (../main.py): {run_python_file('calculator', '../main.py')}")
    print(f"Test 5 (nonexistent): {run_python_file('calculator', 'nonexistent.py')}")
    print(f"Test 6 (lorem.txt): {run_python_file('calculator', 'lorem.txt')}")

if __name__ == "__main__":
    test()