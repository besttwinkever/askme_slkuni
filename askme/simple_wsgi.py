def app(environ, start_response):
    method = environ['REQUEST_METHOD']
    params = []

    if method == 'GET':
        queryParams = environ.get('QUERY_STRING', '')
        if queryParams:
            for param in queryParams.split('&'):
                key, value = param.split('=')
                params.append((key, value))
    elif method == 'POST':
        contentLength = int(environ.get('CONTENT_LENGTH', 0))
        if contentLength:
            for param in environ['wsgi.input'].read(contentLength).decode().split('&'):
                key, value = param.split('=')
                params.append((key, value))

    print('Method:', method, 'Params:', params)
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [f'{key}: {value}\n'.encode() for key, value in params]

application = app