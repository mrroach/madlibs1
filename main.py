import webapp2
import jinja2
import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainHandler(webapp2.RequestHandler):
    def get(self):
        main_template = JINJA_ENVIRONMENT.get_template('templates/main.html')
        self.response.write(main_template.render(template_vars))

    def post(self):
        template_vars = {
            'noun1':self.request.get("noun1"),
            'activity':self.request.get("activity"),
            'teacher':self.request.get("teacher"),
            'celebrity':self.request.get("celebrity"), 		
            'show':self.request.get("show"),
            'fun':self.request.get("fun"),
        } 
        main_template = JINJA_ENVIRONMENT.get_template('templates/main.html')
        self.response.write(main_template.render(template_vars))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)
