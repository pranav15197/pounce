# pounce

# Installation Instructions
install python dependencies

`bash
pip install -r requirements.txt
`

Redis is required for this. You can install and run redis locally, or more easily you could use docker.
Once redis is runnnig set the following variable in the project settings

`python
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}
`

# start the app

`bash
python manage.py runserver
`

Quiz Master Screen -
http://localhost:8000/quiz


Player Screens - 

http://localhost:8000/quiz/1/
http://localhost:8000/quiz/2/
http://localhost:8000/quiz/3/
http://localhost:8000/quiz/4/
http://localhost:8000/quiz/5/
http://localhost:8000/quiz/6/
http://localhost:8000/quiz/7/
http://localhost:8000/quiz/8/

Audience Screen - 

http://localhost:8000/quiz/audience/


config variables - 

SHOW_QUESTION_TO_AUDIENCE = False
LOGO = "https://via.placeholder.com/350"
