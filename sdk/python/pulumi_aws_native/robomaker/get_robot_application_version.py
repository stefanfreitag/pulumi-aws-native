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
    'GetRobotApplicationVersionResult',
    'AwaitableGetRobotApplicationVersionResult',
    'get_robot_application_version',
    'get_robot_application_version_output',
]

@pulumi.output_type
class GetRobotApplicationVersionResult:
    def __init__(__self__, application_version=None, arn=None):
        if application_version and not isinstance(application_version, str):
            raise TypeError("Expected argument 'application_version' to be a str")
        pulumi.set(__self__, "application_version", application_version)
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)

    @property
    @pulumi.getter(name="applicationVersion")
    def application_version(self) -> Optional[str]:
        return pulumi.get(self, "application_version")

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")


class AwaitableGetRobotApplicationVersionResult(GetRobotApplicationVersionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRobotApplicationVersionResult(
            application_version=self.application_version,
            arn=self.arn)


def get_robot_application_version(arn: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRobotApplicationVersionResult:
    """
    AWS::RoboMaker::RobotApplicationVersion resource creates an AWS RoboMaker RobotApplicationVersion. This helps you control which code your robot uses.
    """
    __args__ = dict()
    __args__['arn'] = arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:robomaker:getRobotApplicationVersion', __args__, opts=opts, typ=GetRobotApplicationVersionResult).value

    return AwaitableGetRobotApplicationVersionResult(
        application_version=pulumi.get(__ret__, 'application_version'),
        arn=pulumi.get(__ret__, 'arn'))


@_utilities.lift_output_func(get_robot_application_version)
def get_robot_application_version_output(arn: Optional[pulumi.Input[str]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRobotApplicationVersionResult]:
    """
    AWS::RoboMaker::RobotApplicationVersion resource creates an AWS RoboMaker RobotApplicationVersion. This helps you control which code your robot uses.
    """
    ...
