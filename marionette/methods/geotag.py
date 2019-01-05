from funcy import rcompose, take
from itertools import islice
from ..nodes import Geotag, Media
from .common import accepts


@accepts(Media)
def geotag(bot, nodes, amount, args) -> Geotag:

    result = (tag for media in nodes for tag in media.get_geotag(bot))
    # result = (geotag for geotag in result if bot.suitable(geotag))
    result = (geotag for geotag in result if geotag)
    result = take(amount, result)

    return result, bot.last
