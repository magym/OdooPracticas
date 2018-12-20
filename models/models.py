from odoo import models, fields

class res_partner(models.Model):
	"""docstring for ClassName"""
	_name = 'res.partner'
	_inherit = 'res.partner'
	
	hola = fields.Boolean('Hola')
	
	



