import configparser
import sys


def format_error_message__value_error(section, option):
    return f'config.ini: {section}.{option} is required!'


def format_error_message__type_error(section, option, required_type):
    return f'config.ini: {section}.{option} must be of type <{required_type}>!'


def format_error_message__format_error(section, option, required_format):
    return f'config.ini: {section}.{option} must have a format of <{required_format}>!'


def validate_config():
    with open("config.ini") as file:
        config = configparser.RawConfigParser(allow_no_value=True)
        config.read_string(file.read())

        sys.tracebacklimit = 0

        if not config.has_option('discord', 'token'):
            raise ValueError(format_error_message__value_error('discord', 'token'))
        if not config.has_option('parameters', 'channel-id'):
            raise ValueError(format_error_message__value_error('discord', 'channel-id'))

        if not config.get('parameters', 'channel-id').isdigit():
            raise TypeError(format_error_message__type_error('discord', 'channel-id', 'int'))

        if config.has_option('parameters', 'time'):
            if len(config.get('parameters', 'time')) != 5:
                raise TypeError(format_error_message__format_error('discord', 'time', 'HH:MM'))

        for day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            if not config.has_option('videos', day):
                raise ValueError(format_error_message__value_error('videos', day))

    sys.tracebacklimit = None
