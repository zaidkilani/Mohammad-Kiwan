from odoo import api, fields, models, tools, _
from odoo.exceptions import AccessError, UserError, ValidationError
from odoo.tools import float_is_zero, float_round, float_repr, float_compare
from odoo.exceptions import ValidationError, UserError
from odoo.http import request
from odoo.osv.expression import AND
import base64
from odoo.tools import float_round


class TimeOff(models.Model):
    _inherit = "hr.leave"

    number_of_days = fields.Float(
        'Number of Days', compute='_check_timeoff_number', store=True, readonly=False, tracking=True,
        default=1,
        help='Duration in days. Reference field to use when necessary.')

    @api.constrains('number_of_days')
    def _check_timeoff_number(self):

        if (self.holiday_status_id):
            if (self.number_of_days) > (
                    self.holiday_status_id.remaining_leaves / 12):
                raise ValidationError('you can not take this time off days ')
            else:
                return True

                # @api.constrains('phone')
    # def _check_phone_number_len(self):
    #
    #     for rec in self:
    #
    #         if (rec.phone and len(rec.phone) > 11 or rec.phone and len(rec.phone) < 11):
    #             raise ValidationError(_("this is invalid phone number !"))
    #         return True

    # @api.constrains('mobile')
    # def _check_phone(self):
    #     count_mobile = self.search_count([('mobile', '=', self.mobile)])
    #     if count_mobile > 1 and self.mobile is not False:
    #         raise ValidationError('The phone already registered, please use another phone!')
