from fastapi import FastAPI


app = FastAPI()


@app.get("/") 
async def root(): 
      return {"message": "Sarmad Rafique API on vercel build with FastAPI!"}