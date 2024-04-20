from functools import wraps
from django.utils import timezone
from .models import Comment, Post


def update_last_viewed(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        # Call the original view function
        response = func(request, *args, **kwargs)
        
        # Update last viewed time and user
        if request.user.is_authenticated:
            if hasattr(request, 'post'):
                request.post.update_last_viewed(request.user)
            elif 'post_pk' in kwargs:
                post = Post.objects.get(pk=kwargs['post_pk'])
                post.update_last_viewed(request.user)
        
        return response
    return wrapper