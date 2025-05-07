from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_ecommerce_vendor = fields.Boolean(string="Is eCommerce Vendor", default=False)
    is_customer = fields.Boolean(string="Is Customer", default=False)

    @api.model_create_multi
    def create(self, vals_list):
        # Loop through the vals_list to update context-based fields
        for vals in vals_list:
            if self._context.get('from_sales'):
                vals['is_customer'] = True
            elif self._context.get('from_purchase'):
                vals['is_ecommerce_vendor'] = True

        # Call the super method to create the partners
        partners = super(ResPartner, self).create(vals_list)
        return partners