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

__all__ = ['RotationArgs', 'Rotation']

@pulumi.input_type
class RotationArgs:
    def __init__(__self__, *,
                 contact_ids: pulumi.Input[Sequence[pulumi.Input[str]]],
                 recurrence: pulumi.Input['RotationRecurrenceSettingsArgs'],
                 start_time: pulumi.Input[str],
                 time_zone_id: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a Rotation resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] contact_ids: Members of the rotation
        :param pulumi.Input[str] start_time: Start time of the first shift of Oncall Schedule
        :param pulumi.Input[str] time_zone_id: TimeZone Identifier for the Oncall Schedule
        :param pulumi.Input[str] name: Name of the Rotation
        """
        pulumi.set(__self__, "contact_ids", contact_ids)
        pulumi.set(__self__, "recurrence", recurrence)
        pulumi.set(__self__, "start_time", start_time)
        pulumi.set(__self__, "time_zone_id", time_zone_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="contactIds")
    def contact_ids(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        Members of the rotation
        """
        return pulumi.get(self, "contact_ids")

    @contact_ids.setter
    def contact_ids(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "contact_ids", value)

    @property
    @pulumi.getter
    def recurrence(self) -> pulumi.Input['RotationRecurrenceSettingsArgs']:
        return pulumi.get(self, "recurrence")

    @recurrence.setter
    def recurrence(self, value: pulumi.Input['RotationRecurrenceSettingsArgs']):
        pulumi.set(self, "recurrence", value)

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> pulumi.Input[str]:
        """
        Start time of the first shift of Oncall Schedule
        """
        return pulumi.get(self, "start_time")

    @start_time.setter
    def start_time(self, value: pulumi.Input[str]):
        pulumi.set(self, "start_time", value)

    @property
    @pulumi.getter(name="timeZoneId")
    def time_zone_id(self) -> pulumi.Input[str]:
        """
        TimeZone Identifier for the Oncall Schedule
        """
        return pulumi.get(self, "time_zone_id")

    @time_zone_id.setter
    def time_zone_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "time_zone_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Rotation
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)


class Rotation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 contact_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 recurrence: Optional[pulumi.Input[pulumi.InputType['RotationRecurrenceSettingsArgs']]] = None,
                 start_time: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 time_zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::SSMContacts::Rotation.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] contact_ids: Members of the rotation
        :param pulumi.Input[str] name: Name of the Rotation
        :param pulumi.Input[str] start_time: Start time of the first shift of Oncall Schedule
        :param pulumi.Input[str] time_zone_id: TimeZone Identifier for the Oncall Schedule
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RotationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::SSMContacts::Rotation.

        :param str resource_name: The name of the resource.
        :param RotationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RotationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 contact_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 recurrence: Optional[pulumi.Input[pulumi.InputType['RotationRecurrenceSettingsArgs']]] = None,
                 start_time: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 time_zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RotationArgs.__new__(RotationArgs)

            if contact_ids is None and not opts.urn:
                raise TypeError("Missing required property 'contact_ids'")
            __props__.__dict__["contact_ids"] = contact_ids
            __props__.__dict__["name"] = name
            if recurrence is None and not opts.urn:
                raise TypeError("Missing required property 'recurrence'")
            __props__.__dict__["recurrence"] = recurrence
            if start_time is None and not opts.urn:
                raise TypeError("Missing required property 'start_time'")
            __props__.__dict__["start_time"] = start_time
            __props__.__dict__["tags"] = tags
            if time_zone_id is None and not opts.urn:
                raise TypeError("Missing required property 'time_zone_id'")
            __props__.__dict__["time_zone_id"] = time_zone_id
            __props__.__dict__["arn"] = None
        super(Rotation, __self__).__init__(
            'aws-native:ssmcontacts:Rotation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Rotation':
        """
        Get an existing Rotation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = RotationArgs.__new__(RotationArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["contact_ids"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["recurrence"] = None
        __props__.__dict__["start_time"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["time_zone_id"] = None
        return Rotation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the rotation.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="contactIds")
    def contact_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        Members of the rotation
        """
        return pulumi.get(self, "contact_ids")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the Rotation
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def recurrence(self) -> pulumi.Output['outputs.RotationRecurrenceSettings']:
        return pulumi.get(self, "recurrence")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> pulumi.Output[str]:
        """
        Start time of the first shift of Oncall Schedule
        """
        return pulumi.get(self, "start_time")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="timeZoneId")
    def time_zone_id(self) -> pulumi.Output[str]:
        """
        TimeZone Identifier for the Oncall Schedule
        """
        return pulumi.get(self, "time_zone_id")

