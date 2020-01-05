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
from ..serializers.Round import RoundSerializer
from ..serializers.Token import TokenSerializer
from ..serializers.ImageAsset import ImageAssetSerializer
from ..serializers.Style import StyleSerializer
from ..serializers.Sound import SoundSerializer
from ..serializers.Expression import ExpressionSerializer
from ..serializers.Animation import AnimationSerializer
from ..serializers.Setup import SetupSerializer
from ..serializers.Transition import TransitionSerializer
from ..serializers.Text import TextSerializer
from ..serializers.Sonata import SonataSerializer
from ..serializers.Shape import ShapeSerializer

from ..entities.Action import Action
from ..entities.Condition import Condition
from ..entities.Choice import Choice
from ..entities.Faction import Faction
from ..entities.Stage import Stage
from ..entities.Round import Round
from ..entities.Token import Token
from ..entities.ImageAsset import ImageAsset
from ..entities.Style import Style
from ..entities.Sound import Sound
from ..entities.Expression import Expression
from ..entities.Animation import Animation
from ..entities.Setup import Setup
from ..entities.Transition import Transition
from ..entities.Text import Text
from ..entities.Sonata import Sonata
from ..entities.Shape import Shape


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
        keywords = request.query_params.get('keywords', None)
        query = {
            'game': kwargs['pk']
        }
        if keywords is not None:
            query['keywords__contains'] = keywords

        actions = Action.objects.filter(**query)
        conditions = Condition.objects.filter(game=kwargs['pk'])
        choices = Choice.objects.filter(game=kwargs['pk'])
        factions = Faction.objects.filter(game=kwargs['pk'])

        stages = Stage.objects.filter(game=kwargs['pk'])
        sonatas = Sonata.objects.filter(game=kwargs['pk'])

        rounds = Round.objects.filter(game=kwargs['pk'])

        tokens = Token.objects.filter(game=kwargs['pk'])
        images = ImageAsset.objects.filter(game=kwargs['pk'])
        styles = Style.objects.filter(game=kwargs['pk'])
        sounds = Sound.objects.filter(game=kwargs['pk'])
        expressions = Expression.objects.filter(game=kwargs['pk'])
        animations = Animation.objects.filter(game=kwargs['pk'])
        setups = Setup.objects.filter(game=kwargs['pk'])
        transitions = Transition.objects.filter(game=kwargs['pk'])
        texts = Text.objects.filter(game=kwargs['pk'])
        shapes = Shape.objects.filter(game=kwargs['pk'])

        return Response({
            'actions': ActionSerializer(actions, many=True).data,
            'conditions': ConditionSerializer(conditions, many=True).data,
            'choices': ChoiceSerializer(choices, many=True).data,
            'factions': FactionSerializer(factions, many=True).data,

            'stages': StageSerializer(stages, many=True).data,
            'sonatas': SonataSerializer(sonatas, many=True).data,

            'rounds': RoundSerializer(rounds, many=True).data,

            'tokens': TokenSerializer(tokens, many=True).data,
            'images': ImageAssetSerializer(images, many=True).data,
            'styles': StyleSerializer(styles, many=True).data,
            'sounds': SoundSerializer(sounds, many=True).data,
            'expressions': ExpressionSerializer(expressions, many=True).data,
            'animations': AnimationSerializer(animations, many=True).data,
            'setups': SetupSerializer(setups, many=True).data,
            'transitions': TransitionSerializer(transitions, many=True).data,
            'texts': TextSerializer(texts, many=True).data,
            'shapes': ShapeSerializer(shapes, many=True).data
        })
