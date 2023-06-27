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
    'GetAccountAuditConfigurationResult',
    'AwaitableGetAccountAuditConfigurationResult',
    'get_account_audit_configuration',
    'get_account_audit_configuration_output',
]

@pulumi.output_type
class GetAccountAuditConfigurationResult:
    def __init__(__self__, audit_check_configurations=None, audit_notification_target_configurations=None, role_arn=None):
        if audit_check_configurations and not isinstance(audit_check_configurations, dict):
            raise TypeError("Expected argument 'audit_check_configurations' to be a dict")
        pulumi.set(__self__, "audit_check_configurations", audit_check_configurations)
        if audit_notification_target_configurations and not isinstance(audit_notification_target_configurations, dict):
            raise TypeError("Expected argument 'audit_notification_target_configurations' to be a dict")
        pulumi.set(__self__, "audit_notification_target_configurations", audit_notification_target_configurations)
        if role_arn and not isinstance(role_arn, str):
            raise TypeError("Expected argument 'role_arn' to be a str")
        pulumi.set(__self__, "role_arn", role_arn)

    @property
    @pulumi.getter(name="auditCheckConfigurations")
    def audit_check_configurations(self) -> Optional['outputs.AccountAuditConfigurationAuditCheckConfigurations']:
        return pulumi.get(self, "audit_check_configurations")

    @property
    @pulumi.getter(name="auditNotificationTargetConfigurations")
    def audit_notification_target_configurations(self) -> Optional['outputs.AccountAuditConfigurationAuditNotificationTargetConfigurations']:
        return pulumi.get(self, "audit_notification_target_configurations")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[str]:
        """
        The ARN of the role that grants permission to AWS IoT to access information about your devices, policies, certificates and other items as required when performing an audit.
        """
        return pulumi.get(self, "role_arn")


class AwaitableGetAccountAuditConfigurationResult(GetAccountAuditConfigurationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAccountAuditConfigurationResult(
            audit_check_configurations=self.audit_check_configurations,
            audit_notification_target_configurations=self.audit_notification_target_configurations,
            role_arn=self.role_arn)


def get_account_audit_configuration(account_id: Optional[str] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAccountAuditConfigurationResult:
    """
    Configures the Device Defender audit settings for this account. Settings include how audit notifications are sent and which audit checks are enabled or disabled.


    :param str account_id: Your 12-digit account ID (used as the primary identifier for the CloudFormation resource).
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:iot:getAccountAuditConfiguration', __args__, opts=opts, typ=GetAccountAuditConfigurationResult).value

    return AwaitableGetAccountAuditConfigurationResult(
        audit_check_configurations=__ret__.audit_check_configurations,
        audit_notification_target_configurations=__ret__.audit_notification_target_configurations,
        role_arn=__ret__.role_arn)


@_utilities.lift_output_func(get_account_audit_configuration)
def get_account_audit_configuration_output(account_id: Optional[pulumi.Input[str]] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAccountAuditConfigurationResult]:
    """
    Configures the Device Defender audit settings for this account. Settings include how audit notifications are sent and which audit checks are enabled or disabled.


    :param str account_id: Your 12-digit account ID (used as the primary identifier for the CloudFormation resource).
    """
    ...
