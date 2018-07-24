import webapp2
import jinja2
import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainHandler(webapp2.RequestHandler):
    """This shows our form."""

    def get(self):
        main_template = JINJA_ENVIRONMENT.get_template('templates/main.html')
        self.response.write(main_template.render())


class ResultsHandler(webapp2.RequestHandler):
    """This shows the results of submitting the form."""

    def get(self):
        template_vars = {
            'noun1':self.request.get("noun1"),
            'activity':self.request.get("activity"),
            'teacher':self.request.get("teacher"),
            'celebrity':self.request.get("celebrity"), 		
            'show':self.request.get("show"),
            'fun':self.request.get("fun"),
        } 
        results_template = JINJA_ENVIRONMENT.get_template('templates/results.html')
        self.response.write(results_template.render(template_vars))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/results', ResultsHandler),
], debug=True)
