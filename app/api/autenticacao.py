from fastapi import APIRouter

router = APIRouter(prefix='/autenticacao', tags=['autenticação'])

@router.post('/usuario')
def autenticacao():
    return {'m': 'funciona'}