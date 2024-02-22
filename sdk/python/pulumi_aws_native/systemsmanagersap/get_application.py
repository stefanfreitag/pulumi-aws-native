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
from ._enums import *

__all__ = [
    'GetApplicationResult',
    'AwaitableGetApplicationResult',
    'get_application',
    'get_application_output',
]

@pulumi.output_type
class GetApplicationResult:
    def __init__(__self__, application_id=None, application_type=None, arn=None, tags=None):
        if application_id and not isinstance(application_id, str):
            raise TypeError("Expected argument 'application_id' to be a str")
        pulumi.set(__self__, "application_id", application_id)
        if application_type and not isinstance(application_type, str):
            raise TypeError("Expected argument 'application_type' to be a str")
        pulumi.set(__self__, "application_type", application_type)
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[str]:
        return pulumi.get(self, "application_id")

    @property
    @pulumi.getter(name="applicationType")
    def application_type(self) -> Optional['ApplicationType']:
        return pulumi.get(self, "application_type")

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        The ARN of the Helix application
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        The tags of a SystemsManagerSAP application.
        """
        return pulumi.get(self, "tags")


class AwaitableGetApplicationResult(GetApplicationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetApplicationResult(
            application_id=self.application_id,
            application_type=self.application_type,
            arn=self.arn,
            tags=self.tags)


def get_application(arn: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetApplicationResult:
    """
    Resource schema for AWS::SystemsManagerSAP::Application


    :param str arn: The ARN of the Helix application
    """
    __args__ = dict()
    __args__['arn'] = arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:systemsmanagersap:getApplication', __args__, opts=opts, typ=GetApplicationResult).value

    return AwaitableGetApplicationResult(
        application_id=pulumi.get(__ret__, 'application_id'),
        application_type=pulumi.get(__ret__, 'application_type'),
        arn=pulumi.get(__ret__, 'arn'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_application)
def get_application_output(arn: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetApplicationResult]:
    """
    Resource schema for AWS::SystemsManagerSAP::Application


    :param str arn: The ARN of the Helix application
    """
    ...
