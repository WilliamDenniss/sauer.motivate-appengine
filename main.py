from google.appengine.api import oauth
import logging
import traceback
import webapp2


class MainHandler(webapp2.RequestHandler):
  def get(self):
    self.post()

  def post(self):
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.write('Hi there!\n')

    scope = 'https://www.googleapis.com/auth/userinfo.email'
    self.response.write('\noauth.get_current_user(%s)' % repr(scope))
    try:
      user = oauth.get_current_user(scope)
      self.response.write(' = %s\n' % user)
    except oauth.OAuthRequestError, e:
      self.response.set_status(200)
      self.response.write(' -> %s %s\n' % (e.__class__.__name__, e.message))
      logging.warn(traceback.format_exc())


app = webapp2.WSGIApplication([
  ('/.*', MainHandler)
], debug=True)
