from requests import get                        #to make GET request
import random


def download(url):
    name = random.randrange(1, 99999)
    file_name = str(name) + ".mp3"
    with open(file_name, "wb") as file:         # open in binary mode
        response = get(url)                     # get request
        file.write(response.content)            # write to file


download("https://dl.pagal.link/upload_file/5570/6757/Latest%20Bollywood%20Hindi%20Mp3%20Songs%20-%202017/Mom%20%282017%29%20Hindi%20Movie%20Mp3%20Songs/06%20Muafi%20Mushkil%20-%20MOM%20%28Darshana%20KT%29%20190Kbps.mp3")