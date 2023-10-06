# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = [
    'AccountTag',
    'OrganizationalUnitTag',
    'PolicyTag',
    'ResourcePolicyTag',
]

@pulumi.output_type
class AccountTag(dict):
    """
    A custom key-value pair associated with a resource within your organization.
    """
    def __init__(__self__, *,
                 key: str,
                 value: str):
        """
        A custom key-value pair associated with a resource within your organization.
        :param str key: The key identifier, or name, of the tag.
        :param str value: The string value that's associated with the key of the tag. You can set the value of a tag to an empty string, but you can't set the value of a tag to null.
        """
        AccountTag._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            key=key,
            value=value,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             key: str,
             value: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("key", key)
        _setter("value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The key identifier, or name, of the tag.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The string value that's associated with the key of the tag. You can set the value of a tag to an empty string, but you can't set the value of a tag to null.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class OrganizationalUnitTag(dict):
    """
    A custom key-value pair associated with a resource within your organization.
    """
    def __init__(__self__, *,
                 key: str,
                 value: str):
        """
        A custom key-value pair associated with a resource within your organization.
        :param str key: The key identifier, or name, of the tag.
        :param str value: The string value that's associated with the key of the tag. You can set the value of a tag to an empty string, but you can't set the value of a tag to null.
        """
        OrganizationalUnitTag._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            key=key,
            value=value,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             key: str,
             value: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("key", key)
        _setter("value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The key identifier, or name, of the tag.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The string value that's associated with the key of the tag. You can set the value of a tag to an empty string, but you can't set the value of a tag to null.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class PolicyTag(dict):
    """
    A custom key-value pair associated with a resource within your organization.
    """
    def __init__(__self__, *,
                 key: str,
                 value: str):
        """
        A custom key-value pair associated with a resource within your organization.
        :param str key: The key identifier, or name, of the tag.
        :param str value: The string value that's associated with the key of the tag. You can set the value of a tag to an empty string, but you can't set the value of a tag to null.
        """
        PolicyTag._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            key=key,
            value=value,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             key: str,
             value: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("key", key)
        _setter("value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The key identifier, or name, of the tag.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The string value that's associated with the key of the tag. You can set the value of a tag to an empty string, but you can't set the value of a tag to null.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class ResourcePolicyTag(dict):
    """
    A custom key-value pair associated with a resource within your organization.
    """
    def __init__(__self__, *,
                 key: str,
                 value: str):
        """
        A custom key-value pair associated with a resource within your organization.
        :param str key: The key identifier, or name, of the tag.
        :param str value: The string value that's associated with the key of the tag. You can set the value of a tag to an empty string, but you can't set the value of a tag to null.
        """
        ResourcePolicyTag._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            key=key,
            value=value,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             key: str,
             value: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("key", key)
        _setter("value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The key identifier, or name, of the tag.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The string value that's associated with the key of the tag. You can set the value of a tag to an empty string, but you can't set the value of a tag to null.
        """
        return pulumi.get(self, "value")


