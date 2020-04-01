s = ("""
AAA
BBB
CCC
DDD
""")

# with open ("text.txt", "w") as f:
#     f.write(s)

# with open ("text,txt", "r") as f:
#     # print(f.read())
#     # while True:
#     #     chunk = 5
#     #     line = f.readline(chunk)
#     #     print(line)
#     #     if not line:
#     #         break
#
#     print(f.tell())
#     print(f.read(1))

with open ("text.txt", "r+") as f:
    print(f.read())
    f.seek(0)
    f.write(s)
    pass