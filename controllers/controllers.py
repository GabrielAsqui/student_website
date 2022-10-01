# -*- coding: utf-8 -*-
# from odoo import http


# class StudentWebsite(http.Controller):
#     @http.route('/student_website/student_website', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/student_website/student_website/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('student_website.listing', {
#             'root': '/student_website/student_website',
#             'objects': http.request.env['student_website.student_website'].search([]),
#         })

#     @http.route('/student_website/student_website/objects/<model("student_website.student_website"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('student_website.object', {
#             'object': obj
#         })
