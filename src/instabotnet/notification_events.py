
switch = {
    'comments': { 
        12: 'got_commented',
        66: 'got_referenced',
    },
    'relationships': {
        101: 'got_followed',
    },
    # 'requests': {},
    # 'likes': {},
    # 'usertags': {},
    # 'usertags': {},
    # 'photos_of_you': {},
    # 'comment_likes': {},
}

def notification_events(bot):
    data = bot.api.news_inbox()
    events = []
    notifications = data['new_stories']
    # get number of notifications unread
    for notification_type, count in data['counts']:
        if notification_type in switch:
            filtered = [n for n in notifications if n['story_type'] in switch[notification_type].keys()]
            filtered = sorted(filtered, lambda x: x['timestamp'])
            for n in filtered:
                events.append({
                    'type': switch[notification_type][n['story_type']],
                    'metadata': bot.metadata,
                    'args': {
                        'notification': n['text'],
                    },
                    'timestamp': n['timestamp'],
                })
    return events

    # grab the notification from the data
    # create events for them