import os
import pathlib
import glob
import shutil

print(os.path.exists("../sandbox/test.csv"))
print(os.path.isfile("../sandbox/test.csv"))
print(os.path.isdir("../sandbox/design"))


# os.rename("text.txt", "renamed.txt")
# os.symlink("renamed.txt", "symlink.txt")

# os.mkdir("test_dir")
# os.rmdir("test_dir")

# pathlib.Path("empty.txt").touch
# os.remove("empty.txt")

# os.mkdir("text_dir")
# os.mkdir("test_dir/test_dir2")
