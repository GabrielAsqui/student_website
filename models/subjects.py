# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Subjects(models.Model):
    _name = 'student_website.subjects'
    _description = 'grades for students'

    name = fields.Char('Name')
    student_id = fields.Many2one(
        comodel_name ="student_website.student",
        required=True,
        ondelete="restrict"
    )
    grades_group_ids = fields.One2many(
        comodel_name ='student_website.grades_group', 
        inverse_name ='subject_id', 
        string='Grades group'
    )