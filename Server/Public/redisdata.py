import redis
from utils import RedisMonitor
from utils import JsonUtil

p = RedisMonitor.name

host = '127.0.0.1'
port = 6379
pwd = ''

#print(p)

respo = RedisMonitor.new_request(host,port,pwd)
#print('Starting Output \n\n\n', respo['success'])
respo_data = dict(respo['data'])
#cache_data = {} 
#cache_data == respo_data

#for x in respo_data:
#    print(x + '  ===> ',respo_data[x])

#respo_data['os'] = 'Linux'

#js = JsonUtil.object_2_json(respo)
#print('Starting Output 2 \n\n\n', js[])

#print('\n\n\n\n\n', respo_data['os'])

'''def changedata(respo_data, cache_data):
    havechanged = {}
    
    for x in respo_data:
        if respo_data[x] != cache_data[x]:
            print('Data changed')
            cache_data[x] = respo_data[x]
            havechanged[x] = respo_data [x]
        else:
            print('###### No Data changed########')
    return havechanged

got_change = changedata(respo_data,cache_data)

print('\n\nDATA got Changed\n', got_change)
'''

with open('./Server/Public/testingjson.json','w') as json_file:
    JsonUtil.json.dump(respo_data, json_file)