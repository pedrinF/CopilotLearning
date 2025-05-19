from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "name")
    search_fields = ("email", "name")

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ("user_email", "activity_type", "duration")
    search_fields = ("user_email", "activity_type")

@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ("user_email", "score")
    search_fields = ("user_email",)

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
