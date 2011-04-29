from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

def showPage(handler, page):
  f = open('index.html')
  content = f.read()
  f.close()

  handler.response.out.write(content)

class HomeHandler(webapp.RequestHandler):
  def get(self):
    showPage(self, "index")

class ProjectsHandler(webapp.RequestHandler):
  def get(self):
    showPage(self, "projects")

class WorkHandler(webapp.RequestHandler):
  def get(self):
    showPage(self, "work")

class ContactHandler(webapp.RequestHandler):
  def get(self):
    showPage(self, "contact")


appRoute = webapp.WSGIApplication( [
  ('/', HomeHandler),
  ('/projects', ProjectsHandler),
  ('/work', WorkHandler),
  ('/contact', ContactHandler),
], debug=True)

def main():
  run_wsgi_app(appRoute)

if __name__ == '__main__':
  main()
