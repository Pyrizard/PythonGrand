from requests import get  # to make GET request


def download(url, file_name):
        # open in binary mode
    with open(file_name, "wb") as file:
            # get request
        response = get(url)
            # write to file
        file.write(response.content)


download("http://d.wload.vc/files/sfd495/247141/Machine%20On%20-%20SMS%20Tone(WapKing).mp3","22221.mp3")