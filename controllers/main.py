# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class WebsiteStudent(http.Controller):

    @http.route(['/student'], type="http", methods=['GET', 'POST'], auth="user", website=True)
    def website_form_student(self, **kwargs):
        '''
        csrf = False
        Nos da la seguridad para que no existan ataques por robo de sesión
        Method Get by default
        -> Request -> ODOO -> controllador (DB, FUNCIONES) -> RESP (Vistas, JSON, error 404)
        Para todo el sudo() menos el search, y para el search en permisos muy estrictos
        '''
        response = {}
        if request.httprequest.method == 'POST':
            error = False
            student_name = request.params.get('student_name')
            # VALIDACIONES
            if not len(student_name) > 5:
                response['error'] = 'El nombre de ser mayor a 5 caracteres'
                error = True
            if error:
                return request.render('student_website.template_website_student_form', response)
            # Create new Student
            student = request.env['student_website.student'].sudo().create({
                'name': student_name
            })
            return request.render('student_website.template_website_student_success_form', {'student': student})
        # Obtener el id del estudiante
        student = request.env['student_website.student'].sudo().search([('email', '=', request.session.login)])
        response['student'] = student
        return request.render('student_website.template_website_student_form', response)

    @http.route(['/student/<int:student_id>'], type='http', auth="user", website=True)
    def website_search_student_by_id(self, student_id, **kwargs):
        '''
        '''
        student = request.env['student_website.student'].sudo().browse(student_id)
        response = {'student': student}
        return request.render('student_website.template_show_student', response)