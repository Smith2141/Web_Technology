def application(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    result = [bytes(i + '\n', 'utf8') for i in environ['QUERY_STRING'].split('&')]
    start_response(status, headers)
    return result

"""
git clone https://github.com/Smith2141/Web_Technology.git ./web && cd web && ls -l web

curl -vv 127.0.0.1:8080/?a=b - запрос отправляется напрямую к gunicorn
curl -vv 127.0.0.1/hello/?a=b - проверяем работает и проксирует ли nginx
"""