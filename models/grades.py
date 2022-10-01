# -*- coding: utf-8 -*-

from odoo import models, fields, api


class GradesGroup(models.Model):
    _name = 'student_website.grades_group'
    _description = 'grades for students'

    name = fields.Char('Name')
    subject_id = fields.Many2one(
        "student_website.subjects",
        required=True,
        ondelete="restrict"
    )
    grades_line_ids = fields.One2many(
        comodel_name ='student_website.grades_group_line', 
        inverse_name ='grades_group_id', 
        string='Grades'
    )

class GradesGroupLine(models.Model):
    _name = 'student_website.grades_group_line'
    _description ='grades lines'

    grades_group_id = fields.Many2one(
        comodel_name="student_website.grades_group", 
        required=True,
        ondelete="restrict"
    )
    name = fields.Char('Name')
    grade = fields.Float('Grade')
    active = fields.Boolean('Active')