#! /usr/bin/env python

import tornado.ioloop
import tornado.web
import tornado.template

import json
from collections import defaultdict



all_data = defaultdict(list)

class DataEndpointHandler(tornado.web.RequestHandler):
    def post(self, series_name):
        data = json.loads(self.request.body)
        all_data[series_name].append(data)
        self.finish()

    def get(self, series_name):
        self.write(json.dumps( 
                {
                    'd' : all_data[series_name] 
                } 
        ))
        self.finish()

class ChartEndpointHandler(tornado.web.RequestHandler):
    
    def get(self, series_name):
        
        

application = tornado.web.Application([
    (r'/([^/]+)', DataEndpointHandler),
    (r'/([^/]+)/chart', ChartEndpointHandler)
])


if __name__ == '__main__':
    application.listen(5805)
    tornado.ioloop.IOLoop.instance().start()
