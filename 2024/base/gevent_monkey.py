import gevent
from gevent import monkey;monkey.patch_all()
import socket
hosts = ['www.crappytaxidermy.com', 'www.walterpottertaxidermy.com', 'www.antique-taxidermy.com']
jobs = [gevent.spawn(socket.gethostbyname, host) for host in hosts]
gevent.joinall(jobs, timeout=5)
print([job.value for job in jobs])
# Compare this snippet from 2024/base/gevent_monkey.py: