from functools import wraps
from flask import redirect, url_for, session

# Decorator untuk memastikan pengguna sudah login
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:  # Mengecek apakah pengguna sudah login
            return redirect(url_for('login'))  # Jika tidak, alihkan ke halaman login
        return f(*args, **kwargs)
    return decorated_function