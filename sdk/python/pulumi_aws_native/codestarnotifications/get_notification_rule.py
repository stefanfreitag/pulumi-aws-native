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
    'GetNotificationRuleResult',
    'AwaitableGetNotificationRuleResult',
    'get_notification_rule',
    'get_notification_rule_output',
]

@pulumi.output_type
class GetNotificationRuleResult:
    def __init__(__self__, arn=None, created_by=None, detail_type=None, event_type_ids=None, name=None, status=None, tags=None, targets=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if created_by and not isinstance(created_by, str):
            raise TypeError("Expected argument 'created_by' to be a str")
        pulumi.set(__self__, "created_by", created_by)
        if detail_type and not isinstance(detail_type, str):
            raise TypeError("Expected argument 'detail_type' to be a str")
        pulumi.set(__self__, "detail_type", detail_type)
        if event_type_ids and not isinstance(event_type_ids, list):
            raise TypeError("Expected argument 'event_type_ids' to be a list")
        pulumi.set(__self__, "event_type_ids", event_type_ids)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if targets and not isinstance(targets, list):
            raise TypeError("Expected argument 'targets' to be a list")
        pulumi.set(__self__, "targets", targets)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[str]:
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="detailType")
    def detail_type(self) -> Optional['NotificationRuleDetailType']:
        return pulumi.get(self, "detail_type")

    @property
    @pulumi.getter(name="eventTypeIds")
    def event_type_ids(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "event_type_ids")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def status(self) -> Optional['NotificationRuleStatus']:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Any]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def targets(self) -> Optional[Sequence['outputs.NotificationRuleTarget']]:
        return pulumi.get(self, "targets")


class AwaitableGetNotificationRuleResult(GetNotificationRuleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNotificationRuleResult(
            arn=self.arn,
            created_by=self.created_by,
            detail_type=self.detail_type,
            event_type_ids=self.event_type_ids,
            name=self.name,
            status=self.status,
            tags=self.tags,
            targets=self.targets)


def get_notification_rule(arn: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNotificationRuleResult:
    """
    Resource Type definition for AWS::CodeStarNotifications::NotificationRule
    """
    __args__ = dict()
    __args__['arn'] = arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:codestarnotifications:getNotificationRule', __args__, opts=opts, typ=GetNotificationRuleResult).value

    return AwaitableGetNotificationRuleResult(
        arn=__ret__.arn,
        created_by=__ret__.created_by,
        detail_type=__ret__.detail_type,
        event_type_ids=__ret__.event_type_ids,
        name=__ret__.name,
        status=__ret__.status,
        tags=__ret__.tags,
        targets=__ret__.targets)


@_utilities.lift_output_func(get_notification_rule)
def get_notification_rule_output(arn: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNotificationRuleResult]:
    """
    Resource Type definition for AWS::CodeStarNotifications::NotificationRule
    """
    ...
