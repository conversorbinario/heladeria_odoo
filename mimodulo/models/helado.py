# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class helados_receta(models.Model):
    _name = 'helados.receta'
    _order = 'sabor desc'

    sabor = fields.Char('Sabor', required=True)
    data_alta = fields.Date('Data de alta')
    estado = fields.Selection(
        [('desarrollo', 'Desarrollo'),
         ('experimental', 'Experimental'),
         ('producción', 'En producción')],
        'Estado', default="desarrollo")
    temperatura_celsius = fields.Float(
        "Temperatura Conservación", required=True)
    receta = fields.Text("Receta", required=True)
    autor_id = fields.Many2one('helados.repostero', String='Autor')

#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
    @api.constrains('temperatura_celsius')
    def _check_porcentaje(self):
        for helado in self:
            if helado.temperatura_celsius > 0:
                raise models.ValidationError('La temperatura de congelación no puede ser superior a 0')

class helados_repostero(models.Model):
    _name = 'helados.repostero'
    _inherit = 'res.partner'

    helados_ids = fields.One2many(
        'helados.receta', 'autor_id', string='Recetas')
    name = fields.Char("Nombre y apellidos", required=True)
    partner_id = fields.Many2one('res.partner', ondelete='cascade')
    local = fields.Char("Lugar de Trabajo", required=True)


class Gelato(models.Model):
    _name = 'helados.receta.gelato'
    _inherit = 'helados.receta'

    densidad = fields.Float('kg/l')
    porcentaje_leche = fields.Integer("Porcentaje graso")

    @api.constrains('porcentaje_graso')
    def _check_porcentaje(self):
        for gelato in self:
            if gelato.porcentaje_leche > 15:
                raise models.ValidationError('Demasiada base láctea')


class Sorbete(models.Model):
    _name = 'helados.receta.sorbete'
    _inherit = 'helados.receta'
    porcentaje_agua = fields.Integer()
    fruta = fields.Boolean()

    @api.constrains('porcentaje_agua')
    def _check_porcentaje(self):
        for sorbete in self:
            if sorbete.porcentaje_agua < 30:
                raise models.ValidationError('Falta agua en este sorbete')
            elif sorbete.porcentaje_agua > 60:
                raise models.ValidationError('Demasiado aguado')
