from funcy import partial
from .nodes import Media, User, Geotag, Hashtag
from .make_predicate import make_predicate
from .bot import Bot





def make_bots(script):
    """


    bots:
        -
            username:           '{username}'
            password:           qwerty
            cache:              ./cache.db
            log:                ./logs.html
            cookie:             ./cookie.json
        -
            username:           giovanotti
            password:           qwerty
            cache:              ./cache.db
            log:                ./logs.html
            cookie:             ./cookie.json

    max_per_day:
        likes:                  50
        follow:                 20
        unfollow:               10
        ...

    delay:
        like:                   10
        usual:                  2
        ...

    """

    bots = []

    for data in script['bots']:
        params = dict(
            cache_file=data['cache'] if 'cache' in data else None,
            logs_file=data['logs'] if 'logs' in data else \
                data['log'] if 'log' in data else None,
            cookie_file=data['cookie'] if 'cookie' in data else None,
            username=data['username'] if 'username' in data \
                else error(Exception('username necessary')),
            password=data['password'] if 'password' in data \
                else error(Exception('password necessary')),
        )
        bots += [Bot(**params)]

    for bot in bots:

        if 'max_per_day' in script:
            bot.max_per_day = {key: value for key,
                               value in script['max_per_day'].items()}
        if 'delay' in script:
            bot.delay = {**bot.delay, **{key: value for key, value in script['delay'].items()} }

        if 'filter' in script:
            bot.predicates += [make_predicate(script['filter'], bot)]

    return bots

def error(exception):
    raise exception