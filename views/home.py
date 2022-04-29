import fastapi
from starlette.requests import Request
from starlette.templating import Jinja2Templates
from typing import Optional
from services import digital_ocean_service

secret: Optional[str] = None

router = fastapi.APIRouter()
templates = Jinja2Templates('templates')

@router.get('/')
async def home(request: Request):
    droplet_images = await digital_ocean_service.get_droplet_images_async()
    return templates.TemplateResponse('home.html', {'request': request,
    'display_secret': secret, 'droplet_images': droplet_images})