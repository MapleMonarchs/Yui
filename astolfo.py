############################################################################################################################
# astolfo.py - ein Skript zum Herunterladen von Astolfo-Rule34 von rule34.xxx
#
# BGI says Trans Rights!
# (c) 2022 by Fake
############################################################################################################################

import random
import sys
import os
import requests
import shutil

############################################################################################################################


def downloadImage(url):  # wir öffnen die URL und schreiben die Daten in eine Datei
    file = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        with open(file, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

############################################################################################################################


tag = "astolfo_(fate)"  # wonach wollen wir suchen?
postNum = 1  # wie viele Bilder wollen wir?

# flags:
doDownload = True

############################################################################################################################

if __name__ == '__main__':

    for i, arg in enumerate(sys.argv):
        if arg == "-n" or arg == "--noImage":
            doDownload = False
        if arg == "-t" or arg == "--tag":
            tag = sys.argv[i + 1]
        if arg == "-h" or arg == "--help":
            print("""astolfo.py - download stuff from rule34.xxx
                  
options:
                  
-n, --noImage --> surpresses the download of images
                    
-t <para>, --tag <para> --> changes the search tag to the value given in <para>""")

            sys.exit(0)

    numRq = requests.get(
        f"https://api.rule34.xxx/index.php?page=dapi&s=post&q=index&tags={tag}&json=1")
    numPosts = len(numRq.json())

    pageNum = random.randint(0, numPosts - 1)

    print(f"number o. Posts: {numPosts}, PostNum: {pageNum}")

    post = requests.get(
        f"https://api.rule34.xxx/index.php?page=dapi&s=post&q=index&limit={postNum}&pid={pageNum}&tags={tag}&json=1")

    print(post.json()[0]['tags'])

    if(doDownload):
        # wir laden die Datei an der URL, die uns die API gegeben hat, herunter
        downloadImage(post.json()[0]['file_url'])

    sys.exit(0)
