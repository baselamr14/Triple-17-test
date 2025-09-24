{
    "name": "real_estate",
    "version": "17.0.1.0.0",
    "category": "Productivity",
    "license": "LGPL-3",
    "author": "You",
    "depends": ["base",'sale','mail','contacts'],
    "data": [
        # groups first
        # then views
        "views/property_menus.xml",
        "views/property_view.xml",
        "views/building_view.xml",

        "views/owner_view.xml",
        "views/tag_view.xml",
        "views/sale_order_view.xml",
        "views/res_partner_view.xml",
        'security/ir.model.access.csv',

    ],
    "assets":{
        'web.assets_backend':['real_estate/static/src/css/property.css']
    },
    "installable": True,
    "application": False,
}
