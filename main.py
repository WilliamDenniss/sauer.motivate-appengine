import traceback
import webapp2

from google.appengine.api import oauth


class MainHandler(webapp2.RequestHandler):
  def get(self):
    self.post()

  def post(self):
    self.response.headers['Content-Type'] = 'text/plain'
    try:
      user = oauth.get_current_user()
      self.response.write('Hello, %s' % user)
    except oauth.OAuthRequestError, e:
      self.response.set_status(200)
      self.response.write('Dude, you need to authorize yourself.\n')
      self.response.write(traceback.format_exc())

    try:
      user = oauth.get_current_user('https://www.googleapis.com/auth/userinfo.email')
      self.response.write('Hello, %s' % user)
    except oauth.OAuthRequestError, e:
      self.response.set_status(200)
      self.response.write('Dude, you need to authorize yourself.\n')
      self.response.write(traceback.format_exc())

app = webapp2.WSGIApplication([
  ('/.*', MainHandler)
], debug=True)
