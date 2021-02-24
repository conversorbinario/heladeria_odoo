# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class helados_receta(models.Model):
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
class helados_repostero(models.Model):
    _name = 'helados.repostero'
    _inherit = 'res.partner'

    helados_ids=fields.One2many('helados.receta', 'autor_id', string='Recetas')
    name=fields.Char("Nombre y apellidos", required=True)
    partner_id = fields.Many2one('res.partner', ondelete='cascade')
    local = fields.Char("Lugar de Trabajo", required=True)

class Gelato(models.Model):

    _inherit = 'helados.receta'
    densidad = fields.Float('kg/l', required=True)
    porcentaje_leche = fields.Integer("Porcentaje graso")

    @api.constrains('porcentaje_graso')
    def _check_porcentaje(self):
        for gelato in self:
            if gelato.porcentaje_leche > 15:
                raise models.ValidationError('Demasiada base láctea')

class Sorbete(models.Model):
    
    _name = 'helados.receta'
    porcentaje_agua = fields.Integer()

    @api.constrains('porcentaje_agua')
    def _check_porcentaje(self):
        for sorbete in self:
            if sorbete.porcentaje_agua < 30:
                raise models.ValidationError('Falta agua en este sorbete')
            elif sorbete.porcentaje_agua > 60:
                raise models.ValidationError('Demasiado aguado')
