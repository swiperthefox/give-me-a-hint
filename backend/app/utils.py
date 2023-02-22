from urllib.request import urlopen
def save_picture(p, dataurl):
    response = urlopen(dataurl)
    with open(p, 'wb') as f:
        f.write(response.read())