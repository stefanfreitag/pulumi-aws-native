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
    'GetCampaignResult',
    'AwaitableGetCampaignResult',
    'get_campaign',
    'get_campaign_output',
]

@pulumi.output_type
class GetCampaignResult:
    def __init__(__self__, additional_treatments=None, arn=None, campaign_hook=None, campaign_id=None, custom_delivery_configuration=None, description=None, holdout_percent=None, is_paused=None, limits=None, message_configuration=None, name=None, priority=None, schedule=None, segment_id=None, segment_version=None, tags=None, template_configuration=None, treatment_description=None, treatment_name=None):
        if additional_treatments and not isinstance(additional_treatments, list):
            raise TypeError("Expected argument 'additional_treatments' to be a list")
        pulumi.set(__self__, "additional_treatments", additional_treatments)
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if campaign_hook and not isinstance(campaign_hook, dict):
            raise TypeError("Expected argument 'campaign_hook' to be a dict")
        pulumi.set(__self__, "campaign_hook", campaign_hook)
        if campaign_id and not isinstance(campaign_id, str):
            raise TypeError("Expected argument 'campaign_id' to be a str")
        pulumi.set(__self__, "campaign_id", campaign_id)
        if custom_delivery_configuration and not isinstance(custom_delivery_configuration, dict):
            raise TypeError("Expected argument 'custom_delivery_configuration' to be a dict")
        pulumi.set(__self__, "custom_delivery_configuration", custom_delivery_configuration)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if holdout_percent and not isinstance(holdout_percent, int):
            raise TypeError("Expected argument 'holdout_percent' to be a int")
        pulumi.set(__self__, "holdout_percent", holdout_percent)
        if is_paused and not isinstance(is_paused, bool):
            raise TypeError("Expected argument 'is_paused' to be a bool")
        pulumi.set(__self__, "is_paused", is_paused)
        if limits and not isinstance(limits, dict):
            raise TypeError("Expected argument 'limits' to be a dict")
        pulumi.set(__self__, "limits", limits)
        if message_configuration and not isinstance(message_configuration, dict):
            raise TypeError("Expected argument 'message_configuration' to be a dict")
        pulumi.set(__self__, "message_configuration", message_configuration)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if priority and not isinstance(priority, int):
            raise TypeError("Expected argument 'priority' to be a int")
        pulumi.set(__self__, "priority", priority)
        if schedule and not isinstance(schedule, dict):
            raise TypeError("Expected argument 'schedule' to be a dict")
        pulumi.set(__self__, "schedule", schedule)
        if segment_id and not isinstance(segment_id, str):
            raise TypeError("Expected argument 'segment_id' to be a str")
        pulumi.set(__self__, "segment_id", segment_id)
        if segment_version and not isinstance(segment_version, int):
            raise TypeError("Expected argument 'segment_version' to be a int")
        pulumi.set(__self__, "segment_version", segment_version)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if template_configuration and not isinstance(template_configuration, dict):
            raise TypeError("Expected argument 'template_configuration' to be a dict")
        pulumi.set(__self__, "template_configuration", template_configuration)
        if treatment_description and not isinstance(treatment_description, str):
            raise TypeError("Expected argument 'treatment_description' to be a str")
        pulumi.set(__self__, "treatment_description", treatment_description)
        if treatment_name and not isinstance(treatment_name, str):
            raise TypeError("Expected argument 'treatment_name' to be a str")
        pulumi.set(__self__, "treatment_name", treatment_name)

    @property
    @pulumi.getter(name="additionalTreatments")
    def additional_treatments(self) -> Optional[Sequence['outputs.CampaignWriteTreatmentResource']]:
        return pulumi.get(self, "additional_treatments")

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="campaignHook")
    def campaign_hook(self) -> Optional['outputs.CampaignHook']:
        return pulumi.get(self, "campaign_hook")

    @property
    @pulumi.getter(name="campaignId")
    def campaign_id(self) -> Optional[str]:
        return pulumi.get(self, "campaign_id")

    @property
    @pulumi.getter(name="customDeliveryConfiguration")
    def custom_delivery_configuration(self) -> Optional['outputs.CampaignCustomDeliveryConfiguration']:
        return pulumi.get(self, "custom_delivery_configuration")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="holdoutPercent")
    def holdout_percent(self) -> Optional[int]:
        return pulumi.get(self, "holdout_percent")

    @property
    @pulumi.getter(name="isPaused")
    def is_paused(self) -> Optional[bool]:
        return pulumi.get(self, "is_paused")

    @property
    @pulumi.getter
    def limits(self) -> Optional['outputs.CampaignLimits']:
        return pulumi.get(self, "limits")

    @property
    @pulumi.getter(name="messageConfiguration")
    def message_configuration(self) -> Optional['outputs.CampaignMessageConfiguration']:
        return pulumi.get(self, "message_configuration")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def priority(self) -> Optional[int]:
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter
    def schedule(self) -> Optional['outputs.CampaignSchedule']:
        return pulumi.get(self, "schedule")

    @property
    @pulumi.getter(name="segmentId")
    def segment_id(self) -> Optional[str]:
        return pulumi.get(self, "segment_id")

    @property
    @pulumi.getter(name="segmentVersion")
    def segment_version(self) -> Optional[int]:
        return pulumi.get(self, "segment_version")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Any]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="templateConfiguration")
    def template_configuration(self) -> Optional['outputs.CampaignTemplateConfiguration']:
        return pulumi.get(self, "template_configuration")

    @property
    @pulumi.getter(name="treatmentDescription")
    def treatment_description(self) -> Optional[str]:
        return pulumi.get(self, "treatment_description")

    @property
    @pulumi.getter(name="treatmentName")
    def treatment_name(self) -> Optional[str]:
        return pulumi.get(self, "treatment_name")


class AwaitableGetCampaignResult(GetCampaignResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCampaignResult(
            additional_treatments=self.additional_treatments,
            arn=self.arn,
            campaign_hook=self.campaign_hook,
            campaign_id=self.campaign_id,
            custom_delivery_configuration=self.custom_delivery_configuration,
            description=self.description,
            holdout_percent=self.holdout_percent,
            is_paused=self.is_paused,
            limits=self.limits,
            message_configuration=self.message_configuration,
            name=self.name,
            priority=self.priority,
            schedule=self.schedule,
            segment_id=self.segment_id,
            segment_version=self.segment_version,
            tags=self.tags,
            template_configuration=self.template_configuration,
            treatment_description=self.treatment_description,
            treatment_name=self.treatment_name)


def get_campaign(campaign_id: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCampaignResult:
    """
    Resource Type definition for AWS::Pinpoint::Campaign
    """
    __args__ = dict()
    __args__['campaignId'] = campaign_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:pinpoint:getCampaign', __args__, opts=opts, typ=GetCampaignResult).value

    return AwaitableGetCampaignResult(
        additional_treatments=__ret__.additional_treatments,
        arn=__ret__.arn,
        campaign_hook=__ret__.campaign_hook,
        campaign_id=__ret__.campaign_id,
        custom_delivery_configuration=__ret__.custom_delivery_configuration,
        description=__ret__.description,
        holdout_percent=__ret__.holdout_percent,
        is_paused=__ret__.is_paused,
        limits=__ret__.limits,
        message_configuration=__ret__.message_configuration,
        name=__ret__.name,
        priority=__ret__.priority,
        schedule=__ret__.schedule,
        segment_id=__ret__.segment_id,
        segment_version=__ret__.segment_version,
        tags=__ret__.tags,
        template_configuration=__ret__.template_configuration,
        treatment_description=__ret__.treatment_description,
        treatment_name=__ret__.treatment_name)


@_utilities.lift_output_func(get_campaign)
def get_campaign_output(campaign_id: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCampaignResult]:
    """
    Resource Type definition for AWS::Pinpoint::Campaign
    """
    ...
