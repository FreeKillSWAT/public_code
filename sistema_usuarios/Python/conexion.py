from LDAPconnect import LDAPConnector

def test_ldap_connection():
    ldap_connector = LDAPConnector()

    try:
        conn = ldap_connector.connect()
        print("Conexión exitosa a Active Directory")
        # Puedes realizar más pruebas o consultas aquí si es necesario

    except Exception as e:
        print(f"Error durante la conexión: {e}")

    finally:
        ldap_connector.disconnect()

if __name__ == "__main__":
    test_ldap_connection()
