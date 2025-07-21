from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

# get_file_content tests:

print(get_file_content("calculator", "main.py"))
print(get_file_content("calculator", "pkg/calculator.py"))
print(get_file_content("calculator", "/bin/cat"))
print(get_file_content("calculator", "pkg/does_not_exist.py"))

# get_files_info tests:

# current_directory = get_files_info("calculator", ".")
# print(f"Result for current directory: {current_directory}")

# pkg_directory = get_files_info("calculator", "pkg")
# print(f"Result for 'pkg' directory: {pkg_directory}")

# bin_directory = get_files_info("calculator", "/bin")
# print(f"Result for '/bin' directory: {bin_directory}")

# outside_directory = get_files_info("calculator", "../")
# print(f"Result for '../' directory: {outside_directory}")

