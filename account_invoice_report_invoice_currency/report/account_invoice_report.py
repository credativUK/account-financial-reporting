# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2016 credativ Ltd (<http://credativ.co.uk>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import fields, osv


class account_invoice_report(osv.osv):
    _inherit = "account.invoice.report"

    _columns = {
        'price_total_local': fields.float(
            'Total Without Tax (Invoice Currency)',
            readonly=True),
    }

    def _select(self):
        select_str = super(account_invoice_report, self)._select()
        select_str += ", sub.price_total as price_total_local "
        return select_str
