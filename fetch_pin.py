import urllib.request
import re

url = 'https://pin.it/7451cdafT'
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    resp = urllib.request.urlopen(req)
    html = resp.read().decode('utf-8')
    match = re.search(r'\"og:image\"\s*content=\"([^\"]+)\"', html)
    if not match:
        match = re.search(r'content=\"([^\"]+\.jpg)\"', html)
        
    if match:
        img_url = match.group(1)
        print('IMAGE URL:', img_url)
        
        req_img = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req_img) as response, open(r'd:\Web_E-Bisnis\images\lampu_camping.jpg', 'wb') as out_file:
            data = response.read()
            out_file.write(data)
            
        print('Downloaded to images/lampu_camping.jpg')
    else:
        print('No og:image found')
except Exception as e:
    print('Error:', e)
