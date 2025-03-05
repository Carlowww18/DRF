from django.urls import path
from .views import AvaliacoesAPIView, CursosAPIView, CursoAPIView, AvaliacaoAPIView, AvaliacaoViewSet, CursoViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('cursos', CursoViewSet)
router.register('avaliacoes', AvaliacaoViewSet)

urlpatterns = [
    path("cursos/", CursosAPIView.as_view()),
    path("cursos/<int:pk>", CursoAPIView.as_view()),

    path("cursos/<int:curso_pk>/avaliacoes", AvaliacoesAPIView.as_view()),
    path("cursos/<int:curso_pk>/avaliacoes/<int:avaliacao_pk>", AvaliacaoAPIView.as_view()),

    path("avaliacoes/", AvaliacoesAPIView.as_view()),
    path("avaliacoes/<int:avaliacao_pk>", AvaliacaoAPIView.as_view())
]
