from glog import *

logs = ArizonaLogs('USERNAME', 'PASSWORD', 'GOOGLE_AUTH_SECRET')
query = SearchQuery(server=22, player=14, types=[Type.ADMIN_SALARY])
logs.login()
result = logs.search(query)
