# Django
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Utilities
from datetime import datetime

posts = [
    {
        'name': 'Mont Blac',
        'user': 'L. Andrés',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1036',
    },
    {
        'name': 'Via Láctea',
        'user': 'L. Morales',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=903',
    },
    {
        'name': 'Nuevo auditorio',
        'user': 'D. Naula',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1076',
    }
]


def list_posts(request):
    content = []
    for post in posts:
        content.append("""
            <p>
                <strong>{name}</strong>
            </p>
            <p>
                <strong>{user} - <i>{timestamp}</i></strong>
            </p>
            <figure>
                <img src='{picture}'/>
            </figure>
        """.format(**post))
    return HttpResponse('<br>'.join(content))
