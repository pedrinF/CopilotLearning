from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Test data for users
        User.objects.create(email='john.doe@example.com', name='John Doe')
        User.objects.create(email='jane.smith@example.com', name='Jane Smith')

        # Test data for teams
        Team.objects.create(name='Team Alpha', members=['john.doe@example.com', 'jane.smith@example.com'])

        # Test data for activities
        Activity.objects.create(user_email='john.doe@example.com', activity_type='Running', duration=30)
        Activity.objects.create(user_email='jane.smith@example.com', activity_type='Cycling', duration=45)

        # Test data for leaderboard
        Leaderboard.objects.create(user_email='john.doe@example.com', score=100)
        Leaderboard.objects.create(user_email='jane.smith@example.com', score=150)

        # Test data for workouts
        Workout.objects.create(name='Morning Yoga', description='A relaxing yoga session to start the day.')
        Workout.objects.create(name='HIIT', description='High-Intensity Interval Training for advanced users.')

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
