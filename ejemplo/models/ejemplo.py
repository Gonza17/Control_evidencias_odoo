# -*- coding: utf-8 -*-
##############################################################################
#
#    ODOO, Solución ERP de código abierto
#
#    Este programa es software libre: se puede redistribuir y / o modificar
#    bajo los términos de la GNU Affero General Public License
#
#    Debería haber recibido una copia de la Licencia Pública General GNU Affero
#    Junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.
#
##############################################################################
# Generado por el plugin Odoo V12 para Dia!

from odoo import api, fields, models
class claseejemplo(models.Model):
    """Esto es una Clase de Ejemplo"""
    _name = 'claseejemplo'
    #_rec_name = ''
    binario = fields.Binary(string='Binario', help='Campo Binario')
    entero = fields.Integer(string='Entero', required=False, readonly=False, help='Canpo Entero')
    caracter = fields.Char(string='Caracter', required=False, readonly=False, help='Campo Caracter')
    boleano = fields.Boolean(string='Boleano', readonly=False, default=True, help='Campo Boleano')
    fecha = fields.Date(string='Fecha', required=True, readonly=False, copy=False, help='Campo Fecha')
    hora = fields.Datetime(string='Hora', required=False, readonly=False, copy=False, help='Campo Hora')
    texto = fields.Text('Texto', required=False, readonly=False, help='Campo Texto')
    flotante = fields.Float('Flotante', required=True, default=0.0, help='Campo Flotante')
    seleccion = fields.Selection([('seleccion1', 'Seleccion 1'),('seleccion2', 'Seleccion 2')], string='Seleccion', store=True, readonly=False, default='seleccion1', help='Campo Selección')
    muchosuno_id = fields.Many2one('muchosuno', string='Muchos a Uno', required=True, readonly=False, help='Campo Muchos a Uno')
    unomuchos_ids = fields.One2many('unomuchos', 'unomuchos_id', string='Uno a Muchos', required=False, readonly=False, help='Campo Uno a Muchos')


class muchosuno(models.Model):
    """Tabla Muchos a Uno"""
    _name = 'muchosuno'
    #_rec_name = ''
    dni = fields.Integer('DNI', size=8, required=True, help='Introduzca su DNI')
    nombres = fields.Char('Nombres', size=100, required=False, help='Introduzca sus Nombres')
    apellidos = fields.Char('Apellidos', size=100, required=False, help='Introduzca sus Apellidos')


class unomuchos(models.Model):
    """Tabla Uno a Muchos"""
    _name = 'unomuchos'
    #_rec_name = ''
    unomuchos_id = fields.Many2one('Uno a Muchos', required=False, readonly=False, help='Campo Uno a Muchos')
    telefono = fields.Char('telefonos', size=100, required=False, readonly=False, help='Introduzca sus Telefonos')


