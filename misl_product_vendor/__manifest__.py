# -*- coding: utf-8 -*-
{
    'name': "MISL Product Vendor",

    'summary': "MISL Product Vendor",

    'description': """MISL Product Vendor Extension.
    Added vendor to the product template in the website section. The vendor is also displayed on the website's product 
    card view, also eCommerce item listing, and product details page.
    """,
    'author': "Mehedi Khan",
    'website': "https://www.mirinfosystems.com",

    # for the full list
    'category': 'product',
    'version': '18.0.1.0.0',

    'depends': ['base', 'product', 'website', 'website_sale'],
    'data': [
        'views/res_product_template.xml',

        'views/res_website_products_item.xml',
    ],

    'license': 'LGPL-3',
}
