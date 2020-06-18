# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
	_inherit = "slide.channel"
	scorm_package = fields.Binary(string="Scorm Package")