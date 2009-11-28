import web

urls = (
    '/', 'index',
    '/command', 'command'
)
app = web.application(urls, globals())
render = web.template.render( 'templates/', base='base')

class index:        
    def GET(self):
        return render.index()

class command:
    def GET(self):
        return 'Waiting for a command on POST'

    def POST(self):
        pass

if __name__ == "__main__":
    app.run()

