data = {"Meow": 1, "Wan": 999}


sorted_data = sorted(data, key=data.get, reverse=True)
print(data)
print(data.get)
print(sorted_data)

sorted_data_by_lambda = sorted(data.items(), key=lambda x:x[1], reverse=True)

print(dict(sorted_data_by_lambda))