# -*- coding: utf-8 -*-

from odoo import models, fields


class SurtidoSugerido (models.Model):
    _inherit = 'res.partner'

    sugerido = fields.Char(string='Surtido Sugerido',)
