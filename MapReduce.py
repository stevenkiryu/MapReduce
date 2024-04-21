import pandas as pd

data_item = pd.read_csv("f3d59ad63d49f7847d967b49b35701b6.csv")

List_item = [tuple(row) for index, row in data_item.iterrows()]

# Mapping the Item
def mapper(item):
    word, count = item
    result = [(word,1)]
    return result

intermediate_data = []
for item in List_item:
    intermediate_data.extend(mapper(item))

# Shuffle & Sort Item
sorted_intermediate_data = sorted(intermediate_data, key=lambda x: x[0])

# Reduce Item
def reducer(values):
    return sum(values)

final_output = {}
for word, count in intermediate_data:
    if word not in final_output:
        final_output[word] = []
    final_output[word].append(count)

# Result Item

print("Tuples format")
result = [(key, reducer(values)) for key,values in final_output.items()]

for item in result:
    print(item)

print()
print("String format")
print()

for key,values in final_output.items():
    print(key , "have" , reducer(values) , "item")