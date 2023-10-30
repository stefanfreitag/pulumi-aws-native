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
from ._enums import *

__all__ = [
    'GetResponsePlanResult',
    'AwaitableGetResponsePlanResult',
    'get_response_plan',
    'get_response_plan_output',
]

@pulumi.output_type
class GetResponsePlanResult:
    def __init__(__self__, actions=None, arn=None, chat_channel=None, display_name=None, engagements=None, incident_template=None, integrations=None, tags=None):
        if actions and not isinstance(actions, list):
            raise TypeError("Expected argument 'actions' to be a list")
        pulumi.set(__self__, "actions", actions)
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if chat_channel and not isinstance(chat_channel, dict):
            raise TypeError("Expected argument 'chat_channel' to be a dict")
        pulumi.set(__self__, "chat_channel", chat_channel)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if engagements and not isinstance(engagements, list):
            raise TypeError("Expected argument 'engagements' to be a list")
        pulumi.set(__self__, "engagements", engagements)
        if incident_template and not isinstance(incident_template, dict):
            raise TypeError("Expected argument 'incident_template' to be a dict")
        pulumi.set(__self__, "incident_template", incident_template)
        if integrations and not isinstance(integrations, list):
            raise TypeError("Expected argument 'integrations' to be a list")
        pulumi.set(__self__, "integrations", integrations)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def actions(self) -> Optional[Sequence['outputs.ResponsePlanAction']]:
        """
        The list of actions.
        """
        return pulumi.get(self, "actions")

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        The ARN of the response plan.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="chatChannel")
    def chat_channel(self) -> Optional['outputs.ResponsePlanChatChannel']:
        return pulumi.get(self, "chat_channel")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        The display name of the response plan.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def engagements(self) -> Optional[Sequence[str]]:
        """
        The list of engagements to use.
        """
        return pulumi.get(self, "engagements")

    @property
    @pulumi.getter(name="incidentTemplate")
    def incident_template(self) -> Optional['outputs.ResponsePlanIncidentTemplate']:
        return pulumi.get(self, "incident_template")

    @property
    @pulumi.getter
    def integrations(self) -> Optional[Sequence['outputs.ResponsePlanIntegration']]:
        """
        The list of integrations.
        """
        return pulumi.get(self, "integrations")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.ResponsePlanTag']]:
        """
        The tags to apply to the response plan.
        """
        return pulumi.get(self, "tags")


class AwaitableGetResponsePlanResult(GetResponsePlanResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetResponsePlanResult(
            actions=self.actions,
            arn=self.arn,
            chat_channel=self.chat_channel,
            display_name=self.display_name,
            engagements=self.engagements,
            incident_template=self.incident_template,
            integrations=self.integrations,
            tags=self.tags)


def get_response_plan(arn: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetResponsePlanResult:
    """
    Resource type definition for AWS::SSMIncidents::ResponsePlan


    :param str arn: The ARN of the response plan.
    """
    __args__ = dict()
    __args__['arn'] = arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:ssmincidents:getResponsePlan', __args__, opts=opts, typ=GetResponsePlanResult).value

    return AwaitableGetResponsePlanResult(
        actions=pulumi.get(__ret__, 'actions'),
        arn=pulumi.get(__ret__, 'arn'),
        chat_channel=pulumi.get(__ret__, 'chat_channel'),
        display_name=pulumi.get(__ret__, 'display_name'),
        engagements=pulumi.get(__ret__, 'engagements'),
        incident_template=pulumi.get(__ret__, 'incident_template'),
        integrations=pulumi.get(__ret__, 'integrations'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_response_plan)
def get_response_plan_output(arn: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetResponsePlanResult]:
    """
    Resource type definition for AWS::SSMIncidents::ResponsePlan


    :param str arn: The ARN of the response plan.
    """
    ...
