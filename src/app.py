"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    # Novas atividades relacionadas a esportes
    "Basketball Team": {
        "description": "Join the basketball team and compete in local tournaments",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 6:00 PM",
        "max_participants": 15,
        "participants": []
    },
    "Swimming Club": {
        "description": "Improve your swimming skills and participate in competitions",
        "schedule": "Mondays and Wednesdays, 5:00 PM - 6:30 PM",
        "max_participants": 20,
        "participants": []
    },
    # Novas atividades artísticas
    "Drama Club": {
        "description": "Explore acting and stage performance in a creative environment",
        "schedule": "Wednesdays, 3:00 PM - 5:00 PM",
        "max_participants": 25,
        "participants": []
    },
    "Painting Workshop": {
        "description": "Learn painting techniques and create your own masterpieces",
        "schedule": "Fridays, 2:00 PM - 4:00 PM",
        "max_participants": 15,
        "participants": []
    },
    # Novas atividades intelectuais
    "Math Club": {
        "description": "Solve challenging math problems and prepare for competitions",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 10,
        "participants": []
    },
    "Science Club": {
        "description": "Conduct experiments and explore scientific concepts",
        "schedule": "Mondays, 4:00 PM - 5:30 PM",
        "max_participants": 12,
        "participants": []
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    # Verificar se a atividade existe
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Obter os detalhes da atividade
    activity = activities[activity_name]

    # Verificar se o e-mail já está registrado
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Student is already signed up")

    # Adicionar o participante
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}
