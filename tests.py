from functions.get_files_info import get_files_info

current_directory = get_files_info("calculator", ".")
print(f"Result for current directory: {current_directory}")

pkg_directory = get_files_info("calculator", "pkg")
print(f"Result for 'pkg' directory: {pkg_directory}")

bin_directory = get_files_info("calculator", "/bin")
print(f"Result for '/bin' directory: {bin_directory}")

outside_directory = get_files_info("calculator", "../")
print(f"Result for '../' directory: {outside_directory}")


        
