ProtocolsDict = {'FTP':' 21', 'DNS':' 53', 'LDAP':' 389', 'MySQL':' 3306'}
question = input("For which protocol whould you like to know the port number?")
if question in ProtocolsDict.keys():
    answer = ProtocolsDict[question]
    print("The port number for protocol " + question + " is" + answer + "!")
else:
    print("The protocol can't be found.")