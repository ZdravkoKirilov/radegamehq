from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from ..entities.Game import Game
from ..serializers.Game import GameSerializer

from ..serializers.Condition import ConditionSerializer
from ..serializers.Action import ActionSerializer
from ..serializers.Choice import ChoiceSerializer
from ..serializers.Faction import FactionSerializer
from ..serializers.Stage import StageSerializer
from ..serializers.Slot import SlotSerializer
from ..serializers.Path import MapPathSerializer
from ..serializers.Field import FieldSerializer
from ..serializers.Team import TeamSerializer
from ..serializers.Round import RoundSerializer
from ..serializers.Phase import PhaseSerializer
from ..serializers.Token import TokenSerializer
from ..serializers.Source import SourceSerializer
from ..serializers.ImageAsset import ImageAssetSerializer

from ..entities.Action import Action
from ..entities.Condition import Condition
from ..entities.Choice import Choice
from ..entities.Faction import Faction
from ..entities.Stage import Stage
from ..entities.Slot import Slot
from ..entities.Path import Path
from ..entities.Field import Field
from ..entities.Team import Team
from ..entities.Round import Round
from ..entities.Phase import Phase
from ..entities.Token import Token
from ..entities.Source import Source
from ..entities.ImageAsset import ImageAsset


class GameView(generics.ListCreateAPIView):
    serializer_class = GameSerializer

    ##permission_classes = [IsAuthenticatedOrReadOnly, IsOwner]

    def get_queryset(self):
        user = self.request.user
        # queryset = Game.objects.filter(owner=user.id) if user else None
        queryset = Game.objects.all()
        return queryset


class GameDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GameDataView(APIView):
    def get(self, request, *args, **kwargs):
        actions = Action.objects.filter(game=kwargs['pk'])
        conditions = Condition.objects.filter(game=kwargs['pk'])
        choices = Choice.objects.filter(game=kwargs['pk'])
        factions = Faction.objects.filter(game=kwargs['pk'])

        stages = Stage.objects.filter(game=kwargs['pk'])
        slots = Slot.objects.filter(game=kwargs['pk'])
        paths = Path.objects.filter(game=kwargs['pk'])
        fields = Field.objects.filter(game=kwargs['pk'])

        teams = Team.objects.filter(game=kwargs['pk'])
        rounds = Round.objects.filter(game=kwargs['pk'])
        phases = Phase.objects.filter(game=kwargs['pk'])

        tokens = Token.objects.filter(game=kwargs['pk'])
        images = ImageAsset.objects.filter(game=kwargs['pk'])
        sources = Source.objects.filter(game=kwargs['pk'])

        return Response({
            'actions': ActionSerializer(actions, many=True).data,
            'conditions': ConditionSerializer(conditions, many=True).data,
            'choices': ChoiceSerializer(choices, many=True).data,
            'factions': FactionSerializer(factions, many=True).data,

            'stages': StageSerializer(stages, many=True).data,
            'slots': SlotSerializer(slots, many=True).data,
            'paths': MapPathSerializer(paths, many=True).data,
            'fields': FieldSerializer(fields, many=True).data,

            'teams': TeamSerializer(teams, many=True).data,
            'rounds': RoundSerializer(rounds, many=True).data,
            'phases': PhaseSerializer(phases, many=True).data,

            'tokens': TokenSerializer(tokens, many=True).data,
            'images': ImageAssetSerializer(images, many=True).data,
            'sources': SourceSerializer(sources, many=True).data,
        })
