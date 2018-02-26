#!/usr/bin/env python
import os
import jinja2
import webapp2

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if params is None:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))

class Capital(object):
    def __init__(self, country, capital, img):
        self.country = country
        self.capital = capital,
        self.img = img

def content():
    lj = Capital(country='Slovenia', capital='Ljubljana', img='/assets/img/lj.jpg')
    zg = Capital(country='Croatia', capital='Zagreb', img='/assets/img/zg.jpg')
    bg = Capital(country='Serbia', capital='Belgrade', img='/assets/img/bg.jpg')
    sr = Capital(country='Bosnia and Hercegovina', capital='Sarajevo', img='/assets/img/sr.jpg')
    pg = Capital(country='Montenegro', capital='Podgorica', img='/assets/img/pg.jpg')
    at = Capital(country='Greece', capital='Athens', img='/assets/img/at.jpg')
    rm = Capital(country='Italy', capital='Rome', img='/assets/img/rm.jpg')
    vi = Capital(country='Austria', capital='Vienna', img='/assets/img/vi.jpg')
    br = Capital(country='Germany', capital='Berlin', img='/assets/img/br.jpg')
    pr = Capital(country='France', capital='Paris', img='/assets/img/pr.jpg')


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("index.html")



app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
], debug=True)
