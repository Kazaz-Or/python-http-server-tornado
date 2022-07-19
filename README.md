<h3>What's in the repo?</h3>

<p>Just a very simple python project for learning purposes about another way to spin a python http web server for REST API's.</p>
</p>This is not an application, but more like different features of tornado library.</p>

<h4>Covered endpoints:</h4>

Basic Request Handler (Returns a simple string):
```
localhost:8000/
```
Static Request Handler (renders a simple HTML page):
```
localhost:8000/front
```
Query String Request Handler (Recievs an number as an argument and returns if number is odd or even):
```
http://localhost:8000/isEven?n=<number>
```
Resource Request Handler:
```
http://localhost:8000/tweet/<number>
```
Upload Image Handler (renders HTML file with a file upload input & button, handles post request with the uploaded file, and eventually returns a URL with the uploaded image:
```
localhost:8000/front
or
localhost:8000/upload
```
List Request Handler (Reads a file and returns a json object with the file's content):
```
localhost:8000/list
```
List Request Write Handler (via the front HTML page, you can add any string to an input field, and it'll eventually write the string into a file in the backend):
```
localhost:8000/front
```


<h4>index.py structure:</h4>

```
    app = tornado.web.Application([
        (r"/", basicRequestHandler),
        (r"/front", staticRequestHandler),
        (r"/isEven", queryStringRequestHandler),
        (r"/tweet/([0-9]+)", resourceRequestHandler),
        (r"/upload", uploadHandler),
        (r"/img/(.*)", tornado.web.StaticFileHandler, {"path": "img"}),
        (r"/list", listRequestHandler)
```

![en-cok-kullanilan-python-frameworkler-06](https://user-images.githubusercontent.com/83350680/179785420-591992df-204d-4307-9186-b87a4bb34419.jpeg)

