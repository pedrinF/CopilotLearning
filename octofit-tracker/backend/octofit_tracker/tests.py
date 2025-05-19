from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(email="test@school.edu", name="Test User")
        self.assertEqual(user.email, "test@school.edu")
        self.assertEqual(user.name, "Test User")

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name="Test Team", members=["test@school.edu"])
        self.assertEqual(team.name, "Test Team")
        self.assertIn("test@school.edu", team.members)

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(user_email="test@school.edu", activity_type="Running", duration=30)
        self.assertEqual(activity.user_email, "test@school.edu")
        self.assertEqual(activity.activity_type, "Running")
        self.assertEqual(activity.duration, 30)

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        lb = Leaderboard.objects.create(user_email="test@school.edu", score=100)
        self.assertEqual(lb.user_email, "test@school.edu")
        self.assertEqual(lb.score, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name="Test Workout", description="Desc")
        self.assertEqual(workout.name, "Test Workout")
        self.assertEqual(workout.description, "Desc")
