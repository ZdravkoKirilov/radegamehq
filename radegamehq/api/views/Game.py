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
from ..serializers.Team import TeamSerializer
from ..serializers.Round import RoundSerializer
from ..serializers.Phase import PhaseSerializer
from ..serializers.Token import TokenSerializer
from ..serializers.ImageAsset import ImageAssetSerializer
from ..serializers.Style import StyleSerializer
from ..serializers.Keyword import KeywordSerializer
from ..serializers.Sound import SoundSerializer
from ..serializers.State import StateSerializer
from ..serializers.Expression import ExpressionSerializer
from ..serializers.Animation import AnimationSerializer
from ..serializers.Handler import HandlerSerializer
from ..serializers.Setup import SetupSerializer
from ..serializers.Transition import TransitionSerializer
from ..serializers.Text import TextSerializer
from ..serializers.Sonata import SonataSerializer

from ..entities.Action import Action
from ..entities.Condition import Condition
from ..entities.Choice import Choice
from ..entities.Faction import Faction
from ..entities.Stage import Stage
from ..entities.Slot import Slot
from ..entities.Path import Path
from ..entities.Team import Team
from ..entities.Round import Round
from ..entities.Phase import Phase
from ..entities.Token import Token
from ..entities.ImageAsset import ImageAsset
from ..entities.Style import Style
from ..entities.Keyword import Keyword
from ..entities.Sound import Sound
from ..entities.State import State
from ..entities.Expression import Expression
from ..entities.Animation import Animation
from ..entities.Handler import Handler
from ..entities.Setup import Setup
from ..entities.Transition import Transition
from ..entities.Text import Text
from ..entities.Sonata import Sonata

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
        sonatas = Sonata.objects.filter(game=kwargs['pk'])

        teams = Team.objects.filter(game=kwargs['pk'])
        rounds = Round.objects.filter(game=kwargs['pk'])
        phases = Phase.objects.filter(game=kwargs['pk'])

        tokens = Token.objects.filter(game=kwargs['pk'])
        images = ImageAsset.objects.filter(game=kwargs['pk'])
        styles = Style.objects.filter(game=kwargs['pk'])
        keywords = Keyword.objects.filter(game=kwargs['pk'])
        sounds = Sound.objects.filter(game=kwargs['pk'])
        states = State.objects.filter(game=kwargs['pk'])
        expressions = Expression.objects.filter(game=kwargs['pk'])
        animations = Animation.objects.filter(game=kwargs['pk'])
        handlers = Handler.objects.filter(game=kwargs['pk'])
        setups = Setup.objects.filter(game=kwargs['pk'])
        transitions = Transition.objects.filter(game=kwargs['pk'])
        texts = Text.objects.filter(game=kwargs['pk'])

        return Response({
            'actions': ActionSerializer(actions, many=True).data,
            'conditions': ConditionSerializer(conditions, many=True).data,
            'choices': ChoiceSerializer(choices, many=True).data,
            'factions': FactionSerializer(factions, many=True).data,

            'stages': StageSerializer(stages, many=True).data,
            'slots': SlotSerializer(slots, many=True).data,
            'paths': MapPathSerializer(paths, many=True).data,
            'sonatas': SonataSerializer(sonatas, many=True).data,

            'teams': TeamSerializer(teams, many=True).data,
            'rounds': RoundSerializer(rounds, many=True).data,
            'phases': PhaseSerializer(phases, many=True).data,

            'tokens': TokenSerializer(tokens, many=True).data,
            'images': ImageAssetSerializer(images, many=True).data,
            'styles': StyleSerializer(styles, many=True).data,
            'keywords': KeywordSerializer(keywords, many=True).data,
            'sounds': SoundSerializer(sounds, many=True).data,
            'states': StateSerializer(states, many=True).data,
            'expressions': ExpressionSerializer(expressions, many=True).data,
            'animations': AnimationSerializer(animations, many=True).data,
            'handlers': HandlerSerializer(handlers, many=True).data,
            'setups': SetupSerializer(setups, many=True).data,
            'transitions': TransitionSerializer(transitions, many=True).data,
            'texts': TextSerializer(texts, many=True).data,
        })
