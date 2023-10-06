# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetCrlResult',
    'AwaitableGetCrlResult',
    'get_crl',
    'get_crl_output',
]

@pulumi.output_type
class GetCrlResult:
    def __init__(__self__, crl_data=None, crl_id=None, enabled=None, name=None, tags=None, trust_anchor_arn=None):
        if crl_data and not isinstance(crl_data, str):
            raise TypeError("Expected argument 'crl_data' to be a str")
        pulumi.set(__self__, "crl_data", crl_data)
        if crl_id and not isinstance(crl_id, str):
            raise TypeError("Expected argument 'crl_id' to be a str")
        pulumi.set(__self__, "crl_id", crl_id)
        if enabled and not isinstance(enabled, bool):
            raise TypeError("Expected argument 'enabled' to be a bool")
        pulumi.set(__self__, "enabled", enabled)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if trust_anchor_arn and not isinstance(trust_anchor_arn, str):
            raise TypeError("Expected argument 'trust_anchor_arn' to be a str")
        pulumi.set(__self__, "trust_anchor_arn", trust_anchor_arn)

    @property
    @pulumi.getter(name="crlData")
    def crl_data(self) -> Optional[str]:
        return pulumi.get(self, "crl_data")

    @property
    @pulumi.getter(name="crlId")
    def crl_id(self) -> Optional[str]:
        return pulumi.get(self, "crl_id")

    @property
    @pulumi.getter
    def enabled(self) -> Optional[bool]:
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.CrlTag']]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="trustAnchorArn")
    def trust_anchor_arn(self) -> Optional[str]:
        return pulumi.get(self, "trust_anchor_arn")


class AwaitableGetCrlResult(GetCrlResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCrlResult(
            crl_data=self.crl_data,
            crl_id=self.crl_id,
            enabled=self.enabled,
            name=self.name,
            tags=self.tags,
            trust_anchor_arn=self.trust_anchor_arn)


def get_crl(crl_id: Optional[str] = None,
            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCrlResult:
    """
    Definition of AWS::RolesAnywhere::CRL Resource Type
    """
    __args__ = dict()
    __args__['crlId'] = crl_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:rolesanywhere:getCrl', __args__, opts=opts, typ=GetCrlResult).value

    return AwaitableGetCrlResult(
        crl_data=pulumi.get(__ret__, 'crl_data'),
        crl_id=pulumi.get(__ret__, 'crl_id'),
        enabled=pulumi.get(__ret__, 'enabled'),
        name=pulumi.get(__ret__, 'name'),
        tags=pulumi.get(__ret__, 'tags'),
        trust_anchor_arn=pulumi.get(__ret__, 'trust_anchor_arn'))


@_utilities.lift_output_func(get_crl)
def get_crl_output(crl_id: Optional[pulumi.Input[str]] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCrlResult]:
    """
    Definition of AWS::RolesAnywhere::CRL Resource Type
    """
    ...
