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
    'GetMicrosoftTeamsChannelConfigurationResult',
    'AwaitableGetMicrosoftTeamsChannelConfigurationResult',
    'get_microsoft_teams_channel_configuration',
    'get_microsoft_teams_channel_configuration_output',
]

@pulumi.output_type
class GetMicrosoftTeamsChannelConfigurationResult:
    def __init__(__self__, arn=None, guardrail_policies=None, iam_role_arn=None, logging_level=None, sns_topic_arns=None, teams_channel_id=None, user_role_required=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if guardrail_policies and not isinstance(guardrail_policies, list):
            raise TypeError("Expected argument 'guardrail_policies' to be a list")
        pulumi.set(__self__, "guardrail_policies", guardrail_policies)
        if iam_role_arn and not isinstance(iam_role_arn, str):
            raise TypeError("Expected argument 'iam_role_arn' to be a str")
        pulumi.set(__self__, "iam_role_arn", iam_role_arn)
        if logging_level and not isinstance(logging_level, str):
            raise TypeError("Expected argument 'logging_level' to be a str")
        pulumi.set(__self__, "logging_level", logging_level)
        if sns_topic_arns and not isinstance(sns_topic_arns, list):
            raise TypeError("Expected argument 'sns_topic_arns' to be a list")
        pulumi.set(__self__, "sns_topic_arns", sns_topic_arns)
        if teams_channel_id and not isinstance(teams_channel_id, str):
            raise TypeError("Expected argument 'teams_channel_id' to be a str")
        pulumi.set(__self__, "teams_channel_id", teams_channel_id)
        if user_role_required and not isinstance(user_role_required, bool):
            raise TypeError("Expected argument 'user_role_required' to be a bool")
        pulumi.set(__self__, "user_role_required", user_role_required)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        Amazon Resource Name (ARN) of the configuration
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="guardrailPolicies")
    def guardrail_policies(self) -> Optional[Sequence[str]]:
        """
        The list of IAM policy ARNs that are applied as channel guardrails. The AWS managed 'AdministratorAccess' policy is applied as a default if this is not set.
        """
        return pulumi.get(self, "guardrail_policies")

    @property
    @pulumi.getter(name="iamRoleArn")
    def iam_role_arn(self) -> Optional[str]:
        """
        The ARN of the IAM role that defines the permissions for AWS Chatbot
        """
        return pulumi.get(self, "iam_role_arn")

    @property
    @pulumi.getter(name="loggingLevel")
    def logging_level(self) -> Optional[str]:
        """
        Specifies the logging level for this configuration:ERROR,INFO or NONE. This property affects the log entries pushed to Amazon CloudWatch logs
        """
        return pulumi.get(self, "logging_level")

    @property
    @pulumi.getter(name="snsTopicArns")
    def sns_topic_arns(self) -> Optional[Sequence[str]]:
        """
        ARNs of SNS topics which delivers notifications to AWS Chatbot, for example CloudWatch alarm notifications.
        """
        return pulumi.get(self, "sns_topic_arns")

    @property
    @pulumi.getter(name="teamsChannelId")
    def teams_channel_id(self) -> Optional[str]:
        """
        The id of the Microsoft Teams channel
        """
        return pulumi.get(self, "teams_channel_id")

    @property
    @pulumi.getter(name="userRoleRequired")
    def user_role_required(self) -> Optional[bool]:
        """
        Enables use of a user role requirement in your chat configuration
        """
        return pulumi.get(self, "user_role_required")


class AwaitableGetMicrosoftTeamsChannelConfigurationResult(GetMicrosoftTeamsChannelConfigurationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMicrosoftTeamsChannelConfigurationResult(
            arn=self.arn,
            guardrail_policies=self.guardrail_policies,
            iam_role_arn=self.iam_role_arn,
            logging_level=self.logging_level,
            sns_topic_arns=self.sns_topic_arns,
            teams_channel_id=self.teams_channel_id,
            user_role_required=self.user_role_required)


def get_microsoft_teams_channel_configuration(arn: Optional[str] = None,
                                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMicrosoftTeamsChannelConfigurationResult:
    """
    Resource schema for AWS::Chatbot::MicrosoftTeamsChannelConfiguration.


    :param str arn: Amazon Resource Name (ARN) of the configuration
    """
    __args__ = dict()
    __args__['arn'] = arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:chatbot:getMicrosoftTeamsChannelConfiguration', __args__, opts=opts, typ=GetMicrosoftTeamsChannelConfigurationResult).value

    return AwaitableGetMicrosoftTeamsChannelConfigurationResult(
        arn=pulumi.get(__ret__, 'arn'),
        guardrail_policies=pulumi.get(__ret__, 'guardrail_policies'),
        iam_role_arn=pulumi.get(__ret__, 'iam_role_arn'),
        logging_level=pulumi.get(__ret__, 'logging_level'),
        sns_topic_arns=pulumi.get(__ret__, 'sns_topic_arns'),
        teams_channel_id=pulumi.get(__ret__, 'teams_channel_id'),
        user_role_required=pulumi.get(__ret__, 'user_role_required'))


@_utilities.lift_output_func(get_microsoft_teams_channel_configuration)
def get_microsoft_teams_channel_configuration_output(arn: Optional[pulumi.Input[str]] = None,
                                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetMicrosoftTeamsChannelConfigurationResult]:
    """
    Resource schema for AWS::Chatbot::MicrosoftTeamsChannelConfiguration.


    :param str arn: Amazon Resource Name (ARN) of the configuration
    """
    ...
