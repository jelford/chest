#! /usr/bin/env python

import tornado.ioloop
import tornado.web
import tornado.template

import json
from collections import defaultdict
from pkg_resources import resource_filename

template_loader = tornado.template.Loader(resource_filename(__name__, 'resources'))

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
        self.write(template_loader.load('chart.html').generate(gubby="the_gubby"))
        self.finish()
        

application = tornado.web.Application([
    (r'/([^/]+)', DataEndpointHandler),
    (r'/([^/]+)/chart', ChartEndpointHandler)
])


if __name__ == '__main__':
    application.listen(5805)
    tornado.ioloop.IOLoop.instance().start()
