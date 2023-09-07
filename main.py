from fastapi import FastAPI
from datetime import datetime

app = FastAPI()


@app.get("/api")
def student_info(track: str = "Backend", slack_name: str = "McConnell Ikechukwu"):
    data = {
        "slack_name": slack_name,
        "current_day": datetime.today().strftime("%A"),
        "utc_time": datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ'),
        "track": track,
        "github_file_url": "https://github.com/iConnell/hgnX/blob/master/main.py",
        "github_repo_url": "https://github.com/iConnell/hgnX",
        "status_code": 200,
    }
    
    return data
