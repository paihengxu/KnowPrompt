import os
import json


for fn in ['train.txt', 'test.txt', 'val.txt']:
    with open(os.path.join('../semeval', fn), 'r') as inf, open(fn, 'w') as outf:
        for line in inf:
            data = json.loads(line.strip())
            if data['relation'] != 'Cause-Effect(e2,e1)' and data['relation'] != 'Cause-Effect(e1,e2)':
                data['relation'] = 'Other'
            outf.write(f"{json.dumps(data)}\n")
