# LDAPconnect.py
"""
from ldap3 import Server, Connection, SUBTREE, ALL
from decouple import config

class LDAPConnector:
    def __init__(self, ldap_port=389):
        self.server_url = f'ldap://{config("AD_SERVER")}:{ldap_port}'
        self.user_dn = config("AD_USER_DN")
        self.password = config("AD_PASSWORD")

    def connect(self):
        try:
            server = Server(self.server_url, get_info=ALL)
            conn = Connection(server, user=self.user_dn, password=self.password, auto_bind=True)
            return conn
        except Exception as e:
            print(f"Error durante la conexión: {e}")
            return None

    def search_users(self, search_base, search_filter, attributes):
        conn = self.connect()
        if conn:
            try:
                conn.search(search_base=search_base, search_filter=search_filter,
                            search_scope=SUBTREE, attributes=attributes)
                return conn.entries
            except Exception as e:
                print(f"Error durante la búsqueda: {e}")
            finally:
                conn.unbind()
        return None
        """

# LDAPconnect.py
# LDAPconnect.py
# LDAPconnect.py
from ldap3 import Server, Connection, SUBTREE
from decouple import config

class LDAPConnector:
    def __init__(self):
        self.ldap_server = config('AD_SERVER')
        self.ldap_user = config('AD_USERNAME')
        self.ldap_password = config('AD_PASSWORD')
        self.ldap_port = int(config('LDAP_PORT'))
        self.ldap_domain = config('AD_DOMAIN')
        self.ldap_dc = config('DC')
        self.connection = None

    def connect(self):
        server = Server(self.ldap_server, port=self.ldap_port, get_info=SUBTREE)
        self.connection = Connection(server, user=self.ldap_user, password=self.ldap_password, auto_bind=True)

    def disconnect(self):
        if self.connection:
            self.connection.unbind()

    def search_entries(self, search_base, search_filter, attributes):
        if not self.connection:
            self.connect()  # Agregar la conexión si no está establecida

        with self.connection:
            self.connection.search(search_base, search_filter, attributes=attributes)
            entries = [entry for entry in self.connection.entries]
        return entries
# La clase LDAPSearch manejará las búsquedas