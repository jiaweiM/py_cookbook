import random
import urllib.request


def download_web_img(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + ".png"
    urllib.request.urlretrieve(url, full_name)

download_web_img('http://www.bioinfor.com/wp-content/uploads/2017/03/falsediscoveryrate1-1.png')
