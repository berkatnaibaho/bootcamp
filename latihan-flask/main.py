# from wsgiref.simple_server import make_server
# def application(environ, start_response):
#     body='''
#         <html>
#         <head><title>Demo WSGI</title></head>
#         <body>
#         <h2>Hello WSGI</h2>
#         </body>
#     '''
#     status='200 OK'
#     headers={
#         ('Content-Type', 'text/html'),
#         ('Content-Length', str(len(body)))
#     }
#     start_response(status, headers)
#     return [body]
#
# if __name__=='__main__':
#     server=make_server('localhost', 2000, application)
#     server.serve_forever()

from flask import Flask
application=Flask(__name__)
@application.route('/')
def index():
    return '<h2>Flask on Windows</h2>'

if __name__=='__main__':
    application.run(debug=True)