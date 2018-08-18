def init(app):
    @app.route('/api')
    def home():
        return 'API works!'
