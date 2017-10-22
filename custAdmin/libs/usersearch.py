import ldap

class LDAP_UserSearch:
	
	def __init __(self):
		ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT,False)
		self.url = "ldap://192.168.56.16:389"
		self.bind_dn = "cn=admin,dc=test,dc=com"
		self.bind_pass = "admin"
		self.base_db = "ou=users,dc=test,dc=com"
		self.scope = ldap.SCOPE_SUBTREE
		self.attributes = ['givenName','sn','mail','uid']
		self.ldap_obj = ldap.initialize(self.url)
		self.ldap_obj.simple_bind_s(self.bind_dn,self.bind_pass)
		self.searchFilter = "uid="
	
	def search_user(self,user_id):
		searchFilter = self.searchFilter + user_id
searchFilter = "uid=paragr"