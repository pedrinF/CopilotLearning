from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer

class UserView(APIView):
    def get(self, request):
        return Response({"message": "User endpoint"})

class TeamView(APIView):
    def get(self, request):
        return Response({"message": "Team endpoint"})

class ActivityView(APIView):
    def get(self, request):
        return Response({"message": "Activity endpoint"})

class LeaderboardView(APIView):
    def get(self, request):
        return Response({"message": "Leaderboard endpoint"})

class WorkoutView(APIView):
    def get(self, request):
        return Response({"message": "Workout endpoint"})

def api_root(request):
    return Response({"message": "API Root"})