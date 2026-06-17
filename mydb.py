import sshtunnel
import os
from dotenv import load_dotenv

load_dotenv()   


sshtunnel.SSH_TIMEOUT = 10.0
sshtunnel.TUNNEL_TIMEOUT = 10.0

with sshtunnel.SSHTunnelForwarder(
    (os.getenv('DJANGO_DB_HOST')),
    ssh_username=os.getenv('DJANGO_DB_USER'), ssh_password=os.getenv('DJANGO_DB_PASSWORD'),
    remote_bind_address=(os.getenv('DJANGO_DB_HOST'), 3306)
) as tunnel:
    connection = MySQLdb.connect(
        user=os.getenv('DJANGO_DB_USER'),
        passwd=os.getenv('DJANGO_DB_PASSWORD'),
        host='127.0.0.1', port=tunnel.local_bind_port,
        db=os.getenv('DJANGO_DB_NAME'),
    )
    # Do stuff
    connection.close()