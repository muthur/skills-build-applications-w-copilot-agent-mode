test_users = [
    {"id": 1, "username": "thundergod", "email": "thundergod@mhigh.edu", "password": "thundergodpassword"},
    {"id": 2, "username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "metalgeekpassword"},
    {"id": 3, "username": "zerocool", "email": "zerocool@mhigh.edu", "password": "zerocoolpassword"},
    {"id": 4, "username": "crashoverride", "email": "crashoverride@hmhigh.edu", "password": "crashoverridepassword"},
    {"id": 5, "username": "sleeptoken", "email": "sleeptoken@mhigh.edu", "password": "sleeptokenpassword"},
]

test_teams = [
    {"id": 1, "name": "Avengers", "members": [1, 2]},
    {"id": 2, "name": "Hackers", "members": [3, 4]},
    {"id": 3, "name": "Sleepwalkers", "members": [5]},
]

test_activities = [
    {"id": 1, "user_id": 1, "type": "Running", "duration": 30, "date": "2025-04-01"},
    {"id": 2, "user_id": 2, "type": "Cycling", "duration": 45, "date": "2025-04-02"},
]

test_leaderboard = [
    {"id": 1, "user_id": 1, "score": 100},
    {"id": 2, "user_id": 2, "score": 80},
]

test_workouts = [
    {"id": 1, "name": "Morning Run", "description": "A quick 5km run to start the day."},
    {"id": 2, "name": "Evening Yoga", "description": "Relaxing yoga session to end the day."},
]
