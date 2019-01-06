from .common import accepts
from ..nodes import Node, User, Media
from .common import today, tap
from ..bot import Bot
from funcy import take, rcompose, ignore, raiser, tap as _tap
import time



@accepts(User)
def follow(bot: Bot, nodes,  args):

    count = 0

    def increment():
        global count
        count += 1

    stop = raiser(StopIteration)

    process = rcompose(
            lambda node: node \
                if bot.suitable(node) \
                else tap(None,lambda: bot.logger.warn('{} not suitable'.format(node))),
            lambda x: tap(x, increment) if x else None,
            lambda node: follow_user(node, bot=bot) \
                if node and (count <= args['amount']) \
                else stop(),
        )


    list(map(process, nodes))

    return [], bot.last



def follow_user(user, bot):
    bot.api.follow(user.id)
    if bot.last['status'] != 'ok':
        bot.logger.warn('request didn\'t return "ok" following {}'.format(user.username))
        time.sleep(bot.delay['error'])
    else:
        with bot.cache as cache:
            cache['followed'].insert(dict(identifier=user.id, time=today(), type='user', interaction='follow'))

        bot.logger.info('followed %s' % user)
        time.sleep(bot.delay['follow'])
