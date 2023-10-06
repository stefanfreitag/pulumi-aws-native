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
    'GetApplicationResult',
    'AwaitableGetApplicationResult',
    'get_application',
    'get_application_output',
]

@pulumi.output_type
class GetApplicationResult:
    def __init__(__self__, application_id=None, architecture=None, arn=None, auto_start_configuration=None, auto_stop_configuration=None, image_configuration=None, initial_capacity=None, maximum_capacity=None, network_configuration=None, release_label=None, tags=None, worker_type_specifications=None):
        if application_id and not isinstance(application_id, str):
            raise TypeError("Expected argument 'application_id' to be a str")
        pulumi.set(__self__, "application_id", application_id)
        if architecture and not isinstance(architecture, str):
            raise TypeError("Expected argument 'architecture' to be a str")
        pulumi.set(__self__, "architecture", architecture)
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if auto_start_configuration and not isinstance(auto_start_configuration, dict):
            raise TypeError("Expected argument 'auto_start_configuration' to be a dict")
        pulumi.set(__self__, "auto_start_configuration", auto_start_configuration)
        if auto_stop_configuration and not isinstance(auto_stop_configuration, dict):
            raise TypeError("Expected argument 'auto_stop_configuration' to be a dict")
        pulumi.set(__self__, "auto_stop_configuration", auto_stop_configuration)
        if image_configuration and not isinstance(image_configuration, dict):
            raise TypeError("Expected argument 'image_configuration' to be a dict")
        pulumi.set(__self__, "image_configuration", image_configuration)
        if initial_capacity and not isinstance(initial_capacity, list):
            raise TypeError("Expected argument 'initial_capacity' to be a list")
        pulumi.set(__self__, "initial_capacity", initial_capacity)
        if maximum_capacity and not isinstance(maximum_capacity, dict):
            raise TypeError("Expected argument 'maximum_capacity' to be a dict")
        pulumi.set(__self__, "maximum_capacity", maximum_capacity)
        if network_configuration and not isinstance(network_configuration, dict):
            raise TypeError("Expected argument 'network_configuration' to be a dict")
        pulumi.set(__self__, "network_configuration", network_configuration)
        if release_label and not isinstance(release_label, str):
            raise TypeError("Expected argument 'release_label' to be a str")
        pulumi.set(__self__, "release_label", release_label)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if worker_type_specifications and not isinstance(worker_type_specifications, dict):
            raise TypeError("Expected argument 'worker_type_specifications' to be a dict")
        pulumi.set(__self__, "worker_type_specifications", worker_type_specifications)

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[str]:
        """
        The ID of the EMR Serverless Application.
        """
        return pulumi.get(self, "application_id")

    @property
    @pulumi.getter
    def architecture(self) -> Optional['ApplicationArchitecture']:
        return pulumi.get(self, "architecture")

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the EMR Serverless Application.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="autoStartConfiguration")
    def auto_start_configuration(self) -> Optional['outputs.ApplicationAutoStartConfiguration']:
        """
        Configuration for Auto Start of Application.
        """
        return pulumi.get(self, "auto_start_configuration")

    @property
    @pulumi.getter(name="autoStopConfiguration")
    def auto_stop_configuration(self) -> Optional['outputs.ApplicationAutoStopConfiguration']:
        """
        Configuration for Auto Stop of Application.
        """
        return pulumi.get(self, "auto_stop_configuration")

    @property
    @pulumi.getter(name="imageConfiguration")
    def image_configuration(self) -> Optional['outputs.ApplicationImageConfigurationInput']:
        return pulumi.get(self, "image_configuration")

    @property
    @pulumi.getter(name="initialCapacity")
    def initial_capacity(self) -> Optional[Sequence['outputs.ApplicationInitialCapacityConfigKeyValuePair']]:
        """
        Initial capacity initialized when an Application is started.
        """
        return pulumi.get(self, "initial_capacity")

    @property
    @pulumi.getter(name="maximumCapacity")
    def maximum_capacity(self) -> Optional['outputs.ApplicationMaximumAllowedResources']:
        """
        Maximum allowed cumulative resources for an Application. No new resources will be created once the limit is hit.
        """
        return pulumi.get(self, "maximum_capacity")

    @property
    @pulumi.getter(name="networkConfiguration")
    def network_configuration(self) -> Optional['outputs.ApplicationNetworkConfiguration']:
        """
        Network Configuration for customer VPC connectivity.
        """
        return pulumi.get(self, "network_configuration")

    @property
    @pulumi.getter(name="releaseLabel")
    def release_label(self) -> Optional[str]:
        """
        EMR release label.
        """
        return pulumi.get(self, "release_label")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.ApplicationTag']]:
        """
        Tag map with key and value
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="workerTypeSpecifications")
    def worker_type_specifications(self) -> Optional['outputs.ApplicationWorkerTypeSpecificationInputMap']:
        """
        The key-value pairs that specify worker type to WorkerTypeSpecificationInput. This parameter must contain all valid worker types for a Spark or Hive application. Valid worker types include Driver and Executor for Spark applications and HiveDriver and TezTask for Hive applications. You can either set image details in this parameter for each worker type, or in imageConfiguration for all worker types.
        """
        return pulumi.get(self, "worker_type_specifications")


class AwaitableGetApplicationResult(GetApplicationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetApplicationResult(
            application_id=self.application_id,
            architecture=self.architecture,
            arn=self.arn,
            auto_start_configuration=self.auto_start_configuration,
            auto_stop_configuration=self.auto_stop_configuration,
            image_configuration=self.image_configuration,
            initial_capacity=self.initial_capacity,
            maximum_capacity=self.maximum_capacity,
            network_configuration=self.network_configuration,
            release_label=self.release_label,
            tags=self.tags,
            worker_type_specifications=self.worker_type_specifications)


def get_application(application_id: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetApplicationResult:
    """
    Resource schema for AWS::EMRServerless::Application Type


    :param str application_id: The ID of the EMR Serverless Application.
    """
    __args__ = dict()
    __args__['applicationId'] = application_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:emrserverless:getApplication', __args__, opts=opts, typ=GetApplicationResult).value

    return AwaitableGetApplicationResult(
        application_id=pulumi.get(__ret__, 'application_id'),
        architecture=pulumi.get(__ret__, 'architecture'),
        arn=pulumi.get(__ret__, 'arn'),
        auto_start_configuration=pulumi.get(__ret__, 'auto_start_configuration'),
        auto_stop_configuration=pulumi.get(__ret__, 'auto_stop_configuration'),
        image_configuration=pulumi.get(__ret__, 'image_configuration'),
        initial_capacity=pulumi.get(__ret__, 'initial_capacity'),
        maximum_capacity=pulumi.get(__ret__, 'maximum_capacity'),
        network_configuration=pulumi.get(__ret__, 'network_configuration'),
        release_label=pulumi.get(__ret__, 'release_label'),
        tags=pulumi.get(__ret__, 'tags'),
        worker_type_specifications=pulumi.get(__ret__, 'worker_type_specifications'))


@_utilities.lift_output_func(get_application)
def get_application_output(application_id: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetApplicationResult]:
    """
    Resource schema for AWS::EMRServerless::Application Type


    :param str application_id: The ID of the EMR Serverless Application.
    """
    ...
