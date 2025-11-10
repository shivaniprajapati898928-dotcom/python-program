# Create a Python program to rename, copy, and delete a file using the os module Ensure exception handling for file access errors

import os
import shutil  # for copying files safely

# Original file name (must exist in the same directory)
original_file = "example.txt"
renamed_file = "renamed_example.txt"
copied_file = "copied_example.txt"

try:
    # ✅ Rename file
    if os.path.exists(original_file):
        os.rename(original_file, renamed_file)
        print(f"File renamed successfully: {original_file} → {renamed_file}")
    else:
        raise FileNotFoundError(f"File '{original_file}' not found for renaming.")

    # ✅ Copy file
    if os.path.exists(renamed_file):
        shutil.copy(renamed_file, copied_file)
        print(f"File copied successfully: {renamed_file} → {copied_file}")
    else:
        raise FileNotFoundError(f"File '{renamed_file}' not found for copying.")

    # ✅ Delete file
    if os.path.exists(copied_file):
        os.remove(copied_file)
        print(f"File deleted successfully: {copied_file}")
    else:
        raise FileNotFoundError(f"File '{copied_file}' not found for deletion.")

except FileNotFoundError as e:
    print("Error:", e)
except PermissionError:
    print("Error: Permission denied while accessing the file.")
except Exception as e:
    print("Unexpected error:", e)
