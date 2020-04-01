import string

# s = (
#     """
#     Hi $name.
#
#     $contents
#
#     Have a good day
#     """
# )

# t = string.Template(s)


with open("design/text_template.txt") as f:
    t = string.Template(s)
contents = t.substitute(name="Mike", contents="How are you?")
print(contents)