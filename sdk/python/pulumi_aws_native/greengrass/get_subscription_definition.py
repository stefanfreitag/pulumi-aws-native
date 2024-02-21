# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetSubscriptionDefinitionResult',
    'AwaitableGetSubscriptionDefinitionResult',
    'get_subscription_definition',
    'get_subscription_definition_output',
]

@pulumi.output_type
class GetSubscriptionDefinitionResult:
    def __init__(__self__, arn=None, id=None, latest_version_arn=None, name=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if latest_version_arn and not isinstance(latest_version_arn, str):
            raise TypeError("Expected argument 'latest_version_arn' to be a str")
        pulumi.set(__self__, "latest_version_arn", latest_version_arn)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="latestVersionArn")
    def latest_version_arn(self) -> Optional[str]:
        return pulumi.get(self, "latest_version_arn")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Any]:
        """
        Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Greengrass::SubscriptionDefinition` for more information about the expected schema for this property.
        """
        return pulumi.get(self, "tags")


class AwaitableGetSubscriptionDefinitionResult(GetSubscriptionDefinitionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSubscriptionDefinitionResult(
            arn=self.arn,
            id=self.id,
            latest_version_arn=self.latest_version_arn,
            name=self.name,
            tags=self.tags)


def get_subscription_definition(id: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSubscriptionDefinitionResult:
    """
    Resource Type definition for AWS::Greengrass::SubscriptionDefinition
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:greengrass:getSubscriptionDefinition', __args__, opts=opts, typ=GetSubscriptionDefinitionResult).value

    return AwaitableGetSubscriptionDefinitionResult(
        arn=pulumi.get(__ret__, 'arn'),
        id=pulumi.get(__ret__, 'id'),
        latest_version_arn=pulumi.get(__ret__, 'latest_version_arn'),
        name=pulumi.get(__ret__, 'name'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_subscription_definition)
def get_subscription_definition_output(id: Optional[pulumi.Input[str]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSubscriptionDefinitionResult]:
    """
    Resource Type definition for AWS::Greengrass::SubscriptionDefinition
    """
    ...
