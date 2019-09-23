from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from lobby.routing import lobby_urlpatterns
from arena.routing import arena_urlpatterns

urls = arena_urlpatterns + lobby_urlpatterns

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            urls,
        )
    )
})
