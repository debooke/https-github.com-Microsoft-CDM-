# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DDLBatch(Model):
    """DDL batch.

    :param dd_ls:
    :type dd_ls: list of :class:`DDLPayload
     <Microsoft.ADF.SyMSAPIClient.models.DDLPayload>`
    """ 

    _validation = {
        'dd_ls': {'required': True},
    }

    _attribute_map = {
        'dd_ls': {'key': 'DDLs', 'type': '[DDLPayload]'},
    }

    def __init__(self, dd_ls):
        self.dd_ls = dd_ls
