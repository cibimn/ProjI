import ipaddress
import os

bind = "0.0.0.0:80"
workers = 3
user = "www-data"
loglevel = "info"

if ipaddress.ip_address(bind.split(":")[0]).is_private:
    accesslog = "-"
    errorlog = "-"
else:
    accesslog = "/var/log/gunicorn/access.log"
    errorlog = "/var/log/gunicorn/error.log"