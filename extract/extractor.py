# open the csv file and read the data

import os
import pandas as pd
import json

print('extractor.py running...')

# open data.csv with pandas (this was extracted using https://github.com/mdawsonuk/LevelDBDumper)
filename = './maps-in-cyberspace_packs_cybermaps_LevelDBDumper.csv'
data = pd.read_csv(filename)


# create the squares/ folder if it doesn't exist
if not os.path.exists('./squares'):
    os.makedirs('./squares')

values_to_map = ["drawings", "lights", "tiles", "walls",]
# map all the data values for later
for i, row in data.iterrows():
    key = row['Key']
    if '.' in key:
        continue
    value = json.loads(row['Value'])
    for v in values_to_map:
        if v in value:
            new_list = []
            for i in range(len(value[v])):
                id = value[v][i]

                # print("looking for id", id)
                target = data[data['Key'].str.contains(id)]
                if target.empty:
                    print('empty', id)
                    continue

                id_object = json.loads(target['Value'].values[0])
                print('found id', id, type(id_object))
                value[v][i] = id_object

    # print(json.dumps(value, indent=4))
    # exit()
    with open('./squares/' + key + '.json', 'w') as outfile:
        json.dump(value, outfile, indent=4)

print('done')
