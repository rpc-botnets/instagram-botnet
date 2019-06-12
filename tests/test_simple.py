

from .support import *

# def test_upload():
#     template = """
#     bot:
#         username: {{ env.username }}
#         password: {{ env.password }}
#         settings_path: {{ env.username + '_settings.json' }}
#     actions:
#         -
#             name: 1
#             nodes:
#                 # - 'https://images1.apartments.com/i2/nKi28WK6ehLQFaC7840rel_Yj1KkegXMz6vtF7iyhZM/111/panorama-tower-miami-fl-primary-photo.jpg'
#                 - 'https://www.instagram.com/p/BxkxjB-HQ0v/'
#             from: media
#             edges:
#                 - upload_post:
#                     max: 1
#                     caption: weila
#                     geotag: colorado
                    
#     """
#     data = dotdict()
#     result = execute(template, data)
#     print(json.dumps(result, indent=4))


def test_private_follow():
    template = """
    bot:
        username: {{ env.username }}
        password: {{ env.password }}
        settings_path: {{ env.username + '_settings.json' }}
    actions:
        -
            name: 1
            nodes: [patelvaibhav6992]
            from: user
            edges:
                - feed:
                    amount: 1
                - like
    """
    data = dotdict()
    result = execute(template, data)
    print(json.dumps(result, indent=4))
    

def test_scrape_all():
    template = """
    bot:
        username: {{ env.username }}
        password: {{ env.password }}
        settings_path: {{ env.username + '_settings.json' }}
    actions:
        -
            name: 1
            nodes: [mongodb]
            from: user
            edges:
                - followers:
                    amount: 2
                - scrape:
                    model: x.username
                    key: users
    """
    data = dotdict()
    result = execute(template, data)
    print(json.dumps(result, indent=4))


def test_message():
    template = """
    bot:
        username: {{ env.username }}
        password: {{ env.password }}
        settings_path: {{ env.username + '_settings.json' }}
    actions:
        -
            name: 1
            nodes: [xmorse_]
            from: user
            edges:
                - follow
                - message:
                    messages:
                        - [ciao]
                    
    """
    data = dotdict()
    result = execute(template, data)
    print(json.dumps(result, indent=4))

def test_scrape():
    template = """
    bot:
        username: {{ env.username }}
        password: {{ env.password }}
        settings_path: {{ env.username + '_settings.json' }}
    actions:
        -
            name: 1
            nodes: [instagram]
            from: user
            edges:
                - followers:
                    amount: 2
                - scrape:
                    model:
                        username: x.username
                    key: users
    """
    data = dotdict()
    result = execute(template, data)
    print(json.dumps(result, indent=4))

def test_follow():
    template = """
    bot:
        username: {{ env.username }}
        password: {{ env.password }}
        settings_path: {{ env.username + '_settings.json' }}
    actions:
        -
            name: 1
            nodes: [instagram]
            from: user
            edges:
                - follow
    """
    data = dotdict()
    result = execute(template, data)
    print(json.dumps(result, indent=4))

def test_like():
    template = """
    bot:
        username: {{ env.username }}
        password: {{ env.password }}
        settings_path: {{ env.username + '_settings.json' }}
    actions:
        -
            name: 1
            nodes: [instagram]
            from: user
            edges:
                - feed:
                    amount: 1
                - like
    """
    data = dotdict()
    result = execute(template, data)
    print(json.dumps(result, indent=4))


