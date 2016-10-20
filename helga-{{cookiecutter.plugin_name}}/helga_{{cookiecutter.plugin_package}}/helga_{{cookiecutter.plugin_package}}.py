from helga.plugins import command


@command('{{ cookiecutter.plugin_name }}', help='{{ cookiecutter.plugin_description }}')
def {{ cookiecutter.plugin_package }}(client, channel, nick, message, cmd, args):
    return 'Success!'
