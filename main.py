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

    scopes = (None,
              'https://www.googleapis.com/auth/userinfo.email',
              'oauth2:https://www.googleapis.com/auth/userinfo.email')
    for scope in scopes:
      self.response.out.write('\noauth.get_current_user(%s)' % repr(scope))
      try:
        user = oauth.get_current_user(scope)
        self.response.out.write(' = %s\n' % user)
      except oauth.OAuthRequestError, e:
        self.response.set_status(200)
        self.response.out.write(' -> %s\n' % e)
        self.response.out.write(traceback.format_exc())

def main():
  app = webapp.WSGIApplication([
    ('/.*', MainHandler)
  ], debug=True)
  util.run_wsgi_app(app)

if __name__ == "__main__":
  main()
