from odoo import api, fields, models, tools, _
from odoo.exceptions import AccessError, UserError, ValidationError
from odoo.tools import float_is_zero, float_round, float_repr, float_compare
from odoo.exceptions import ValidationError, UserError
from odoo.http import request
from odoo.osv.expression import AND
import base64
from odoo.tools import float_round


class BounceRule(models.Model):
    _inherits = "product.category"

    add_bonus = fields.Boolean(string="Bonus Rules",
                               help="Has Bonus Rules."
                               )
