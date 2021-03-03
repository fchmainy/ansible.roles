#!/usr/bin/env python
import json
import getopt, sys

# print usage
def usage():
	print("python reconciliate.py -i <tenant_file.json> -t <tenantName> -n <appName> -a <app_file.json> -o <output_file.json>")
        print("-i       --input         input AS3 declaration")
	print("-t	--tenant	tenant name")
	print("-n	--appName	Application Service Name")
	print("-a	--appSvc	Application file part of the AS3 declaration")
        print("-o       --output        output AS3 declaration")

# Reconciliate entries
def reconciliate(i,t,n,a):

	with open(i) as f1:
		data_tenant = json.load(f1)

	with open(a) as f2:
		data_app = json.load(f2)
	
	data_tenant[t][n] = data_app
#	res = json.dumps(data_tenant)
	return data_tenant

def createFile(o, res):
	with open(o,'w') as f:
		json.dump(res, f)

def main():
	try:
		(opts, args) = getopt.getopt(sys.argv[1:], 'hi:t:n:a:o:e', ['help','input','tenant=', 'appName=', 'appSvc=', 'output','end='])
	except getopt.GetoptError as err:
		print(err)
		sys.exit(2)

	if len(opts) != 0:
		for (o, a) in opts:
			if o in ('h', '--help'):
				usage()
				sys.exit()
                        elif o in ('-i', '--input'):
                                inputFile = a
			elif o in ('-t', '--tenant'):
				tenant = a
			elif o in ('-n', '--appName'):
				appName = a
			elif o in ('-a', '--appSvc'):
				appSvc = a
                        elif o in ('-o', '--output'):
                                output = a
			else:
				usage()
				sys.exit(2)
	else:
		usage()
		sys.exit(2)

	res=reconciliate(inputFile, tenant, appName, appSvc)
	createFile(output, res)

if __name__ == '__main__':
	main()
