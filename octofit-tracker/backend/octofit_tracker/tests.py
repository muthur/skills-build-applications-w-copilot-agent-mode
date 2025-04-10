from rest_framework.test import APITestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserTests(APITestCase):
    def test_create_user(self):
        user = User.objects.create(email="test@example.com", name="Test User", age=25)
        self.assertEqual(user.email, "test@example.com")

class TeamTests(APITestCase):
    def test_create_team(self):
        team = Team.objects.create(name="Test Team")
        self.assertEqual(team.name, "Test Team")

class ActivityTests(APITestCase):
    def test_create_activity(self):
        user = User.objects.create(email="test@example.com", name="Test User", age=25)
        activity = Activity.objects.create(user=user, type="Running", duration=30)
        self.assertEqual(activity.type, "Running")

class LeaderboardTests(APITestCase):
    def test_create_leaderboard_entry(self):
        user = User.objects.create(email="test@example.com", name="Test User", age=25)
        leaderboard = Leaderboard.objects.create(user=user, score=100)
        self.assertEqual(leaderboard.score, 100)

class WorkoutTests(APITestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name="Test Workout", description="Test Description")
        self.assertEqual(workout.name, "Test Workout")
