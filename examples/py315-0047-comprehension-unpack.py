lists = [[1, 2], [3, 4]]
flat = [*sub for sub in lists]
dicts = [{"a": 1}, {"b": 2}]
merged = {**d for d in dicts}
