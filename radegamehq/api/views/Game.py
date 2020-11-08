from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from ..entities.Game import Game
from ..serializers.Game import GameSerializer

from ..serializers.Widget import WidgetSerializer
from ..serializers.Token import TokenSerializer
from ..serializers.ImageAsset import ImageAssetSerializer
from ..serializers.Style import StyleSerializer
from ..serializers.Sound import SoundSerializer
from ..serializers.Expression import ExpressionSerializer
from ..serializers.Animation import AnimationSerializer
from ..serializers.Setup import SetupSerializer
from ..serializers.Text import TextSerializer
from ..serializers.Sonata import SonataSerializer
from ..serializers.Shape import ShapeSerializer
from ..serializers.Sandbox import SandboxSerializer

from ..entities.Widget import Widget
from ..entities.Token import Token
from ..entities.ImageAsset import ImageAsset
from ..entities.Style import Style
from ..entities.Sound import Sound
from ..entities.Expression import Expression
from ..entities.Animation import Animation
from ..entities.Setup import Setup
from ..entities.Text import Text
from ..entities.Sonata import Sonata
from ..entities.Shape import Shape
from ..entities.Sandbox import Sandbox


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
        modules = request.query_params.getlist('modules', None)
        query = {
            'module__in': []
        }

        if modules is not None and modules is not []:
            query['module__in'] = modules


        widgets = Widget.objects.filter(**query)
        sonatas = Sonata.objects.filter(**query)
        tokens = Token.objects.filter(**query)
        images = ImageAsset.objects.filter(**query)
        styles = Style.objects.filter(**query)
        sounds = Sound.objects.filter(**query)
        expressions = Expression.objects.filter(**query)
        animations = Animation.objects.filter(**query)
        texts = Text.objects.filter(**query)
        shapes = Shape.objects.filter(**query)
        sandboxes = Sandbox.objects.filter(**query)

        return Response({
            'widgets': WidgetSerializer(widgets, many=True).data,
            'sonatas': SonataSerializer(sonatas, many=True).data,
            'tokens': TokenSerializer(tokens, many=True).data,
            'images': ImageAssetSerializer(images, many=True).data,
            'styles': StyleSerializer(styles, many=True).data,
            'sounds': SoundSerializer(sounds, many=True).data,
            'expressions': ExpressionSerializer(expressions, many=True).data,
            'animations': AnimationSerializer(animations, many=True).data,
            'texts': TextSerializer(texts, many=True).data,
            'shapes': ShapeSerializer(shapes, many=True).data,
            'sandboxes': SandboxSerializer(sandboxes, many=True).data
        })
