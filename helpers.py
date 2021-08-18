import configparser
import sys


def validate_config():
    with open("config.ini") as file:
        config = configparser.RawConfigParser(allow_no_value=True)
        config.read_string(file.read())

        sys.tracebacklimit = 0

        if not config.has_option('discord', 'token'):
            raise ValueError('A discord token is required in the `config.ini` file!')
        if not config.has_option('parameters', 'channel-id'):
            raise ValueError('A channel id is required in the `config.ini` file!')

        if not config.get('parameters', 'channel-id').isdigit():
            raise ValueError('The channel-id must be an integer!')

        if config.has_option('parameters', 'time'):
            if len(config.get('parameters', 'time')) != 5:
                raise ValueError('The time must be of format `HH:MM`!')

    sys.tracebacklimit = None
