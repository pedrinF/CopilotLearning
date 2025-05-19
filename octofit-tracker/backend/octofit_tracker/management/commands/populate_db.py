
# --- Copilot Agent Mode ---
# Este script utiliza o modo agente do Copilot para popular o banco de dados com dados de teste.
# Cada etapa é registrada e explicada para facilitar a auditoria e depuração.

from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data using Copilot agent mode'

    def handle(self, *args, **kwargs):
        self.stdout.write("[Copilot Agent] Iniciando a população do banco de dados...")

        # Limpar dados existentes
        self.stdout.write("[Copilot Agent] Limpando dados antigos...")
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Usuários de teste
        self.stdout.write("[Copilot Agent] Adicionando usuários de teste...")
        users = [
            {'email': 'sarah@monahigh.edu', 'name': 'Sarah Johnson'},
            {'email': 'mike@monahigh.edu', 'name': 'Mike Anderson'},
            {'email': 'emma@monahigh.edu', 'name': 'Emma Wilson'},
            {'email': 'james@monahigh.edu', 'name': 'James Davis'},
            {'email': 'lucas@monahigh.edu', 'name': 'Lucas Silva'},
            {'email': 'maria@monahigh.edu', 'name': 'Maria Santos'},
            {'email': 'pedro@monahigh.edu', 'name': 'Pedro Oliveira'},
            {'email': 'ana@monahigh.edu', 'name': 'Ana Pereira'}
        ]
        for user_data in users:
            user = User.objects.create(**user_data)
            self.stdout.write(f"[Copilot Agent] Usuário criado: {user.name} ({user.email})")

        # Equipes de teste
        self.stdout.write("[Copilot Agent] Adicionando equipes de teste...")
        teams = [
            {
                'name': 'Track Stars',
                'members': ['sarah@monahigh.edu', 'mike@monahigh.edu', 'lucas@monahigh.edu']
            },
            {
                'name': 'Fitness Warriors',
                'members': ['emma@monahigh.edu', 'james@monahigh.edu', 'ana@monahigh.edu']
            },
            {
                'name': 'Power Squad',
                'members': ['pedro@monahigh.edu', 'maria@monahigh.edu']
            }
        ]
        for team_data in teams:
            team = Team.objects.create(**team_data)
            self.stdout.write(f"[Copilot Agent] Equipe criada: {team.name} (membros: {', '.join(team.members)})")

        # Atividades de teste
        self.stdout.write("[Copilot Agent] Adicionando atividades de teste...")
        activities = [
            {'user_email': 'sarah@monahigh.edu', 'activity_type': 'Running', 'duration': 45},
            {'user_email': 'mike@monahigh.edu', 'activity_type': 'Swimming', 'duration': 30},
            {'user_email': 'emma@monahigh.edu', 'activity_type': 'Cycling', 'duration': 60},
            {'user_email': 'james@monahigh.edu', 'activity_type': 'Basketball', 'duration': 40},
            {'user_email': 'lucas@monahigh.edu', 'activity_type': 'CrossFit', 'duration': 50},
            {'user_email': 'maria@monahigh.edu', 'activity_type': 'Yoga', 'duration': 75},
            {'user_email': 'pedro@monahigh.edu', 'activity_type': 'Weightlifting', 'duration': 55},
            {'user_email': 'ana@monahigh.edu', 'activity_type': 'Pilates', 'duration': 45},
            {'user_email': 'sarah@monahigh.edu', 'activity_type': 'Cycling', 'duration': 40},
            {'user_email': 'mike@monahigh.edu', 'activity_type': 'Running', 'duration': 35},
            {'user_email': 'emma@monahigh.edu', 'activity_type': 'Yoga', 'duration': 50},
            {'user_email': 'james@monahigh.edu', 'activity_type': 'Swimming', 'duration': 45}
        ]
        for activity_data in activities:
            activity = Activity.objects.create(**activity_data)
            self.stdout.write(f"[Copilot Agent] Atividade criada: {activity.activity_type} para {activity.user_email} ({activity.duration} min)")

        # Leaderboard de teste
        self.stdout.write("[Copilot Agent] Adicionando leaderboard de teste...")
        leaderboard = [
            {'user_email': 'sarah@monahigh.edu', 'score': 850},
            {'user_email': 'mike@monahigh.edu', 'score': 720},
            {'user_email': 'emma@monahigh.edu', 'score': 980},
            {'user_email': 'james@monahigh.edu', 'score': 840},
            {'user_email': 'lucas@monahigh.edu', 'score': 650},
            {'user_email': 'maria@monahigh.edu', 'score': 890},
            {'user_email': 'pedro@monahigh.edu', 'score': 760},
            {'user_email': 'ana@monahigh.edu', 'score': 920}
        ]
        for score_data in leaderboard:
            score = Leaderboard.objects.create(**score_data)
            self.stdout.write(f"[Copilot Agent] Leaderboard: {score.user_email} com {score.score} pontos")

        # Workouts de teste
        self.stdout.write("[Copilot Agent] Adicionando workouts de teste...")
        workouts = [
            {
                'name': 'Morning Cardio Blast',
                'description': 'Iniciar o dia com 30 minutos de cardio incluindo corrida, jumping jacks e burpees.'
            },
            {
                'name': 'Treino de Força Total',
                'description': 'Treino completo focando em grandes grupos musculares com pesos e exercícios compostos.'
            },
            {
                'name': 'Circuito HIIT',
                'description': 'Treino intervalado de alta intensidade com 8 exercícios em 4 rounds.'
            },
            {
                'name': 'Yoga Flow',
                'description': 'Sequência de yoga para melhorar flexibilidade e equilíbrio.'
            },
            {
                'name': 'Core Express',
                'description': 'Treino focado em abdômen e core com 15 exercícios em 30 minutos.'
            },
            {
                'name': 'Treino de Mobilidade',
                'description': 'Exercícios para melhorar amplitude de movimento e prevenir lesões.'
            }
        ]
        for workout_data in workouts:
            workout = Workout.objects.create(**workout_data)
            self.stdout.write(f"[Copilot Agent] Workout criado: {workout.name}")

        self.stdout.write(self.style.SUCCESS('[Copilot Agent] Banco de dados populado com sucesso!'))
