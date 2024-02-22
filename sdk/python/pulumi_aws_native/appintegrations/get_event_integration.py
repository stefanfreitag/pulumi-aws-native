# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from .. import outputs as _root_outputs

__all__ = [
    'GetEventIntegrationResult',
    'AwaitableGetEventIntegrationResult',
    'get_event_integration',
    'get_event_integration_output',
]

@pulumi.output_type
class GetEventIntegrationResult:
    def __init__(__self__, description=None, event_integration_arn=None, tags=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if event_integration_arn and not isinstance(event_integration_arn, str):
            raise TypeError("Expected argument 'event_integration_arn' to be a str")
        pulumi.set(__self__, "event_integration_arn", event_integration_arn)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The event integration description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="eventIntegrationArn")
    def event_integration_arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the event integration.
        """
        return pulumi.get(self, "event_integration_arn")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        The tags (keys and values) associated with the event integration.
        """
        return pulumi.get(self, "tags")


class AwaitableGetEventIntegrationResult(GetEventIntegrationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEventIntegrationResult(
            description=self.description,
            event_integration_arn=self.event_integration_arn,
            tags=self.tags)


def get_event_integration(name: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEventIntegrationResult:
    """
    Resource Type definition for AWS::AppIntegrations::EventIntegration


    :param str name: The name of the event integration.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:appintegrations:getEventIntegration', __args__, opts=opts, typ=GetEventIntegrationResult).value

    return AwaitableGetEventIntegrationResult(
        description=pulumi.get(__ret__, 'description'),
        event_integration_arn=pulumi.get(__ret__, 'event_integration_arn'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_event_integration)
def get_event_integration_output(name: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetEventIntegrationResult]:
    """
    Resource Type definition for AWS::AppIntegrations::EventIntegration


    :param str name: The name of the event integration.
    """
    ...
