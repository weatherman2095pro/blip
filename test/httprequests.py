request = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00E\x00\x01\xab\x1f\x9f@\x00@\x06\x1b\xac\x7f\x00\x00\x01\x7f\x00\x00\x01\x94(\x1f\x90a\x9b\x88(?\xad,\x97\x80\x18\x01V\xff\x9f\x00\x00\x01\x01\x08\n\x00\x1b\x97\xba\x00\x1b\x97\xbaGET /example.txt HTTP/1.1\r\nHost: localhost:8080\r\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\nIf-Modified-Since: Tue, 03 Apr 2018 13:40:06 GMT\r\n\r\n'

response = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00E\x00\x00\xed\xbb.@\x00@\x06\x80\xda\x7f\x00\x00\x01\x7f\x00\x00\x01\x1f\x90\x94(?\xad,\x97a\x9b\x89\x9f\x80\x18\x01^\xfe\xe1\x00\x00\x01\x01\x08\n\x00\x1b\x97\xba\x00\x1b\x97\xbaHTTP/1.0 200 OK\r\nServer: SimpleHTTP/0.6 Python/3.5.3\r\nDate: Tue, 03 Apr 2018 14:47:17 GMT\r\nContent-type: text/plain\r\nContent-Length: 19\r\nLast-Modified: Tue, 03 Apr 2018 13:40:06 GMT\r\n\r\n'


