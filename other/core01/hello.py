#! /usr/bin/env python
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

# （tornado.options）来从命令行中读取设置
from tornado.options import define,options
# 如果用户没有为这个选项指定值，则使用default的值进行代替。Tornado使用type参数进行基本的参数类型验证，当不合适的类型被给出时抛出一个异常。因此，我们允许一个整数的port参数作为options.port来访问程序
define("port",default=8080,help="run on the given port",type=int)

class IndexHandler(tornado.web.RequestHandler):
	# 我们只定义了一个get方法，也就是说这个处理函数将对HTTP的GET请求作出响应
	def get(self):
		# get_argument从一个查询字符串中取得参数greeting的值,如果这个参数没有出现在查询字符串中，Tornado将使用get_argument的第二个参数作为默认值
		greeting = self.get_argument('greeting','Hello')
		# write，它以一个字符串作为函数的参数，并将其写入到HTTP响应中
		self.write(greeting + ',friendly user!')


if __name__ == "__main__":
	# 使用Tornado的options模块来解析命令行。然后我们创建了一个Tornado的Application类的实例。传递给Application类__init__方法的最重要的参数是handlers。它告诉Tornado应该用哪个类来响应请求
	tornado.options.parse_command_line()
	# 参数handlers它是一个元组组成的列表，其中每个元组的第一个元素是一个用于匹配的正则表达式，第二个元素是一个RequestHanlder类
	# "/"被看作为"^/$"
	app = tornado.web.Application(handlers=[(r"/",IndexHandler)])
	# 一旦Application对象被创建，我们可以将其传递给Tornado的HTTPServer对象，然后使用我们在命令行指定的端口进行监听（通过options对象取出。）最后，在程序准备好接收HTTP请求后，我们创建一个Tornado的IOLoop的实例。
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()