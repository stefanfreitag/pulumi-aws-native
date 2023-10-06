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
    'GetSiteToSiteVpnAttachmentResult',
    'AwaitableGetSiteToSiteVpnAttachmentResult',
    'get_site_to_site_vpn_attachment',
    'get_site_to_site_vpn_attachment_output',
]

@pulumi.output_type
class GetSiteToSiteVpnAttachmentResult:
    def __init__(__self__, attachment_id=None, attachment_policy_rule_number=None, attachment_type=None, core_network_arn=None, created_at=None, edge_location=None, owner_account_id=None, proposed_segment_change=None, resource_arn=None, segment_name=None, state=None, tags=None, updated_at=None):
        if attachment_id and not isinstance(attachment_id, str):
            raise TypeError("Expected argument 'attachment_id' to be a str")
        pulumi.set(__self__, "attachment_id", attachment_id)
        if attachment_policy_rule_number and not isinstance(attachment_policy_rule_number, int):
            raise TypeError("Expected argument 'attachment_policy_rule_number' to be a int")
        pulumi.set(__self__, "attachment_policy_rule_number", attachment_policy_rule_number)
        if attachment_type and not isinstance(attachment_type, str):
            raise TypeError("Expected argument 'attachment_type' to be a str")
        pulumi.set(__self__, "attachment_type", attachment_type)
        if core_network_arn and not isinstance(core_network_arn, str):
            raise TypeError("Expected argument 'core_network_arn' to be a str")
        pulumi.set(__self__, "core_network_arn", core_network_arn)
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if edge_location and not isinstance(edge_location, str):
            raise TypeError("Expected argument 'edge_location' to be a str")
        pulumi.set(__self__, "edge_location", edge_location)
        if owner_account_id and not isinstance(owner_account_id, str):
            raise TypeError("Expected argument 'owner_account_id' to be a str")
        pulumi.set(__self__, "owner_account_id", owner_account_id)
        if proposed_segment_change and not isinstance(proposed_segment_change, dict):
            raise TypeError("Expected argument 'proposed_segment_change' to be a dict")
        pulumi.set(__self__, "proposed_segment_change", proposed_segment_change)
        if resource_arn and not isinstance(resource_arn, str):
            raise TypeError("Expected argument 'resource_arn' to be a str")
        pulumi.set(__self__, "resource_arn", resource_arn)
        if segment_name and not isinstance(segment_name, str):
            raise TypeError("Expected argument 'segment_name' to be a str")
        pulumi.set(__self__, "segment_name", segment_name)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if updated_at and not isinstance(updated_at, str):
            raise TypeError("Expected argument 'updated_at' to be a str")
        pulumi.set(__self__, "updated_at", updated_at)

    @property
    @pulumi.getter(name="attachmentId")
    def attachment_id(self) -> Optional[str]:
        """
        The ID of the attachment.
        """
        return pulumi.get(self, "attachment_id")

    @property
    @pulumi.getter(name="attachmentPolicyRuleNumber")
    def attachment_policy_rule_number(self) -> Optional[int]:
        """
        The policy rule number associated with the attachment.
        """
        return pulumi.get(self, "attachment_policy_rule_number")

    @property
    @pulumi.getter(name="attachmentType")
    def attachment_type(self) -> Optional[str]:
        """
        The type of attachment.
        """
        return pulumi.get(self, "attachment_type")

    @property
    @pulumi.getter(name="coreNetworkArn")
    def core_network_arn(self) -> Optional[str]:
        """
        The ARN of a core network for the VPC attachment.
        """
        return pulumi.get(self, "core_network_arn")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[str]:
        """
        Creation time of the attachment.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="edgeLocation")
    def edge_location(self) -> Optional[str]:
        """
        The Region where the edge is located.
        """
        return pulumi.get(self, "edge_location")

    @property
    @pulumi.getter(name="ownerAccountId")
    def owner_account_id(self) -> Optional[str]:
        """
        Owner account of the attachment.
        """
        return pulumi.get(self, "owner_account_id")

    @property
    @pulumi.getter(name="proposedSegmentChange")
    def proposed_segment_change(self) -> Optional['outputs.SiteToSiteVpnAttachmentProposedSegmentChange']:
        """
        The attachment to move from one segment to another.
        """
        return pulumi.get(self, "proposed_segment_change")

    @property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> Optional[str]:
        """
        The ARN of the Resource.
        """
        return pulumi.get(self, "resource_arn")

    @property
    @pulumi.getter(name="segmentName")
    def segment_name(self) -> Optional[str]:
        """
        The name of the segment that attachment is in.
        """
        return pulumi.get(self, "segment_name")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The state of the attachment.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.SiteToSiteVpnAttachmentTag']]:
        """
        Tags for the attachment.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> Optional[str]:
        """
        Last update time of the attachment.
        """
        return pulumi.get(self, "updated_at")


class AwaitableGetSiteToSiteVpnAttachmentResult(GetSiteToSiteVpnAttachmentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSiteToSiteVpnAttachmentResult(
            attachment_id=self.attachment_id,
            attachment_policy_rule_number=self.attachment_policy_rule_number,
            attachment_type=self.attachment_type,
            core_network_arn=self.core_network_arn,
            created_at=self.created_at,
            edge_location=self.edge_location,
            owner_account_id=self.owner_account_id,
            proposed_segment_change=self.proposed_segment_change,
            resource_arn=self.resource_arn,
            segment_name=self.segment_name,
            state=self.state,
            tags=self.tags,
            updated_at=self.updated_at)


def get_site_to_site_vpn_attachment(attachment_id: Optional[str] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSiteToSiteVpnAttachmentResult:
    """
    AWS::NetworkManager::SiteToSiteVpnAttachment Resource Type definition.


    :param str attachment_id: The ID of the attachment.
    """
    __args__ = dict()
    __args__['attachmentId'] = attachment_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:networkmanager:getSiteToSiteVpnAttachment', __args__, opts=opts, typ=GetSiteToSiteVpnAttachmentResult).value

    return AwaitableGetSiteToSiteVpnAttachmentResult(
        attachment_id=pulumi.get(__ret__, 'attachment_id'),
        attachment_policy_rule_number=pulumi.get(__ret__, 'attachment_policy_rule_number'),
        attachment_type=pulumi.get(__ret__, 'attachment_type'),
        core_network_arn=pulumi.get(__ret__, 'core_network_arn'),
        created_at=pulumi.get(__ret__, 'created_at'),
        edge_location=pulumi.get(__ret__, 'edge_location'),
        owner_account_id=pulumi.get(__ret__, 'owner_account_id'),
        proposed_segment_change=pulumi.get(__ret__, 'proposed_segment_change'),
        resource_arn=pulumi.get(__ret__, 'resource_arn'),
        segment_name=pulumi.get(__ret__, 'segment_name'),
        state=pulumi.get(__ret__, 'state'),
        tags=pulumi.get(__ret__, 'tags'),
        updated_at=pulumi.get(__ret__, 'updated_at'))


@_utilities.lift_output_func(get_site_to_site_vpn_attachment)
def get_site_to_site_vpn_attachment_output(attachment_id: Optional[pulumi.Input[str]] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSiteToSiteVpnAttachmentResult]:
    """
    AWS::NetworkManager::SiteToSiteVpnAttachment Resource Type definition.


    :param str attachment_id: The ID of the attachment.
    """
    ...
