def convert_hash_to_array(h:dict):
    h_sorted = dict(sorted(h.items()))
    return [[key, value] for key, value in zip(h_sorted.keys(), h_sorted.values())]

print(convert_hash_to_array({"name": "Jeremy", "age": 24, "role": "Software Engineer"}))
