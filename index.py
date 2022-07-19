import json
import tornado.web
import tornado.ioloop

PORT = 8000


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


class uploadHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

    def post(self):
        files = self.request.files["imgFile"]
        for file in files:
            file_handler = open(f"img/{file.filename}", "wb")
            file_handler.write(file.body)
            file_handler.close()
        self.write(f"http://localhost:8080/img/{file.filename}")
        

class listRequestHandler(tornado.web.RequestHandler):
    def get(self):
        fh = open("list.txt", "r")
        fruits = fh.read().splitlines()
        fh.close()
        self.write(json.dumps(fruits))
        
    def post(self):
        fruit = self.get_argument("fruit")
        fh = open("list.txt", "a")
        fh.write(f"{fruit}\n")
        fh.close()
        self.write(json.dumps({"message": "Fruit added successfully"}))


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", basicRequestHandler),
        (r"/front", staticRequestHandler),
        (r"/isEven", queryStringRequestHandler),
        (r"/tweet/([0-9]+)", resourceRequestHandler),
        (r"/upload", uploadHandler),
        (r"/img/(.*)", tornado.web.StaticFileHandler, {"path": "img"}),
        (r"/list", listRequestHandler)
    ])

    app.listen(PORT)
    tornado.ioloop.IOLoop.current().start()
