# -*- coding: utf-8 -*-
{
    "name": "tech_order",
    "summary": "Short (1 phrase/line) summary of the module's purpose",
    "description": """
Long description of module's purpose
    """,
    "author": "My Company",
    "website": "https://www.yourcompany.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Uncategorized",
    "version": "0.1",
    # any module necessary for this one to work correctly
    "depends": ["base", "stock"],
    # always loaded
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/meal.xml",
        "wizards/add_external_item.xml",
        "views/order.xml",
        "views/order_tag.xml",
        "views/meal_ingredient.xml",
        "wizards/feedback_reason.xml",
        "views/customer_feedback.xml",
        "views/external_item.xml",
        "views/res_partner.xml",
        "data/server_actions.xml",
        "data/scheduale_action.xml",
        "data/sequence.xml",
    ],
}
