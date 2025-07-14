from fastapi import FastAPI
from supabase import create_client
from fastapi.responses import RedirectResponse
import random
import string
from starlette.requests import Request
from fastapi.responses import PlainTextResponse

url = ("https://ipdmueraulauiyhxxkhp.supabase.co")

api = ("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlwZG11ZXJhdWxhdWl5aHh4a2hwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTAzNDc5MzQsImV4cCI6MjA2NTkyMzkzNH0.cI3E0jTkZg3P7muKNlLWsYxxmlCzx-dTuiRGqoPYldg")

db = create_client(url, api)

app = FastAPI(
    title = "URL shortner",
    description= "This is used to shorten large URL's"
)



def create_short(length):
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return random_string
    
# @app.post("/post")
# def post(long):
#     shorter = create_short(5)
#     result = db.table("url").insert({"long": long, "short": shorter}).execute()
#     return "https://url-backend-six.vercel.app/"+ result.data[0]['short']
    
    
@app.post("/post")
def post(long: str, request: Request):
    shorter = create_short(5)
    db.table("url").insert({"long": long, "short": shorter}).execute()
    return f"https://url-backend-six.vercel.app/{shorter}"
    
    
     
@app.get("/{short}")
def get(short):
    result = db.table("url").select("long").eq("short", short).execute()
    return RedirectResponse(result.data[0]['long'])

@app.get("/get", response_class=PlainTextResponse)
def get_sample():
    return "This is working fine!!"