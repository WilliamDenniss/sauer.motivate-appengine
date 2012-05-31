import logging
import os
import traceback

from google.appengine.api import oauth
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util


class MainHandler(webapp.RequestHandler):
  def get(self):
    self.post()

  def post(self):
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.out.write('Hi there!\n')

    scope = 'https://www.googleapis.com/auth/userinfo.email'
    self.response.out.write('\noauth.get_current_user(%s)' % repr(scope))
    try:
      user = oauth.get_current_user(scope)
      self.response.out.write(' = %s\n' % user)
    except oauth.OAuthRequestError, e:
      self.response.set_status(200)
      self.response.out.write(' -> %s %s\n' % (e.__class__.__name__, e.message))
      logging.warn(traceback.format_exc())

def main():
  app = webapp.WSGIApplication([
    ('/.*', MainHandler)
  ], debug=True)
  util.run_wsgi_app(app)

if __name__ == "__main__":
  main()
