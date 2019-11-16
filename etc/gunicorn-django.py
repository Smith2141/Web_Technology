CONFIG = {
    'mode': 'wsgi',
    'working_dir': '/home/box/web/ask/ask/',
    'pythonpath': '/home/box/web/ask/ask/',
    #'python': '/usr/bin/python3',
    'args': (
        '--bind=0.0.0.0:8080',
        '--workers=5',
        '--timeout=60',
        'wsgi:application',
    ),
}
