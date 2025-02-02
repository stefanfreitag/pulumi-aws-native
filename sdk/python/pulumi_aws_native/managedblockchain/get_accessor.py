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
    'GetAccessorResult',
    'AwaitableGetAccessorResult',
    'get_accessor',
    'get_accessor_output',
]

@pulumi.output_type
class GetAccessorResult:
    def __init__(__self__, arn=None, billing_token=None, creation_date=None, id=None, status=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if billing_token and not isinstance(billing_token, str):
            raise TypeError("Expected argument 'billing_token' to be a str")
        pulumi.set(__self__, "billing_token", billing_token)
        if creation_date and not isinstance(creation_date, str):
            raise TypeError("Expected argument 'creation_date' to be a str")
        pulumi.set(__self__, "creation_date", creation_date)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="billingToken")
    def billing_token(self) -> Optional[str]:
        return pulumi.get(self, "billing_token")

    @property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> Optional[str]:
        return pulumi.get(self, "creation_date")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def status(self) -> Optional['AccessorStatus']:
        return pulumi.get(self, "status")


class AwaitableGetAccessorResult(GetAccessorResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAccessorResult(
            arn=self.arn,
            billing_token=self.billing_token,
            creation_date=self.creation_date,
            id=self.id,
            status=self.status)


def get_accessor(id: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAccessorResult:
    """
    Definition of AWS::ManagedBlockchain::com.amazonaws.taiga.webservice.api#Accessor Resource Type
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:managedblockchain:getAccessor', __args__, opts=opts, typ=GetAccessorResult).value

    return AwaitableGetAccessorResult(
        arn=pulumi.get(__ret__, 'arn'),
        billing_token=pulumi.get(__ret__, 'billing_token'),
        creation_date=pulumi.get(__ret__, 'creation_date'),
        id=pulumi.get(__ret__, 'id'),
        status=pulumi.get(__ret__, 'status'))


@_utilities.lift_output_func(get_accessor)
def get_accessor_output(id: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAccessorResult]:
    """
    Definition of AWS::ManagedBlockchain::com.amazonaws.taiga.webservice.api#Accessor Resource Type
    """
    ...
