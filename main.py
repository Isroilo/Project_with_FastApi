from fastapi import FastAPI, Body, Depends

from app.models import Blog, User, UserLogin
from app.auth.auth_bearer import JWTBearer
from app.auth.auth_handler import signJWT

blogs = [
    {
        "id": 1,
        "title": "Penguins ",
        "text": "Penguins are a group of aquatic flightless birds."
    },
    {
        "id": 2,
        "title": "Tigers ",
        "text": "Tigers are the largest living cat species and a memeber of the genus panthera."
    },
    {
        "id": 3,
        "title": "Koalas ",
        "text": "Koala is arboreal herbivorous maruspial native to Australia."
    },
]

users = []

app = FastAPI()

""" this is login required"""
def check_user(data: UserLogin):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False


# Get blogs
@app.get("/blogs", dependencies=[Depends(JWTBearer())],  tags=["blogs"])
def get_posts():
    return { "data": blogs }


#Get single blog by id
@app.get("/blogs/{id}", dependencies=[Depends(JWTBearer())], tags=["blogs"])
def get_single_post(id: int):
    if id > len(blogs):
        return {
            "error": "No such post with the supplied ID."
        }

    for blog in blogs:
        if blog["id"] == id:
            return {
                "data": blog
            }

#Create new  blog
@app.post("/blog-create", dependencies=[Depends(JWTBearer())], tags=["blogs"])
def add_post(blog: Blog):
    blog.id = len(blogs) + 1
    blogs.append(blog.dict())
    return {
        "data": "blog create succesfull"
    }


@app.post("/user/signup", tags=["user"])
def create_user(user: User = Body(...)):
    users.append(user) # replace with db call, making sure to hash the password first
    return signJWT(user.email)


@app.post("/user/login", tags=["user"])
def user_login(user: UserLogin = Body(...)):
    if check_user(user):
        return signJWT(user.email)
    return {
        "error": "Wrong login details!"
    }