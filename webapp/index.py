
import web

import settings

from remotecontrol import RemoteControl

urls = (
    '/', 'index',
    '/command/(.*)', 'command'
)
app = web.application(urls, globals())
render = web.template.render( 'templates/', base='base')

remote = RemoteControl(settings.SERIAL_HOST, settings.SERIAL_TCP_PORT)

class index:        
    def GET(self):
        return render.index()

class command:
    def GET(self, key):
        remote.key_command(key)
        return 'Got command: %s' % key

if __name__ == "__main__":
    app.run()

