from flask import Flask
web=Flask(__name__)

@web.route("/Hello")
def fun():
    return "<h1>Hello</h1>"

web.run()