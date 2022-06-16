import tornado.web
import tornado.ioloop

PORT = 8881


class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Basic, simple HTTP server with Python using Tornado")


class staticRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class queryStringRequestHandler(tornado.web.RequestHandler):
    def get(self):
        n = int(self.get_argument("n"))
        r = "odd" if n % 2 else "even"
        self.write("The number " + str(n) + " is " + r)


class resourceRequestHandler(tornado.web.RequestHandler):
    def get(self, id):
        self.write(f"Querying tweet with id {id}")


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", basicRequestHandler),
        (r"/blog", staticRequestHandler),
        (r"/isEven", queryStringRequestHandler),
        (r"/tweet/([0-9]+)", resourceRequestHandler)
    ])

    app.listen(PORT)
    tornado.ioloop.IOLoop.current().start()