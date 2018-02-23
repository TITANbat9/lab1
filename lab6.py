from wsgiref.simple_server import make_server
from pyramid.response import Response
from pyramid.config import Configurator
from jinja2 import Environment, FileSystemLoader

includes = [
        'app.js',
        'react.js',
        'leaflet.js',
        'D3.js',
        'moment.js',
        'math.js',
        'main.css',
        'bootstrap.css',
        'normalize.css',
    ]
    
css = []
js = []

for include in includes:
    if(include.split('.')[1] == 'js'):
        js.append(include)
    else:
        css.append(include)
        
def index(request):
    env = Environment(loader=FileSystemLoader('.'))  
    res = env.get_template('/index.html').render({'css': css, 'js': js}) 
    return Response(res)

def aboutme(request):
    env = Environment(loader=FileSystemLoader('.'))
    res = env.get_template('about/aboutme.html').render({'css': css, 'js': js})
    return Response(res)
    
if __name__ == '__main__':
    configurator = Configurator()
    configurator.add_route('aboutme', '/about/aboutme.html')
    configurator.add_view(aboutme, route_name='aboutme')
    configurator.add_route('index', '/index.html')
    configurator.add_view(index, route_name='index')
    app = configurator.make_wsgi_app()
    server = make_server('0.0.0.0', 8000, app)
	      server.serve_forever()
