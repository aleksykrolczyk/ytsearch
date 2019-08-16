import requests
from bs4 import BeautifulSoup


def get_videos(query, n=9):

    base_url = 'https://m.youtube.com/results?search_query='
    page = requests.get(base_url + query)
    soup = BeautifulSoup(page.content, 'html.parser')
    divs = soup.select(
        'div.yt-lockup-dismissable:not(:has(ol.yt-lockup-playlist-items))')[:n]

    # example img url: https://i.ytimg.com/vi/dQw4w9WgXcQ/hqdefault.jpg
    # example video url: https://www.youtube.com/watch?v=dQw4w9WgXcQ

    videos = []
    for div in divs:
        ref = div.select('a.yt-uix-sessionlink.spf-link')
        video_id = ref[0].attrs['href'].split('=')[1]
        length = ref[0].text[2:]
        title = ref[1].text

        video = {
            'img_url': f'https://i.ytimg.com/vi/{video_id}/hqdefault.jpg',
            'video_url': f'https://www.youtube.com/watch?v={video_id}',
            'length': length,
            'title': title
        }

        videos.append(video)

    return videos
