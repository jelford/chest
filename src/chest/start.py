#! /usr/bin/env python

import tornado.ioloop
import tornado.web

class DataEndpointHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello, world')

application = tornado.web.Application([
    (r'/', DataEndpointHandler),
])


if __name__ == '__main__':
    application.listen(5805)
    tornado.ioloop.IOLoop.instance().start()
