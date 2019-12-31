import os
import requests

r = requests.get("https://www.baidu.com")
os.makedirs('production', exist_ok=True)
with open('./production/result.txt', 'w+') as wf:
    wf.write(f'{r.status_code}\n{r.encoding}')