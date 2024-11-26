# coding: utf-8
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models,api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    max_table_number = fields.Integer()



    @api.model
    def get_values(self):
        res = super(ResConfigSettings,self).get_values()
        res.update(
            max_table_number = self.env['ir.config_parameter'].get_param('tech_order.max_table_number')
        )
        return res


    @api.model
    def set_values(self):
        res = super(ResConfigSettings,self).set_values()
        self.env['ir.config_parameter'].set_param('tech_order.max_table_number',self.max_table_number)
        return res
        