# -*- coding: utf-8 -*-
from odoo import models, fields, api
from .helado import Helado

class Sorbete(models.Model):

    porcentaje_agua = fields.Integer()

    @api.constrains('porcentaje_agua')
    def _check_porcentaje(self):
        for sorbete in self:
            if sorbete.porcentaje_agua < 30:
                raise models.ValidationError('Falta agua en este sorbete')
            elif sorbete.porcentaje_agua > 60:
                raise models.ValidationError('Demasiado aguado')