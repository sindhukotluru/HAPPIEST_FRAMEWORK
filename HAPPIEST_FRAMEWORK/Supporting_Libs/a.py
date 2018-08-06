my_mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee}
print(my_mapping)
import json
print(json.dumps(my_mapping,  indent=10, sort_keys=False))
