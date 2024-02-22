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
    'SigningProfileSignatureValidityPeriodArgs',
]

@pulumi.input_type
class SigningProfileSignatureValidityPeriodArgs:
    def __init__(__self__, *,
                 type: Optional[pulumi.Input['SigningProfileSignatureValidityPeriodType']] = None,
                 value: Optional[pulumi.Input[int]] = None):
        if type is not None:
            pulumi.set(__self__, "type", type)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input['SigningProfileSignatureValidityPeriodType']]:
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input['SigningProfileSignatureValidityPeriodType']]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "value", value)


