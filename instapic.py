import requests
import json
import base64
import os

insta_username= input('Instagram Profile_URL/UserName: ')
if insta_username.startswith("http"):
    if insta_username.endswith("/"):
        insta_username=insta_username.split(".com/")[1][:-1]
    elif insta_username.endswith("link"):
        insta_username=insta_username.split(".com/")[1].split("?")[0]
    else:
        insta_username=insta_username=insta_username.split(".com/")[1]

key_imgbb="ab6f158359d0a96a54476b63d3529d31"
insta_url='https://www.instagram.com'
response = requests.get(f"{insta_url}/{insta_username}/?__a=1")

if response.ok:
    json_data = json.loads(response.text)
    profile_pic_url=json_data["graphql"]["user"]["profile_pic_url_hd"]
    r = requests.get(profile_pic_url, allow_redirects=True)
    open(f"{insta_username}.jpeg", 'wb').write(r.content)
    print("Image URL Generating.....")
    with open(f"{insta_username}.jpeg", "rb") as file:
        url = "https://api.imgbb.com/1/upload"
        payload = {
            "key": key_imgbb,
            "image": base64.b64encode(file.read()),
            }
        r = requests.post(url, data= payload)
        view_url=(json.loads(r.text)["data"]["url_viewer"])
        os.remove(f"{insta_username}.jpeg")
        print("Image URL is: "+view_url)
else:
    print("Username/Profile URL isn't correct...")
