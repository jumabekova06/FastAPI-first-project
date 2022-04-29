import fastapi
from services import digital_ocean_service

router = fastapi.APIRouter()

@router.get('/api/droplet_images')
async def images():
    return await digital_ocean_service.get_droplet_images_async()