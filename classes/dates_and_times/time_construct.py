# time([hour][, minute][, second][, microsec])

from datetime import time

login_time = time(10, 30)
logout_time = time(20, 45, 35, 13438)

print(f"Login time: {login_time}")
print(f"Logout time: {logout_time}")
