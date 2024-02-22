# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from .. import outputs as _root_outputs
from ._enums import *

__all__ = [
    'GetTlsInspectionConfigurationResult',
    'AwaitableGetTlsInspectionConfigurationResult',
    'get_tls_inspection_configuration',
    'get_tls_inspection_configuration_output',
]

@pulumi.output_type
class GetTlsInspectionConfigurationResult:
    def __init__(__self__, description=None, tags=None, tls_inspection_configuration=None, tls_inspection_configuration_arn=None, tls_inspection_configuration_id=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if tls_inspection_configuration and not isinstance(tls_inspection_configuration, dict):
            raise TypeError("Expected argument 'tls_inspection_configuration' to be a dict")
        pulumi.set(__self__, "tls_inspection_configuration", tls_inspection_configuration)
        if tls_inspection_configuration_arn and not isinstance(tls_inspection_configuration_arn, str):
            raise TypeError("Expected argument 'tls_inspection_configuration_arn' to be a str")
        pulumi.set(__self__, "tls_inspection_configuration_arn", tls_inspection_configuration_arn)
        if tls_inspection_configuration_id and not isinstance(tls_inspection_configuration_id, str):
            raise TypeError("Expected argument 'tls_inspection_configuration_id' to be a str")
        pulumi.set(__self__, "tls_inspection_configuration_id", tls_inspection_configuration_id)

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tlsInspectionConfiguration")
    def tls_inspection_configuration(self) -> Optional['outputs.TlsInspectionConfigurationTlsInspectionConfiguration']:
        return pulumi.get(self, "tls_inspection_configuration")

    @property
    @pulumi.getter(name="tlsInspectionConfigurationArn")
    def tls_inspection_configuration_arn(self) -> Optional[str]:
        return pulumi.get(self, "tls_inspection_configuration_arn")

    @property
    @pulumi.getter(name="tlsInspectionConfigurationId")
    def tls_inspection_configuration_id(self) -> Optional[str]:
        return pulumi.get(self, "tls_inspection_configuration_id")


class AwaitableGetTlsInspectionConfigurationResult(GetTlsInspectionConfigurationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTlsInspectionConfigurationResult(
            description=self.description,
            tags=self.tags,
            tls_inspection_configuration=self.tls_inspection_configuration,
            tls_inspection_configuration_arn=self.tls_inspection_configuration_arn,
            tls_inspection_configuration_id=self.tls_inspection_configuration_id)


def get_tls_inspection_configuration(tls_inspection_configuration_arn: Optional[str] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTlsInspectionConfigurationResult:
    """
    Resource type definition for AWS::NetworkFirewall::TLSInspectionConfiguration
    """
    __args__ = dict()
    __args__['tlsInspectionConfigurationArn'] = tls_inspection_configuration_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:networkfirewall:getTlsInspectionConfiguration', __args__, opts=opts, typ=GetTlsInspectionConfigurationResult).value

    return AwaitableGetTlsInspectionConfigurationResult(
        description=pulumi.get(__ret__, 'description'),
        tags=pulumi.get(__ret__, 'tags'),
        tls_inspection_configuration=pulumi.get(__ret__, 'tls_inspection_configuration'),
        tls_inspection_configuration_arn=pulumi.get(__ret__, 'tls_inspection_configuration_arn'),
        tls_inspection_configuration_id=pulumi.get(__ret__, 'tls_inspection_configuration_id'))


@_utilities.lift_output_func(get_tls_inspection_configuration)
def get_tls_inspection_configuration_output(tls_inspection_configuration_arn: Optional[pulumi.Input[str]] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTlsInspectionConfigurationResult]:
    """
    Resource type definition for AWS::NetworkFirewall::TLSInspectionConfiguration
    """
    ...
