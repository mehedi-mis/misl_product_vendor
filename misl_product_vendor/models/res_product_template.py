from odoo import models, fields


class ProductTemplateExt(models.Model):
    _inherit = "product.template"

    vendor_id = fields.Many2one('res.partner', 'Vendor', ondelete='cascade')
