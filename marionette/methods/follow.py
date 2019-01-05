from .common import accepts
from ..nodes import Node, User, Media
from .common import today, tap
from ..bot import Bot
from funcy import take, rcompose
import time



@accepts(User)
def follow(bot: Bot, nodes, amount, args):

    count = 0

    def increment():
        global count
        count += 1

    process = rcompose(
        lambda node: node if bot.suitable(node) else tap(None,
            lambda: bot.logger.warn('{} not suitable'.format(node))),
        lambda x: tap(x, increment) if x else None,
        lambda node: _follow(node, bot=bot) \
            if (count <= amount) and node else None,
    )

    [process(node) for node in nodes if node]

    data = bot.last
    return [], data



def _follow(user, bot):
    bot.api.follow(user.id)
    if bot.last['status'] != 'ok':
        bot.logger.warn('request didn\'t return "ok" following {}'.format(user.username))
        time.sleep(bot.delay['error'])
    else:
        with bot.cache as cache:
            cache['followed'].insert(dict(identifier=user.id, time=today(), type='user', interaction='follow'))

        bot.logger.debug('followed %s' % user.id)
        time.sleep(bot.delay['follow'])
