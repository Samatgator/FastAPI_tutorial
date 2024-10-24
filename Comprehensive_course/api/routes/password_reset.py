from fastapi import APIRouter, HTTPException, status
from ..schemas import PasswordReset, db
from ..oath2 import create_access_token


router = APIRouter(
    prefix="/password",
    tags=["Password reset"]
)


@router.post("", response_description="Reset password")
async def reset_request(user_email: PasswordReset):
    user = await db["users"].find_one({"email": user_email.email})

    if user is not None:
        token = create_access_token({"id": str(user["_id"])})

        reset_link = f"http://localhost:8000/?token={token}"
        # TODO: send email

    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User with this email not found"
        )