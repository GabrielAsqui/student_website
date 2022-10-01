# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import Warning


class Student(models.Model):
    _name = 'student_website.student'
    _description = 'data for students'
    _inherits = {"res.partner": "partner_id"}

    partner_id = fields.Many2one(
        comodel_name="res.partner", 
        required=True,
        ondelete="restrict"
    )
    subjects_ids = fields.One2many(
        comodel_name ='student_website.subjects', 
        inverse_name ='student_id', 
        string='Subjects'
    )

    def create_portal_user(self):
        for record in self:
            if not record.partner_id:
                raise Warning('Save the faculty first.')
            if not record.email:
                raise Warning('Update faculty email first.')
            groups_id = self.env.ref(
                'base.group_portal') or False
            user_id = self.env['res.users'].create(
                {
                    'partner_id': record.partner_id.id,
                    'login': record.email,
                    'password': record.vat,
                    'groups_id': groups_id           
                })
        return True
