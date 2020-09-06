import urllib

for i in range(0, 2000):
    print str(i)
    urllib.urlretrieve("https://objectif2k30.webflow.io/", filename="index.html")

