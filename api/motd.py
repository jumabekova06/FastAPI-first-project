import fastapi

router = fastapi.APIRouter()

@router.get('/api/motd')

def message():
    return {
    'message': "Hello FastAPI!"
    }