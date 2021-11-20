# Date: 11/20/2021
# Author: Yousaf K Hamza
# Description: Instagram DP Downloader with URL

import requests
import json
import base64
import os

# URL Spliting.
insta_username= input('Instagram Profile_URL/UserName: ')
if insta_username.startswith("http"):
    if insta_username.endswith("/"):
        insta_username=insta_username.split(".com/")[1][:-1]
    elif insta_username.endswith("link"):
        insta_username=insta_username.split(".com/")[1].split("?")[0]
    else:
        insta_username=insta_username=insta_username.split(".com/")[1]
# Downloading path creation
if not os.path.exists("./dp"):
    os.makedirs("./dp")

# URL Imgbb API
key_imgbb="ab6f158359d0a96a54476b63d3529d31"
insta_url='https://www.instagram.com'
response = requests.get(f"{insta_url}/{insta_username}/?__a=1")

# Main 
if response.ok:
    json_data = json.loads(response.text)
    profile_pic_url=json_data["graphql"]["user"]["profile_pic_url_hd"]
    r = requests.get(profile_pic_url, allow_redirects=True)
    print("Image Downloaded under dp Directory!")
    open(f"./dp/{insta_username}.jpeg", 'wb').write(r.content)
    print("Image URL Generating.....")
    with open(f"./dp/{insta_username}.jpeg", "rb") as file:
        url = "https://api.imgbb.com/1/upload"
        payload = {
            "key": key_imgbb,
            "image": base64.b64encode(file.read()),
            }
        r = requests.post(url, data= payload)
        view_url=(json.loads(r.text)["data"]["display_url"])
        print("Image URL is: "+view_url)
else:
    print("UserName/Profile URL isn't correct...")
