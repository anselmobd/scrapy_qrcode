import jmespath
import json
import os
import pathlib
import requests
import shutil
import subprocess
import urllib.request
from pprint import pprint


def download_file(url, subdirs=None, filename=None, force=False):
    if subdirs:
        if not isinstance(subdirs, (list, tuple)):
            subdirs = [subdirs]
        subdir = os.path.join(*subdirs)
        os.makedirs(subdir, exist_ok=True)
    else:
        subdir = ''

    url_name, url_ext = os.path.splitext(pathlib.Path(url).name)

    name, ext = '', ''
    if filename:
        filename = str(filename)
        name, ext = os.path.splitext(filename)

    if not name:
        name = url_name
    if not ext:
        ext = url_ext
    filename = name + ext

    fullname = os.path.join(subdir, filename)

    if force or not os.path.exists(fullname):
        print(f'Downloading {url} to {fullname}')

        # result = requests.get(url, stream=True)
        # print(f"{result.status_code=}")
        # if result.status_code == 200:
        #     with open(fullname, 'wb') as out_file:
        #         result.raw.decode_content = True
        #         shutil.copyfileobj(result.raw, out_file)

        with (
            urllib.request.urlopen(url) as response,
            open(fullname, 'wb') as out_file
        ):
            shutil.copyfileobj(response, out_file)

        # cmd = f"curl {url} > {fullname}"
        # subprocess.run(cmd, shell=True, check=True)


# curl https://www.freepik.com/free-photos-vectors/qrcode > qrcode.html
# download_file(
#     "https://www.freepik.com/free-photos-vectors/qrcode/3",
#     filename="qrcode3.json")

dados = json.load(open("qrcode.json"))

urls = jmespath.search('props.pageProps.items[*].preview.url', dados)
print(len(urls))
# pprint(urls)


for url in urls:
    download_file(url, ['images', '2'])
