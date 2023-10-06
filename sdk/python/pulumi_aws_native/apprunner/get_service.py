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
from ._enums import *

__all__ = [
    'GetServiceResult',
    'AwaitableGetServiceResult',
    'get_service',
    'get_service_output',
]

@pulumi.output_type
class GetServiceResult:
    def __init__(__self__, health_check_configuration=None, instance_configuration=None, network_configuration=None, observability_configuration=None, service_arn=None, service_id=None, service_url=None, source_configuration=None, status=None):
        if health_check_configuration and not isinstance(health_check_configuration, dict):
            raise TypeError("Expected argument 'health_check_configuration' to be a dict")
        pulumi.set(__self__, "health_check_configuration", health_check_configuration)
        if instance_configuration and not isinstance(instance_configuration, dict):
            raise TypeError("Expected argument 'instance_configuration' to be a dict")
        pulumi.set(__self__, "instance_configuration", instance_configuration)
        if network_configuration and not isinstance(network_configuration, dict):
            raise TypeError("Expected argument 'network_configuration' to be a dict")
        pulumi.set(__self__, "network_configuration", network_configuration)
        if observability_configuration and not isinstance(observability_configuration, dict):
            raise TypeError("Expected argument 'observability_configuration' to be a dict")
        pulumi.set(__self__, "observability_configuration", observability_configuration)
        if service_arn and not isinstance(service_arn, str):
            raise TypeError("Expected argument 'service_arn' to be a str")
        pulumi.set(__self__, "service_arn", service_arn)
        if service_id and not isinstance(service_id, str):
            raise TypeError("Expected argument 'service_id' to be a str")
        pulumi.set(__self__, "service_id", service_id)
        if service_url and not isinstance(service_url, str):
            raise TypeError("Expected argument 'service_url' to be a str")
        pulumi.set(__self__, "service_url", service_url)
        if source_configuration and not isinstance(source_configuration, dict):
            raise TypeError("Expected argument 'source_configuration' to be a dict")
        pulumi.set(__self__, "source_configuration", source_configuration)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="healthCheckConfiguration")
    def health_check_configuration(self) -> Optional['outputs.ServiceHealthCheckConfiguration']:
        return pulumi.get(self, "health_check_configuration")

    @property
    @pulumi.getter(name="instanceConfiguration")
    def instance_configuration(self) -> Optional['outputs.ServiceInstanceConfiguration']:
        return pulumi.get(self, "instance_configuration")

    @property
    @pulumi.getter(name="networkConfiguration")
    def network_configuration(self) -> Optional['outputs.ServiceNetworkConfiguration']:
        return pulumi.get(self, "network_configuration")

    @property
    @pulumi.getter(name="observabilityConfiguration")
    def observability_configuration(self) -> Optional['outputs.ServiceObservabilityConfiguration']:
        return pulumi.get(self, "observability_configuration")

    @property
    @pulumi.getter(name="serviceArn")
    def service_arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the AppRunner Service.
        """
        return pulumi.get(self, "service_arn")

    @property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> Optional[str]:
        """
        The AppRunner Service Id
        """
        return pulumi.get(self, "service_id")

    @property
    @pulumi.getter(name="serviceUrl")
    def service_url(self) -> Optional[str]:
        """
        The Service Url of the AppRunner Service.
        """
        return pulumi.get(self, "service_url")

    @property
    @pulumi.getter(name="sourceConfiguration")
    def source_configuration(self) -> Optional['outputs.ServiceSourceConfiguration']:
        return pulumi.get(self, "source_configuration")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        AppRunner Service status.
        """
        return pulumi.get(self, "status")


class AwaitableGetServiceResult(GetServiceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServiceResult(
            health_check_configuration=self.health_check_configuration,
            instance_configuration=self.instance_configuration,
            network_configuration=self.network_configuration,
            observability_configuration=self.observability_configuration,
            service_arn=self.service_arn,
            service_id=self.service_id,
            service_url=self.service_url,
            source_configuration=self.source_configuration,
            status=self.status)


def get_service(service_arn: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetServiceResult:
    """
    The AWS::AppRunner::Service resource specifies an AppRunner Service.


    :param str service_arn: The Amazon Resource Name (ARN) of the AppRunner Service.
    """
    __args__ = dict()
    __args__['serviceArn'] = service_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:apprunner:getService', __args__, opts=opts, typ=GetServiceResult).value

    return AwaitableGetServiceResult(
        health_check_configuration=pulumi.get(__ret__, 'health_check_configuration'),
        instance_configuration=pulumi.get(__ret__, 'instance_configuration'),
        network_configuration=pulumi.get(__ret__, 'network_configuration'),
        observability_configuration=pulumi.get(__ret__, 'observability_configuration'),
        service_arn=pulumi.get(__ret__, 'service_arn'),
        service_id=pulumi.get(__ret__, 'service_id'),
        service_url=pulumi.get(__ret__, 'service_url'),
        source_configuration=pulumi.get(__ret__, 'source_configuration'),
        status=pulumi.get(__ret__, 'status'))


@_utilities.lift_output_func(get_service)
def get_service_output(service_arn: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetServiceResult]:
    """
    The AWS::AppRunner::Service resource specifies an AppRunner Service.


    :param str service_arn: The Amazon Resource Name (ARN) of the AppRunner Service.
    """
    ...
