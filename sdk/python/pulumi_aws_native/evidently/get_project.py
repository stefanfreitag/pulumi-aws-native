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
    'GetProjectResult',
    'AwaitableGetProjectResult',
    'get_project',
    'get_project_output',
]

@pulumi.output_type
class GetProjectResult:
    def __init__(__self__, app_config_resource=None, arn=None, data_delivery=None, description=None, tags=None):
        if app_config_resource and not isinstance(app_config_resource, dict):
            raise TypeError("Expected argument 'app_config_resource' to be a dict")
        pulumi.set(__self__, "app_config_resource", app_config_resource)
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if data_delivery and not isinstance(data_delivery, dict):
            raise TypeError("Expected argument 'data_delivery' to be a dict")
        pulumi.set(__self__, "data_delivery", data_delivery)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="appConfigResource")
    def app_config_resource(self) -> Optional['outputs.ProjectAppConfigResourceObject']:
        return pulumi.get(self, "app_config_resource")

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="dataDelivery")
    def data_delivery(self) -> Optional['outputs.ProjectDataDeliveryObject']:
        return pulumi.get(self, "data_delivery")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.ProjectTag']]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")


class AwaitableGetProjectResult(GetProjectResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetProjectResult(
            app_config_resource=self.app_config_resource,
            arn=self.arn,
            data_delivery=self.data_delivery,
            description=self.description,
            tags=self.tags)


def get_project(arn: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetProjectResult:
    """
    Resource Type definition for AWS::Evidently::Project
    """
    __args__ = dict()
    __args__['arn'] = arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:evidently:getProject', __args__, opts=opts, typ=GetProjectResult).value

    return AwaitableGetProjectResult(
        app_config_resource=pulumi.get(__ret__, 'app_config_resource'),
        arn=pulumi.get(__ret__, 'arn'),
        data_delivery=pulumi.get(__ret__, 'data_delivery'),
        description=pulumi.get(__ret__, 'description'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_project)
def get_project_output(arn: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetProjectResult]:
    """
    Resource Type definition for AWS::Evidently::Project
    """
    ...
