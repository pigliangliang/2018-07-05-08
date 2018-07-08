#author_by zhuxiaoliang
#2018-07-08 下午2:12

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define,options
define('port',default=8000,help='run on the given port',type=int)
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting','pig')
        self.write('hi' +greeting+',this is tornado')
if __name__ =="__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r'/',IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    #http_server.listen(options.port)
    app.listen('8888')
    tornado.ioloop.IOLoop.instance().start()