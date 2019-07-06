# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView
# Forms
from posts.forms import PostForm
# Models
from posts.models import Post


# Create your views here.
class PostDetailView(LoginRequiredMixin, DetailView):
    """Clase Based View para mostrar el detalle de un popst"""
    template_name = 'posts/detail.html'
    slug_field = ('username', 'id')
    slug_url_kwarg = ('username', 'pk')
    context_object_name = 'post'
    queryset = Post.objects.all()


class PostCreateView(LoginRequiredMixin, CreateView):
    """Clase Based View para la creacion de un post"""
    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('feed')

    def get_context_data(self, **kwargs):
        """Agregar un contexto al response (datos adicionales)"""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context
