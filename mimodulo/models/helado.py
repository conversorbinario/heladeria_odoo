# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Helado(models.Model):
    _name = 'helados.receta'
    _order = 'sabor desc, name'

    sabor = fields.Char('Sabor', required=True)
    data_alta = fields.Date('Data de alta')
    state = fields.Selection(
        [('desarrollo', 'Desarrollo'),
         ('experimental', 'Experimental'),
         ('producción', 'En producción')],
        'State', default="desarrollo")
    temperatura_celsius=fields.Float("Temperatura Conservación", required=True)
    receta = fields.Text("Receta", required=True)
    autor_id = fields.Many2one('helados.repostero', string='Autor')

#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class Repostero(models.Model):
    _name = 'helados.repostero'
    _inherit = 'res.partner'

    helados_ids=fields.One2many('helados.receta', 'autor_id', string='Recetas')
    name=fields.Char("Nombre y apellidos", required=True)
    partner_id = fields.Many2one('res.partner', ondelete='cascade')
    local = fields.char("Lugar de Trabajo", required=True)