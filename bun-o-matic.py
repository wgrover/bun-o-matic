from rachiopy import Rachio
import time
import secret

r = Rachio(secret.api)
runtime = 2  # seconds

# far back lawn
r.zone.start(secret.far_back_lawn, runtime)
time.sleep(runtime)

# near back lawn
r.zone.start(secret.near_back_lawn, runtime)
time.sleep(runtime)