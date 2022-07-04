from odoo import api, fields, models, tools, _
from odoo.exceptions import AccessError, UserError, ValidationError
from odoo.tools import float_is_zero, float_round, float_repr, float_compare
from odoo.exceptions import ValidationError, UserError
from odoo.http import request
from odoo.osv.expression import AND
import base64
from odoo.tools import float_round


class Currency(models.Model):
    _inherit = "res.currency"

    currency_id = fields.Many2one(
        'res.currency', string='Currency')
    domain = fields.Selection([('base', 'Base'), ('secondary', 'Secondary')], string='Currency Domain', tracking=True)
    secondary_sale_price = fields.Monetary()
    secondary_buy_price = fields.Monetary()
    base_sale_price = fields.Monetary()
    base_buy_price = fields.Monetary()
    tolerance = fields.Integer()
    evaluation = fields.Monetary()
