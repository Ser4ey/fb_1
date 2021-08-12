import requests
import time

# url = 'https://scontent-arn2-1.xx.fbcdn.net/v/t39.35426-6/s600x600/232471424_171481891717950_6457784168100507472_n.jpg?_nc_cat=110&ccb=1-4&_nc_sid=cf96c8&_nc_ohc=_USpPBKcZCEAX8wkoq6&_nc_ht=scontent-arn2-1.xx&oh=f67dfb1e2b0b95e67dd660a69079f390&oe=611A5666'
# r = requests.get(url)
#
# # jpg mp4
# name = str(time.time())
# print(name)
#
# with open(f'media/{name}.jpg', 'wb') as f:
#     f.write(r.content)
def save_video( url):
    if url == '':
        return ''

    r = requests.get(url)
    name = str(time.time()) + '.mp4'
    path_to_file = 'media/' + name

    with open(path_to_file, 'wb') as f:
        f.write(r.content)


save_video('https://video-arn2-1.xx.fbcdn.net/v/t42.1790-2/235048634_510424603395999_557249510419474097_n.?_nc_cat=109&ccb=1-4&_nc_sid=cf96c8&_nc_ohc=znYiiJy0_aEAX90ahs5&_nc_ht=video-arn2-1.xx&oh=372dc44c089e1c7431602fa590d0fdb6&oe=61152DF4')