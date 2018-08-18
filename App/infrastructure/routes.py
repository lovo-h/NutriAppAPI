from App.infrastructure.converter_regex import RegexConverter


def init(app):
    app.url_map.converters['regex'] = RegexConverter

    # TODO: update these routes
    api_works = '<b>API Works!</b><br /><br/>'

    @app.route('/api/long_descs/<regex("[a-zA-Z0-9&]{3,200}"):snippet>')
    def long_descs(snippet):
        return '{}<p>{}</p>'.format(api_works, snippet.replace('&', ' '))

    @app.route('/api/foods/<regex("[0-9]{5}"):ndb_no>')
    def foods(ndb_no):
        return '{}<p>ndb_no: {}</p>'.format(api_works, ndb_no)
