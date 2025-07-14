import requests

def post(long):
    response = requests.post(f"http://localhost:8000/post?long={long}") 
    return response.json()
    
def get(short):
    response = requests.get(f"http://localhost:8000/{short}")
    return response.json()
