# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from .helado import Helado

class Gelato(models.Model):

    densidad = fields.Float('kg/l', required=True)
    porcentaje_leche = fields.Integer("Porcentaje graso")

    @api.constrains('porcentaje_graso')
    def _check_porcentaje(self):
        for gelato in self:
            if gelato.porcentaje_leche > 15:
                raise models.ValidationError('Demasiada base láctea')

#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100