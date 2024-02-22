# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = [
    'SigningProfileSignatureValidityPeriod',
]

@pulumi.output_type
class SigningProfileSignatureValidityPeriod(dict):
    def __init__(__self__, *,
                 type: Optional['SigningProfileSignatureValidityPeriodType'] = None,
                 value: Optional[int] = None):
        if type is not None:
            pulumi.set(__self__, "type", type)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def type(self) -> Optional['SigningProfileSignatureValidityPeriodType']:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def value(self) -> Optional[int]:
        return pulumi.get(self, "value")


