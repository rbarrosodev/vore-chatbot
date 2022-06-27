import json

x = {
    "type": "image",
    "text": "Hello with image",
    "metadata": {
        "src": "http://www.tiledesk.com/logo.jpg",
        "width": "200",
        "height": "200"
    }
}

x = json.dumps(x)
print(x)
