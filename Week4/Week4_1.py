from fastapi import FastAPI, Request, Form
from starlette.middleware.sessions import SessionMiddleware
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from urllib.parse import quote

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key = "some-random-secret-key")
templates = Jinja2Templates(directory = "templates")
app.mount("/static", StaticFiles(directory = "static"), name = "static")

@app.get("/")
def read_root(request: Request):
    if request.session.get("SIGNED-IN", False):
        return RedirectResponse(url="/member", status_code = 303)
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/member")
def member_page(request: Request):
    if not request.session.get("SIGNED-IN", False):
        return RedirectResponse(url="/", status_code=303)
    return templates.TemplateResponse("member.html", {"request": request})

@app.get("/error")
def error_page(request: Request):
    message = request.query_params.get("message", "An unknown error occurred")
    return templates.TemplateResponse("signInFailed.html", {"request": request, "message": message})

@app.post("/signin")
def handle_login(request: Request, username: str = Form(None), password: str = Form(None)):
    if username == "test" and password == "test":
        request.session['SIGNED-IN'] = True
        return RedirectResponse(url="/member", status_code = 303)
    else:
        request.session.pop('SIGNED-IN', None)
        error_message = "帳號或密碼輸入錯誤"
        error_message_encoded = quote(error_message)
        return RedirectResponse(url = f"/error?message={error_message_encoded}", status_code = 303)

@app.get("/signout")
def handle_signout(request: Request):
    request.session['SIGNED-IN'] = False
    return RedirectResponse(url = "/", status_code = 303)
