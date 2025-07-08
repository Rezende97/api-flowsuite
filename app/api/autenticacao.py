from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
# from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.drivers.database import get_db_session
from app.use_cases.user_use_cases import UserUseCases
from app.schemas.user_schema import UserSchemas

router = APIRouter(prefix='/autenticacao', tags=['autenticação'])

@router.post('/usuario')
def user_register(
    user: UserSchemas,
    db_session: Session = Depends(get_db_session),
):
    use_case = UserUseCases(db_session=db_session)
    use_case.user_register(user=user)
    return JSONResponse(
        content={'msg': 'success'},
        status_code=status.HTTP_201_CREATED
    )
