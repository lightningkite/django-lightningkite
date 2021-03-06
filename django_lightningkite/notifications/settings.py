from django.conf import settings

import environ

env = environ.Env()
env.read_env(settings.ENV_FILE)

TWILIO_ACCOUNT_SID = getattr(
    settings,
    'TWILIO_ACCOUNT_SID',
    env('TWILIO_ACCOUNT_SID', default=None))

TWILIO_AUTH_TOKEN = getattr(
    settings,
    'TWILIO_AUTH_TOKEN',
    env('TWILIO_AUTH_TOKEN', default=None))

TWILIO_NUMBER = getattr(
    settings,
    'TWILIO_NUMBER',
    env('TWILIO_NUMBER', default=None))

# for sending a test text message
TWILIO_RECEIVE_NUMBER = getattr(
    settings,
    'TWILIO_RECEIVE_NUMBER',
    env('TWILIO_RECEIVE_NUMBER', default=None))
