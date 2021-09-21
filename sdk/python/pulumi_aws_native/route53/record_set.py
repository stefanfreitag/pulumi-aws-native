# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['RecordSetArgs', 'RecordSet']

@pulumi.input_type
class RecordSetArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 type: pulumi.Input[str],
                 alias_target: Optional[pulumi.Input['RecordSetAliasTargetArgs']] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 failover: Optional[pulumi.Input[str]] = None,
                 geo_location: Optional[pulumi.Input['RecordSetGeoLocationArgs']] = None,
                 health_check_id: Optional[pulumi.Input[str]] = None,
                 hosted_zone_id: Optional[pulumi.Input[str]] = None,
                 hosted_zone_name: Optional[pulumi.Input[str]] = None,
                 multi_value_answer: Optional[pulumi.Input[bool]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 resource_records: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 set_identifier: Optional[pulumi.Input[str]] = None,
                 t_tl: Optional[pulumi.Input[str]] = None,
                 weight: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a RecordSet resource.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "type", type)
        if alias_target is not None:
            pulumi.set(__self__, "alias_target", alias_target)
        if comment is not None:
            pulumi.set(__self__, "comment", comment)
        if failover is not None:
            pulumi.set(__self__, "failover", failover)
        if geo_location is not None:
            pulumi.set(__self__, "geo_location", geo_location)
        if health_check_id is not None:
            pulumi.set(__self__, "health_check_id", health_check_id)
        if hosted_zone_id is not None:
            pulumi.set(__self__, "hosted_zone_id", hosted_zone_id)
        if hosted_zone_name is not None:
            pulumi.set(__self__, "hosted_zone_name", hosted_zone_name)
        if multi_value_answer is not None:
            pulumi.set(__self__, "multi_value_answer", multi_value_answer)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if resource_records is not None:
            pulumi.set(__self__, "resource_records", resource_records)
        if set_identifier is not None:
            pulumi.set(__self__, "set_identifier", set_identifier)
        if t_tl is not None:
            pulumi.set(__self__, "t_tl", t_tl)
        if weight is not None:
            pulumi.set(__self__, "weight", weight)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="aliasTarget")
    def alias_target(self) -> Optional[pulumi.Input['RecordSetAliasTargetArgs']]:
        return pulumi.get(self, "alias_target")

    @alias_target.setter
    def alias_target(self, value: Optional[pulumi.Input['RecordSetAliasTargetArgs']]):
        pulumi.set(self, "alias_target", value)

    @property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "comment")

    @comment.setter
    def comment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "comment", value)

    @property
    @pulumi.getter
    def failover(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "failover")

    @failover.setter
    def failover(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "failover", value)

    @property
    @pulumi.getter(name="geoLocation")
    def geo_location(self) -> Optional[pulumi.Input['RecordSetGeoLocationArgs']]:
        return pulumi.get(self, "geo_location")

    @geo_location.setter
    def geo_location(self, value: Optional[pulumi.Input['RecordSetGeoLocationArgs']]):
        pulumi.set(self, "geo_location", value)

    @property
    @pulumi.getter(name="healthCheckId")
    def health_check_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "health_check_id")

    @health_check_id.setter
    def health_check_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "health_check_id", value)

    @property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "hosted_zone_id")

    @hosted_zone_id.setter
    def hosted_zone_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hosted_zone_id", value)

    @property
    @pulumi.getter(name="hostedZoneName")
    def hosted_zone_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "hosted_zone_name")

    @hosted_zone_name.setter
    def hosted_zone_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hosted_zone_name", value)

    @property
    @pulumi.getter(name="multiValueAnswer")
    def multi_value_answer(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "multi_value_answer")

    @multi_value_answer.setter
    def multi_value_answer(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "multi_value_answer", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="resourceRecords")
    def resource_records(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "resource_records")

    @resource_records.setter
    def resource_records(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "resource_records", value)

    @property
    @pulumi.getter(name="setIdentifier")
    def set_identifier(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "set_identifier")

    @set_identifier.setter
    def set_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "set_identifier", value)

    @property
    @pulumi.getter(name="tTL")
    def t_tl(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "t_tl")

    @t_tl.setter
    def t_tl(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "t_tl", value)

    @property
    @pulumi.getter
    def weight(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "weight")

    @weight.setter
    def weight(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "weight", value)


warnings.warn("""RecordSet is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class RecordSet(pulumi.CustomResource):
    warnings.warn("""RecordSet is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 alias_target: Optional[pulumi.Input[pulumi.InputType['RecordSetAliasTargetArgs']]] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 failover: Optional[pulumi.Input[str]] = None,
                 geo_location: Optional[pulumi.Input[pulumi.InputType['RecordSetGeoLocationArgs']]] = None,
                 health_check_id: Optional[pulumi.Input[str]] = None,
                 hosted_zone_id: Optional[pulumi.Input[str]] = None,
                 hosted_zone_name: Optional[pulumi.Input[str]] = None,
                 multi_value_answer: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 resource_records: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 set_identifier: Optional[pulumi.Input[str]] = None,
                 t_tl: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 weight: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Route53::RecordSet

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RecordSetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Route53::RecordSet

        :param str resource_name: The name of the resource.
        :param RecordSetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RecordSetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 alias_target: Optional[pulumi.Input[pulumi.InputType['RecordSetAliasTargetArgs']]] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 failover: Optional[pulumi.Input[str]] = None,
                 geo_location: Optional[pulumi.Input[pulumi.InputType['RecordSetGeoLocationArgs']]] = None,
                 health_check_id: Optional[pulumi.Input[str]] = None,
                 hosted_zone_id: Optional[pulumi.Input[str]] = None,
                 hosted_zone_name: Optional[pulumi.Input[str]] = None,
                 multi_value_answer: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 resource_records: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 set_identifier: Optional[pulumi.Input[str]] = None,
                 t_tl: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 weight: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        pulumi.log.warn("""RecordSet is deprecated: RecordSet is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RecordSetArgs.__new__(RecordSetArgs)

            __props__.__dict__["alias_target"] = alias_target
            __props__.__dict__["comment"] = comment
            __props__.__dict__["failover"] = failover
            __props__.__dict__["geo_location"] = geo_location
            __props__.__dict__["health_check_id"] = health_check_id
            __props__.__dict__["hosted_zone_id"] = hosted_zone_id
            __props__.__dict__["hosted_zone_name"] = hosted_zone_name
            __props__.__dict__["multi_value_answer"] = multi_value_answer
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            __props__.__dict__["region"] = region
            __props__.__dict__["resource_records"] = resource_records
            __props__.__dict__["set_identifier"] = set_identifier
            __props__.__dict__["t_tl"] = t_tl
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
            __props__.__dict__["weight"] = weight
        super(RecordSet, __self__).__init__(
            'aws-native:route53:RecordSet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'RecordSet':
        """
        Get an existing RecordSet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = RecordSetArgs.__new__(RecordSetArgs)

        __props__.__dict__["alias_target"] = None
        __props__.__dict__["comment"] = None
        __props__.__dict__["failover"] = None
        __props__.__dict__["geo_location"] = None
        __props__.__dict__["health_check_id"] = None
        __props__.__dict__["hosted_zone_id"] = None
        __props__.__dict__["hosted_zone_name"] = None
        __props__.__dict__["multi_value_answer"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["region"] = None
        __props__.__dict__["resource_records"] = None
        __props__.__dict__["set_identifier"] = None
        __props__.__dict__["t_tl"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["weight"] = None
        return RecordSet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="aliasTarget")
    def alias_target(self) -> pulumi.Output[Optional['outputs.RecordSetAliasTarget']]:
        return pulumi.get(self, "alias_target")

    @property
    @pulumi.getter
    def comment(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "comment")

    @property
    @pulumi.getter
    def failover(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "failover")

    @property
    @pulumi.getter(name="geoLocation")
    def geo_location(self) -> pulumi.Output[Optional['outputs.RecordSetGeoLocation']]:
        return pulumi.get(self, "geo_location")

    @property
    @pulumi.getter(name="healthCheckId")
    def health_check_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "health_check_id")

    @property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "hosted_zone_id")

    @property
    @pulumi.getter(name="hostedZoneName")
    def hosted_zone_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "hosted_zone_name")

    @property
    @pulumi.getter(name="multiValueAnswer")
    def multi_value_answer(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "multi_value_answer")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="resourceRecords")
    def resource_records(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "resource_records")

    @property
    @pulumi.getter(name="setIdentifier")
    def set_identifier(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "set_identifier")

    @property
    @pulumi.getter(name="tTL")
    def t_tl(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "t_tl")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def weight(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "weight")

