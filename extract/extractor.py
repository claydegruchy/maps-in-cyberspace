# open the csv file and read the data

import os
import pandas as pd
import json


# open data.csv with pandas (this was extracted using https://github.com/mdawsonuk/LevelDBDumper)
filename = './maps-in-cyberspace_packs_cybermaps_LevelDBDumper.csv'
data = pd.read_csv(filename)

# json  parse 'value' column
data['Value'] = data['Value'].apply(json.loads)

# create the squares/ folder if it doesn't exist
if not os.path.exists('./squares'):
    os.makedirs('./squares')


def mapper(kind, id):
    for index, row in data.iterrows():
        v = row['Value']
        k = row['Key']
        if kind in k:
            print(k)
            return k


# iterate over the rows and print the value, but only where key cotnains YES

# add columns for id, parent, kind
columns = ['id', 'parent', 'kind']
for col in columns:
    if col not in data.columns:
        data[col] = ""

# if parsed_data.csv exists, dont do this
if not os.path.exists('./parsed_data.csv'):

    # map all the data values for later
    for i, row in data.iterrows():
        v = row['Value']
        k = row['Key']

        ids = k.split('!')[2]
        if '.' not in ids:
            id = ids
            parent = None
        else:
            id = ids.split('.')[1]
            parent = ids.split('.')[0]

        kind = k.split('!')[1]

        if '.' not in kind:
            kind = 'scenes'
        else:
            kind = kind.split('.')[1]

        data.at[i, 'parent'] = parent
        data.at[i, 'kind'] = kind
        data.at[i, 'id'] = id

        # print(row['id'], row['parent'], row['kind'])

# save the data to a new csv file
    data['Values'] = data.apply(lambda x: print(x['Values']), axis=1)

    data.to_csv('parsed_data.csv', encoding='utf-8', index=False)
data = pd.read_csv('parsed_data.csv')

# print(data)
parents = data[data['parent'].isnull()]

kinds = data['kind'].unique()
# remove scenes
kinds = [x for x in kinds if x != 'scenes']
print(kinds)
for i, row in parents.iterrows():
    obj = row['Value']
    # print(type(obj))
    # for kind in kinds:
    #     print(obj[kind])
    #     exit()


# if kind=='scenes':

# id  =

# if 'width' not in v or 'height' not in v or v['width'] != v['height']:
# continue

# create a new file in the squares/ folder, containing the value and name of the row
# with open('./squares/' + str(row['Key']) + '.json', 'w') as outfile:
# json.dump(v, outfile, indent=4)
