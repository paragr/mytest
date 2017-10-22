import yaml

class YAMLReader:

	def __init__(self,file=""):
		self.file = file
		
	def read(self,file,decode=True):
		config = ""
		try:
			with open(file,'r') as stream:
				try:
					config = yaml.load(stream)
				except Exception as exp:
					print "Unable to read the file %s"%(file)
					print "Error : ",exp
		except Exception as exp:
			print "Unable to open the file %s"%(file)
			print "Error : ",exp
		
		if decode:
			self.config = self.decode_conf(config)
		else:
			self.config = config
			
		return self.config
		
	def decode_conf(self,config):
		settings = config['ldap_settings']
		decoded_st = {}
		for key in settings.keys():
			if settings[key].has_key("decode") and settings[key]["decode"]:
				decoded_st[key] = settings[key]["str"].decode('base64','strict')
			else:
				decoded_st[key] = settings[key]
		return decoded_st
		
if __name__ == "__main__":
	obj = YAMLReader()
	decoded_st = obj.read("C:/PARAG/PythonProgramms/DjangoWebApplication/paragr/configs/ldap.conf")
	print decoded_st
