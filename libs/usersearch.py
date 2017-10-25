import ldap

class FindLDAPUser:

	def __init__(self):
		ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT,False)
		self.base_dn = "ou=users,dc=test,dc=com"
		self.searchScope = ldap.SCOPE_SUBTREE
		self.attrs = ['givenName','sn','mail','uid']
		self.attrs_map = {
			"givenName" : "first_name",
			"sn" : "last_name",
			"mail" : "email",
			"uid" : "username",
		}
		self.searchFilter = "uid="

	def ldap_initialize(self):
		try:
			self.s_obj = ldap.initialize("ldap://192.168.56.16:389")
			self.s_obj.simple_bind_s("cn=admin,dc=test,dc=com", "admin")
		except Exception as err:
			print "Error Occured During LDAP Initialization"

	def get_user(self,user):
		try:
			self.ldap_initialize()
			result = self.s_obj.search_s(self.base_dn,self.searchScope,self.searchFilter+user,self.attrs)
		except Exception as err:
			reutrn = "Issues in LDAP Search"

		user_data = {}
		if result:
			result = result[0][1]
			for key in result:
				user_data[self.attrs_map[key]] = result[key][0]
		return user_data
				
		
if __name__ == "__main__":
	obj = FindLDAPUser()
	userdata = obj.get_user("pritesh")
	print userdata
	