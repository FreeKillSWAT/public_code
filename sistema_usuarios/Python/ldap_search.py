# ldap_search.py
from LDAPconnect import LDAPConnector

class LDAPSearch:
    def __init__(self):
        self.ldap_connector = LDAPConnector()

    def get_all_groups(self):
        # Realiza una búsqueda para obtener la lista de grupos desde AD
        search_base = ''  # Ajusta según tu estructura de grupos en AD
        search_filter = '(objectClass=group)'
        attributes = ['sAMAccountName']

        entries = self.ldap_connector.search_entries(search_base, search_filter, attributes)
        
        groups = [entry.sAMAccountName.value for entry in entries]
        return groups

    def search_users_in_group(self):
        search_base1 = (f'') #buscar en OU 1
        search_base2 = (f'') #buscar en OU 2
        search_filter = '(objectclass=user)'
        attributes = ['sAMAccountName','cn','userAccountControl']

        entries1 = self.ldap_connector.search_entries(search_base1, search_filter, attributes)
        entries2 = self.ldap_connector.search_entries(search_base2, search_filter, attributes)

        all_entries = entries1 + entries2
        return all_entries

"""
# ldap_search.py
# ldap_search.py

# ldap_search.py
from LDAPconnect import LDAPConnector

class LDAPSearch:
    def __init__(self):
        self.ldap_connector = LDAPConnector()

    def search_all_users(self):
        search_base = f"DC={self.ldap_connector.ldap_domain},DC={self.ldap_connector.ldap_dc}"
        search_filter = "(&(objectCategory=person)(objectClass=user))"
        attributes = ["sAMAccountName"]

        entries = self.ldap_connector.search_entries(search_base, search_filter, attributes)
        return entries
"""