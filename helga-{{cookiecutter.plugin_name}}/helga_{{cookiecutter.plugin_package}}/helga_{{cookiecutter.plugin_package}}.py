from helga.db import db
from helga.plugins import command, match, random_ack


def logic(args):
    return 'Hello World!'


@command('{{ cookiecutter.plugin_name }}', help='{{ cookiecutter.plugin_description }}')
def {{ cookiecutter.plugin_package }}(client, channel, nick, message, cmd, args):
    return logic(args)
