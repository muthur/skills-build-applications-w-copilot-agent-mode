from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from octofit_tracker.test_data import test_users, test_teams, test_activities, test_leaderboard, test_workouts

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Populate Users
        for user_data in test_users:
            User.objects.update_or_create(id=user_data['id'], defaults=user_data)

        # Populate Teams
        for team_data in test_teams:
            Team.objects.update_or_create(id=team_data['id'], defaults=team_data)

        # Populate Activities
        for activity_data in test_activities:
            Activity.objects.update_or_create(id=activity_data['id'], defaults=activity_data)

        # Populate Leaderboard
        for leaderboard_data in test_leaderboard:
            Leaderboard.objects.update_or_create(id=leaderboard_data['id'], defaults=leaderboard_data)

        # Populate Workouts
        for workout_data in test_workouts:
            Workout.objects.update_or_create(id=workout_data['id'], defaults=workout_data)

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
