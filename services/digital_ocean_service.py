from typing import Optional
import httpx

do_api_token: Optional[str] = 'MyTopSecretToken'

async def get_droplet_images_async():
    url = f'http://127.0.0.1:8000/api/v1/test.png' #здесь есть такой словарь как 'images': "любая ссылка на фотку"
    url_headers = {'Authorization': 'Bearer ' + do_api_token}
    async with httpx.AsyncClient() as client:
        resp = await client.get(url, headers=url_headers)
    data = resp.json()
    droplet_images = data['images']
    return droplet_images