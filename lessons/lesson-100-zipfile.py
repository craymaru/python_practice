import glob
import zipfile

with zipfile.Zip("test.zip", "w") as z:
    z.write("test_dir")
    z.write("test_dir/test.txt")

with zipfile.Zip("test.zip", "w") as z:
    for f in glob.glob("test_dir/**", recursive=True):
        print(f)
        z.write(f)

with zipfile.Zipfile("test.zip", "r") as z:
    z.extractall("z2")


with zipfile.Zipfile("test.zip", "r") as z:
    with z.open("test_dir/test.txt") as f:
        print(f.read())
