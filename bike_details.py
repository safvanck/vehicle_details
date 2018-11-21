import os
import sys
import requests
import json as json
from requests_toolbelt.multipart.encoder import MultipartEncoder as enco


def get_vehicle_details(vehi_num):
    json_decode = {}
    try:

        multipart_data = enco(fields={
            'baxa_renew': 'buy',
            'two_your_vehicle_regno': vehi_num,
            'two_prev_policyno': 'two_your_policy_expdate%5Bdate%5D:24%2F10%2F2018',
            'two_vehicle_mobile': '',
            'two_vehicle_tenure': '1',
            'two_claim_prevpolicy': '1',
            'two_lead_mobile': '9999999999',
            'two_lead_emailid': 'sss333%40sss.sss',
            'two_prev_ncb': '0',
            'op': 'Continue',
            'two_policy_action': '0',
            'form_build_id': 'form-RBcJzEVblfBYXswotxm6q02BlJIDjkJ38pc0uWwro8s',
            'form_id': 'baxa_products_two_index_form'
        }
        )
        urlkey = 'asHGF&shd433?sy\\//rEDDefdslruc@emoh?ecnarusni-releehw-owt/ni.oc.igaxa-itrahb.w{{+w{{+w//:sptthlruc@hjn6BC#43DdhyKn'.replace('{{+', '')[
            ::-1].split('@curl')[1]
        response = requests.post(urlkey, data=multipart_data, headers={
                                 'Content-Type': multipart_data.content_type})
        res = str(response.text)

        model_re = res.split('ng-init="two_vehicle_makemodel=&#039;')[1]
        make_model = model_re[:model_re.find('&#039')]

        model_re = res.split('ng-init="two_city_registration=&#039;')[1]
        reg_place = model_re[:model_re.find('&#039')]

        model_re = res.split('ng-init="two_vehicle_mnf_year=&#039;')[1]
        model_year = int(model_re[:model_re.find('&#039')])

        output = dict(status='success', make_model=make_model,
                      reg_place=reg_place, model_year=model_year)
    except Exception as e:
        output = dict(status='failed', msg='Sorry... Something went wrong! Please give a valid bike registration number! Eg: KL21C3777')
    return output


if __name__ == '__main__':
    vehi_num = sys.argv[1]
    if vehi_num:
        print(get_vehicle_details(vehi_num))
