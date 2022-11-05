from website import create_app
from waitress import serve

#context = SSL.Context('server.crt', 'server.key')
#context.use_privatekey_file('server.key')
#context.use_certificate_file('server.crt')
app = create_app()

if __name__ == '__main__':
    app.run(debug=True, ssl_context=('cert.pem', 'key.pem'))
    #serve(app, host='0.0.0.0', port=5000)

