from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.conf import settings
import json


def index(request):
    return render(request, 'chat/index.html', {})

def audience(request):
    return render(request, 'chat/audience.html', {
        "logo": settings.LOGO,
        "show_question": settings.SHOW_QUESTION_TO_AUDIENCE
    })

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(int(room_name)))
    })

def player(request, player_number):
    return render(request, 'chat/player.html', {
        'player_number_json': mark_safe(json.dumps(int(player_number))),
        'options': [
            'MKBDH',
            'Smosh',
            'Good Mythical Mornings',
            'Pewdiepie'
        ]
    })