# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'ContactListTag',
    'ContactListTopic',
]

@pulumi.output_type
class ContactListTag(dict):
    def __init__(__self__, *,
                 key: str,
                 value: str):
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")


@pulumi.output_type
class ContactListTopic(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "defaultSubscriptionStatus":
            suggest = "default_subscription_status"
        elif key == "displayName":
            suggest = "display_name"
        elif key == "topicName":
            suggest = "topic_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ContactListTopic. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ContactListTopic.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ContactListTopic.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 default_subscription_status: str,
                 display_name: str,
                 topic_name: str,
                 description: Optional[str] = None):
        """
        :param str display_name: The display name of the topic.
        :param str topic_name: The name of the topic.
        :param str description: The description of the topic.
        """
        pulumi.set(__self__, "default_subscription_status", default_subscription_status)
        pulumi.set(__self__, "display_name", display_name)
        pulumi.set(__self__, "topic_name", topic_name)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter(name="defaultSubscriptionStatus")
    def default_subscription_status(self) -> str:
        return pulumi.get(self, "default_subscription_status")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The display name of the topic.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="topicName")
    def topic_name(self) -> str:
        """
        The name of the topic.
        """
        return pulumi.get(self, "topic_name")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of the topic.
        """
        return pulumi.get(self, "description")


