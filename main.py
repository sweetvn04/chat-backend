from fastapi import FastAPI
from pydantic import BaseModel
from google import genai
from fastapi.middleware.cors import CORSMiddleware # solve cors issue
from google.genai import types

client = genai.Client(api_key="AIzaSyDln0H0aJcSyTcoC_JwZNsbffSQDdoQDd0")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel): # need a ChatRequest class that based on BaseMode to json can read
    message: str # the name of attribute 'message' must be match with the json object {message: input}
    # because fastapi will look the data for this attribute named 'message'



@app.get("/")
def root():
    return {"status" : "server is running!"}

@app.post("/chat")
def chat(request: ChatRequest):
    # when it recieved a json data like {'message: input'} from frontend.
    # It see the json has a key is 'message' and it will check the ChatRequest class that also need 'message'
    # then it check if input is a 'str'. if everything is matched, fastapi will translate this json file to python object that we can use
    
    # return {"reply": "I recieved " + request.message} # it is a python object that called dictionary.
    
    # it looks like exactly json format but it's a python object
    # when we return it, fastapi will automatic translate it to a plain json likes using JSON.stringify().
    # in the frontend, cuz we use headers is applicaion/json. fastapi will attaches exactly same headers to reply
    # so we will extract this with response.json()
        
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=types.Part.from_text(text=request.message),
        config=types.GenerateContentConfig(
            temperature=0,
            top_p=0.95,
            top_k=20,
        ),
    )
    
    return {"reply": response.text}


