from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_credentials=True,
)


@app.get("/api")
def student_info():
    response = {
        "data": {
            "email": "ik.ugwuanyi@gmail.com",
            "current_datetime": datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "github_url": "https://github.com/iConnell/hgnX",
        },
        "status_code": 200,
    }

    return response
