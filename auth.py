import json
from datetime import datetime, timedelta

ATTEMPT_LOG = 'logs/login_attempts.log'

def is_locked():
    try:
        with open(ATTEMPT_LOG, 'r') as f:
            data = json.load(f)
            if data['count'] >= 3:
                locked_until = datetime.strptime(data['lock_time'], '%Y-%m-%d %H:%M:%S')
                if datetime.now() < locked_until:
                    return True, (locked_until - datetime.now()).seconds
    except:
        pass
    return False, 0

def reset_lock():
    with open(ATTEMPT_LOG, 'w') as f:
        json.dump({'count': 0, 'lock_time': ''}, f)

def login():
    is_locked_out, wait_time = is_locked()
    if is_locked_out:
        print(f"Account locked. Try again in {wait_time} seconds.")
        return False

    username = input("Username: ")
    password = input("Password: ")

    if username == 'admin' and password == 'admin':
        reset_lock()
        return True
    else:
        try:
            with open(ATTEMPT_LOG, 'r') as f:
                data = json.load(f)
        except:
            data = {'count': 0, 'lock_time': ''}

        data['count'] += 1
        if data['count'] >= 3:
            data['lock_time'] = (datetime.now() + timedelta(minutes=5)).strftime('%Y-%m-%d %H:%M:%S')

        with open(ATTEMPT_LOG, 'w') as f:
            json.dump(data, f)

        print("Invalid credentials.")
        return False
