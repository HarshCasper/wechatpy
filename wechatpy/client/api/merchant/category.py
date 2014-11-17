# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from wechatpy.client.api.base import BaseWeChatAPI


class MerchantCategory(BaseWeChatAPI):

    def get_sub_categories(self, cate_id):
        res = self._post(
            'merchant/category/getsub',
            data={'cate_id': cate_id}
        )
        return res['cate_list']

    def get_sku_list(self, cate_id):
        res = self._post(
            'merchant/category/getsku',
            data={'cate_id': cate_id}
        )
        return res['sku_table']

    def get_properties(self, cate_id):
        res = self._post(
            'merchant/category/getproperty',
            data={'cate_id': cate_id}
        )
        return res['properties']
