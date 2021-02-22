# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Helado(models.Model):
    _name = 'helados.receta'
    _order = 'sabor desc, name'

    sabor = fields.Char('Sabor', required=True)
    estado = fields.Integer()
    data_alta = fields.Date('Data de alta')
    state = fields.Selection(
        [('desarrollo', 'Desarrollo'),
         ('experimental', 'Experimental'),
         ('producción', 'En producción')],
        'State', default="desarrollo")
    temperatura_celsius=fields.Float("Temperatura Congelación", required=True)
    value2 = fields.Float(compute="_value_pc", store=True)
    receta = fields.Text("Receta", required=True)
    autor = fields.Many2one('res.currency', string='Autor')

#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100