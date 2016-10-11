import requests

def consumeGETRequestSync():
 data = '{"query":{"bool":{"must":[{"text":{"record.document":"SOME_JOURNAL"}},{"text":{"record.articleTitle":"farmers"}}],"must_not":[],"should":[]}},"from":0,"size":50,"sort":[],"facets":{}}'
 url = 'http://ES_search_demo.com/document/record/_search?pretty=true'
 headers = {"Accept": "application/json"}
 # call get service with headers and params
 response = requests.get(url,data = data)
 print "code:"+ str(response.status_code)
 print "******************"
 print "headers:"+ str(response.headers)
 print "******************"
 print "content:"+ str(response.text)

consumeGETRequestSync()