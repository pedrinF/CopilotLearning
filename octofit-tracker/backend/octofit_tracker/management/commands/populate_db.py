from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Test data for users
        users = [
            {'email': 'sarah@monahigh.edu', 'name': 'Sarah Johnson'},
            {'email': 'mike@monahigh.edu', 'name': 'Mike Anderson'},
            {'email': 'emma@monahigh.edu', 'name': 'Emma Wilson'},
            {'email': 'james@monahigh.edu', 'name': 'James Davis'}
        ]
        for user_data in users:
            User.objects.create(**user_data)

        # Test data for teams
        teams = [
            {'name': 'Track Stars', 'members': ['sarah@monahigh.edu', 'mike@monahigh.edu']},
            {'name': 'Fitness Warriors', 'members': ['emma@monahigh.edu', 'james@monahigh.edu']}
        ]
        for team_data in teams:
            Team.objects.create(**team_data)

        # Test data for activities
        activities = [
            {'user_email': 'sarah@monahigh.edu', 'activity_type': 'Running', 'duration': 45},
            {'user_email': 'mike@monahigh.edu', 'activity_type': 'Swimming', 'duration': 30},
            {'user_email': 'emma@monahigh.edu', 'activity_type': 'Cycling', 'duration': 60},
            {'user_email': 'james@monahigh.edu', 'activity_type': 'Basketball', 'duration': 40}
        ]
        for activity_data in activities:
            Activity.objects.create(**activity_data)

        # Test data for leaderboard
        leaderboard = [
            {'user_email': 'sarah@monahigh.edu', 'score': 150},
            {'user_email': 'mike@monahigh.edu', 'score': 120},
            {'user_email': 'emma@monahigh.edu', 'score': 180},
            {'user_email': 'james@monahigh.edu', 'score': 140}
        ]
        for score_data in leaderboard:
            Leaderboard.objects.create(**score_data)

        # Test data for workouts
        workouts = [
            {
                'name': 'Morning Cardio',
                'description': 'Start your day with a 30-minute cardio session including running and jumping jacks.'
            },
            {
                'name': 'Strength Training',
                'description': 'Full body workout focusing on major muscle groups with weights.'
            },
            {
                'name': 'Team Sports',
                'description': 'Group activities including basketball and volleyball.'
            },
            {
                'name': 'Swimming Session',
                'description': 'Pool workout with different strokes and endurance training.'
            }
        ]
        for workout_data in workouts:
            Workout.objects.create(**workout_data)

        self.stdout.write(self.style.SUCCESS('Successfully populated database with test data'))
