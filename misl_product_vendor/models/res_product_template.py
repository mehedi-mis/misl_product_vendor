from odoo import models, fields


class ProductTemplateExt(models.Model):
    _inherit = "product.template"

    vendor_id = fields.Many2one(
        "res.partner",
        string="eCommerce Vendor",
        domain=[('is_ecommerce_vendor', '=', True)],
        ondelete="cascade"
    )
