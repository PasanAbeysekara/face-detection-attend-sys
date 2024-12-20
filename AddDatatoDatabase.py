import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://attendace-system-56da1-default-rtdb.firebaseio.com"
})

ref = db.reference('Students')

data = {
    "321654":
        {
            "name": "Hugh Jackman",
            "major": "Robotics",
            "starting_year": 2017,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2024-11-17 00:54:34"
        },
    "852741":
        {
            "name": "Pasan Abeysekara",
            "major": "Economics",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2024-11-17 00:54:34"
        },
    "963852":
        {
            "name": "Rayn Renolds",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)
