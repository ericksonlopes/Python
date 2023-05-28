class Conn:
    def __init__(self):
        print('Connecting...')

    def __enter__(self):
        print('Connected to internet!')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Disconnected...')


with Conn() as conn:
    print('Processing...')
