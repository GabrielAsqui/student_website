# -*- coding: utf-8 -*-

from odoo import models, fields, api


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
