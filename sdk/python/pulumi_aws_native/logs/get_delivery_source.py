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

__all__ = [
    'GetDeliverySourceResult',
    'AwaitableGetDeliverySourceResult',
    'get_delivery_source',
    'get_delivery_source_output',
]

@pulumi.output_type
class GetDeliverySourceResult:
    def __init__(__self__, arn=None, log_type=None, resource_arns=None, service=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if log_type and not isinstance(log_type, str):
            raise TypeError("Expected argument 'log_type' to be a str")
        pulumi.set(__self__, "log_type", log_type)
        if resource_arns and not isinstance(resource_arns, list):
            raise TypeError("Expected argument 'resource_arns' to be a list")
        pulumi.set(__self__, "resource_arns", resource_arns)
        if service and not isinstance(service, str):
            raise TypeError("Expected argument 'service' to be a str")
        pulumi.set(__self__, "service", service)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        The ARN of the Aqueduct Source.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="logType")
    def log_type(self) -> Optional[str]:
        """
        The type of logs being delivered. Only mandatory when the resourceArn could match more than one. In such a case, the error message will contain all the possible options.
        """
        return pulumi.get(self, "log_type")

    @property
    @pulumi.getter(name="resourceArns")
    def resource_arns(self) -> Optional[Sequence[str]]:
        """
        List of ARN of the resource that will be sending the logs
        """
        return pulumi.get(self, "resource_arns")

    @property
    @pulumi.getter
    def service(self) -> Optional[str]:
        """
        The service generating the log
        """
        return pulumi.get(self, "service")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.DeliverySourceTag']]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")


class AwaitableGetDeliverySourceResult(GetDeliverySourceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDeliverySourceResult(
            arn=self.arn,
            log_type=self.log_type,
            resource_arns=self.resource_arns,
            service=self.service,
            tags=self.tags)


def get_delivery_source(name: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDeliverySourceResult:
    """
    Resource Type definition for AWS::Logs::DeliverySource.


    :param str name: The unique name of the Log source.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:logs:getDeliverySource', __args__, opts=opts, typ=GetDeliverySourceResult).value

    return AwaitableGetDeliverySourceResult(
        arn=pulumi.get(__ret__, 'arn'),
        log_type=pulumi.get(__ret__, 'log_type'),
        resource_arns=pulumi.get(__ret__, 'resource_arns'),
        service=pulumi.get(__ret__, 'service'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_delivery_source)
def get_delivery_source_output(name: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDeliverySourceResult]:
    """
    Resource Type definition for AWS::Logs::DeliverySource.


    :param str name: The unique name of the Log source.
    """
    ...
