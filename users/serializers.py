from rest_framework import serializers

from teams.models import Team
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'team_name','password', 'role', 'last_login', 'total_time_spent']
        read_only_fields = ['last_login', 'total_time_spent']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        team_name = validated_data.pop('team_name')
        height = validated_data.pop('height', None)

        try:
            team = Team.objects.get(team_name=team_name)
            validated_data['team'] = team
        except Team.DoesNotExist:
            raise serializers.ValidationError("Team with this name does not exist.")
        
        role = validated_data.get('role')
        if role == 'player':
            if height is None:
                raise serializers.ValidationError("Height is required for player.")
            validated_data['height'] = height

        user = super().create(validated_data)
        return user