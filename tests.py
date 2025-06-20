from functions.get_files_info import get_files_info, get_file_content


def test():
    result = get_file_content("calculator", "lorem.txt")
    print("Result for current directory:")
    print(result)
    print("")

    result = get_file_content("calculator", "main.py")
    print("Result for 'pkg' directory:")
    print(result)

    result = get_file_content("calculator", "pkg/calculator.py")
    print("Result for 'pkg/calculator' directory:")
    print(result)

    result = get_file_content("calculator", "bin/cat")
    print("Result for 'bin' directory:")
    print(result)


if __name__ == "__main__":
    test()
