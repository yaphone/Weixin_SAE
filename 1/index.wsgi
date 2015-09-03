# coding: UTF-8
import os
import sae
import web
import json
import urllib

from weixin import Weixin
 
urls = (
    '/', 'Hello', 
    '/weixin', 'Weixin', 
)
 
app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, 'templates')
render = web.template.render(templates_root)
 
class Hello:
    def GET(self):
        return render.hello("你好")
        
        
 
app = web.application(urls, globals()).wsgifunc()
 
application = sae.create_wsgi_app(app)