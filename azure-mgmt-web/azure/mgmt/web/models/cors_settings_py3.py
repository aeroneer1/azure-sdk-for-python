# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CorsSettings(Model):
    """Cross-Origin Resource Sharing (CORS) settings for the app.

    :param allowed_origins: Gets or sets the list of origins that should be
     allowed to make cross-origin
     calls (for example: http://example.com:12345). Use "*" to allow all.
    :type allowed_origins: list[str]
    """

    _attribute_map = {
        'allowed_origins': {'key': 'allowedOrigins', 'type': '[str]'},
    }

    def __init__(self, *, allowed_origins=None, **kwargs) -> None:
        super(CorsSettings, self).__init__(**kwargs)
        self.allowed_origins = allowed_origins
