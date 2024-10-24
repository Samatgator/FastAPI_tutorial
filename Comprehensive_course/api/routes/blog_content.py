from fastapi import APIRouter, Body, Depends, HTTPException, status
from ..schemas import BlogContent, BlogContentResponse,  db
from .. import oath2
from datetime import datetime, timezone

router = APIRouter(
    prefix="/blog",
    tags=["Blog Content"]
)


# TODO: CRUD

@router.post("", response_description="Create blog content", response_model=BlogContentResponse)
async def create_blog(blog_content: BlogContent = Body(...) , current_user=Depends(oath2.get_current_user)):
    
    print(blog_content)
    print(current_user)

    try:
        blog_content = blog_content.model_dump(by_alias=True, exclude=["id"])
        # add additional information
        blog_content["author_name"] = current_user["name"]
        blog_content["author_id"] = str(current_user["_id"])
        blog_content["created_at"] = str(datetime.now(timezone.utc))

        new_blog_content = await db["blogPost"].insert_one(blog_content)
        created_blog_post = await db["blogPost"].find_one({"_id": new_blog_content.inserted_id})

        return created_blog_post
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )
