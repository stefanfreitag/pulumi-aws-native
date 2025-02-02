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
    'WorkspaceLoggingConfigurationArgs',
]

@pulumi.input_type
class WorkspaceLoggingConfigurationArgs:
    def __init__(__self__, *,
                 log_group_arn: Optional[pulumi.Input[str]] = None):
        """
        Logging configuration
        :param pulumi.Input[str] log_group_arn: CloudWatch log group ARN
        """
        if log_group_arn is not None:
            pulumi.set(__self__, "log_group_arn", log_group_arn)

    @property
    @pulumi.getter(name="logGroupArn")
    def log_group_arn(self) -> Optional[pulumi.Input[str]]:
        """
        CloudWatch log group ARN
        """
        return pulumi.get(self, "log_group_arn")

    @log_group_arn.setter
    def log_group_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "log_group_arn", value)


