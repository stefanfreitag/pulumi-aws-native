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
from .. import _inputs as _root_inputs
from .. import outputs as _root_outputs
from ._enums import *
from ._inputs import *

__all__ = ['TrustAnchorArgs', 'TrustAnchor']

@pulumi.input_type
class TrustAnchorArgs:
    def __init__(__self__, *,
                 source: pulumi.Input['TrustAnchorSourceArgs'],
                 enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notification_settings: Optional[pulumi.Input[Sequence[pulumi.Input['TrustAnchorNotificationSettingArgs']]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a TrustAnchor resource.
        """
        pulumi.set(__self__, "source", source)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if notification_settings is not None:
            pulumi.set(__self__, "notification_settings", notification_settings)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def source(self) -> pulumi.Input['TrustAnchorSourceArgs']:
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: pulumi.Input['TrustAnchorSourceArgs']):
        pulumi.set(self, "source", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="notificationSettings")
    def notification_settings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TrustAnchorNotificationSettingArgs']]]]:
        return pulumi.get(self, "notification_settings")

    @notification_settings.setter
    def notification_settings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TrustAnchorNotificationSettingArgs']]]]):
        pulumi.set(self, "notification_settings", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)


class TrustAnchor(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notification_settings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TrustAnchorNotificationSettingArgs']]]]] = None,
                 source: Optional[pulumi.Input[pulumi.InputType['TrustAnchorSourceArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        """
        Definition of AWS::RolesAnywhere::TrustAnchor Resource Type.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TrustAnchorArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Definition of AWS::RolesAnywhere::TrustAnchor Resource Type.

        :param str resource_name: The name of the resource.
        :param TrustAnchorArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TrustAnchorArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notification_settings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TrustAnchorNotificationSettingArgs']]]]] = None,
                 source: Optional[pulumi.Input[pulumi.InputType['TrustAnchorSourceArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TrustAnchorArgs.__new__(TrustAnchorArgs)

            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["name"] = name
            __props__.__dict__["notification_settings"] = notification_settings
            if source is None and not opts.urn:
                raise TypeError("Missing required property 'source'")
            __props__.__dict__["source"] = source
            __props__.__dict__["tags"] = tags
            __props__.__dict__["trust_anchor_arn"] = None
            __props__.__dict__["trust_anchor_id"] = None
        super(TrustAnchor, __self__).__init__(
            'aws-native:rolesanywhere:TrustAnchor',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'TrustAnchor':
        """
        Get an existing TrustAnchor resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = TrustAnchorArgs.__new__(TrustAnchorArgs)

        __props__.__dict__["enabled"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["notification_settings"] = None
        __props__.__dict__["source"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["trust_anchor_arn"] = None
        __props__.__dict__["trust_anchor_id"] = None
        return TrustAnchor(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="notificationSettings")
    def notification_settings(self) -> pulumi.Output[Optional[Sequence['outputs.TrustAnchorNotificationSetting']]]:
        return pulumi.get(self, "notification_settings")

    @property
    @pulumi.getter
    def source(self) -> pulumi.Output['outputs.TrustAnchorSource']:
        return pulumi.get(self, "source")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="trustAnchorArn")
    def trust_anchor_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "trust_anchor_arn")

    @property
    @pulumi.getter(name="trustAnchorId")
    def trust_anchor_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "trust_anchor_id")

