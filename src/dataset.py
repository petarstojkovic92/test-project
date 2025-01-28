import pandas as pd

data = {
    "Name": ["John", "Anna", "Peter", "Linda"],
    "Age": [23, 34, 45, 56],
    "City": ["New York", "Paris", "Berlin", "London"],
}

df = pd.DataFrame(data)

df.head(2)
