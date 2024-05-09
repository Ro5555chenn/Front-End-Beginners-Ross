from fastapi import FastAPI, Request, Form 
from fastapi.responses import RedirectResponse  
from fastapi.staticfiles import StaticFiles 
from fastapi.templating import Jinja2Templates
from urllib.parse import quote
from starlette.middleware.sessions import SessionMiddleware 
import mysql.connector

app = FastAPI()  
app.add_middleware(SessionMiddleware, secret_key="some-random-secret-key") 
templates = Jinja2Templates(directory="templates") 
app.mount("/static", StaticFiles(directory="static"), name="static")  

@app.get("/")
def home_page(request: Request):
    if request.session.get("SIGNED-IN", False):  
        return RedirectResponse(url="/member", status_code=303) 
    return templates.TemplateResponse("index.html", {"request": request})

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="website"
    )


@app.post("/signup")
async def signup(request: Request, signUpName: str = Form(...), signUpUsername: str = Form(...), signUpPassword: str = Form(...)):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM member WHERE username = %s", (signUpUsername))
    user_exists = cursor.fetchone()
    if user_exists:
        db.close()
        return templates.TemplateResponse("signUpFailed.html", {"request": request, "message": "用戶名已經存在"})
    else:
        cursor.execute("INSERT INTO member (name, username, password) VALUES (%s, %s, %s)", (signUpName, signUpUsername, signUpPassword))
        db.commit()
        db.close()
        return RedirectResponse(url="/", status_code=303)

@app.get("/error")  
def error_page(request: Request): 
    message = request.query_params.get("message", "An unknown error occurred")
    return templates.TemplateResponse("signInFailed.html", {"request": request, "message": message})

@app.post("/signin")
async def signin(request: Request, logInUsername: str = Form(...), logInPassword: str = Form(...)):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT id, name FROM member WHERE username=%s AND password=%s", (logInUsername, logInPassword))
    user = cursor.fetchone()
    db.close()
    if user:
        request.session['SIGNED-IN'] = True
        request.session['USER_ID'] = user[0]
        request.session['USER_NAME'] = user[1] 
        return RedirectResponse(url="/member", status_code=303)
    else:
        request.session.pop('SIGNED-IN', None)
        request.session.pop('USER_ID', None) 
        request.session.pop('USER_NAME', None)
        error_message = "帳號或密碼輸入錯誤"
        error_message_encoded = quote(error_message)
        return RedirectResponse(url=f"/error?message={error_message_encoded}", status_code=303)
    

@app.get("/member")  
def member_page(request: Request):
    if not request.session.get("SIGNED-IN", False):
        return RedirectResponse(url="/", status_code=303)
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("""
        SELECT member.name, message.content
        FROM message 
        JOIN member ON message.member_id = member.id 
        ORDER BY message.time DESC
    """)
    messages = cursor.fetchall()
    db.close()
    user_id = request.session.get("USER_ID")
    user_name = request.session.get("USER_NAME", "Unknown User")
    return templates.TemplateResponse("member.html", {"request": request, "messages": messages, "user_name": user_name, "user_id": user_id})


@app.post("/createMessage")
def create_message(request: Request, content: str = Form(...)):
    if not request.session.get("SIGNED-IN"):
        return RedirectResponse(url="/", status_code=303)
    member_id = request.session.get("USER_ID")
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("INSERT INTO message (member_id, content) VALUES (%s, %s)", (member_id, content))
    db.commit()
    db.close()
    return RedirectResponse(url="/member", status_code=303)



@app.get("/signout")  
def handle_signout(request: Request):   
    request.session['SIGNED-IN'] = False 
    return RedirectResponse(url="/", status_code=303)
