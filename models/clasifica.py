# -*- coding: utf-8 -*-
from odoo import fields, models


class ClasificacionPartner(models.Model):
    _inherit = "res.partner"

    clasificaciones_ids = fields.Many2many(
        'clasificacion.clasificaciones', 'clasificacion_clasificaciones_rel',
        'src_id', 'dest_id',
        string='Clasificaciones')


class SubclasePartner(models.Model):
    _inherit = "res.partner"

    subclases_ids = fields.Many2many(
        'clasificacion.subclases', 'clasificacion_subclases_rel',
        'src_id', 'dest_id',
        string='Subclases')
