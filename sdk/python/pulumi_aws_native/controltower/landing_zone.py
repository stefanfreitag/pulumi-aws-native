# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from .. import _inputs as _root_inputs
from .. import outputs as _root_outputs
from ._enums import *

__all__ = ['LandingZoneArgs', 'LandingZone']

@pulumi.input_type
class LandingZoneArgs:
    def __init__(__self__, *,
                 manifest: Any,
                 version: pulumi.Input[str],
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a LandingZone resource.
        :param Any manifest: Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::ControlTower::LandingZone` for more information about the expected schema for this property.
        """
        pulumi.set(__self__, "manifest", manifest)
        pulumi.set(__self__, "version", version)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def manifest(self) -> Any:
        """
        Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::ControlTower::LandingZone` for more information about the expected schema for this property.
        """
        return pulumi.get(self, "manifest")

    @manifest.setter
    def manifest(self, value: Any):
        pulumi.set(self, "manifest", value)

    @property
    @pulumi.getter
    def version(self) -> pulumi.Input[str]:
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: pulumi.Input[str]):
        pulumi.set(self, "version", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)


class LandingZone(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 manifest: Optional[Any] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Definition of AWS::ControlTower::LandingZone Resource Type

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param Any manifest: Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::ControlTower::LandingZone` for more information about the expected schema for this property.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LandingZoneArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Definition of AWS::ControlTower::LandingZone Resource Type

        :param str resource_name: The name of the resource.
        :param LandingZoneArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LandingZoneArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 manifest: Optional[Any] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LandingZoneArgs.__new__(LandingZoneArgs)

            if manifest is None and not opts.urn:
                raise TypeError("Missing required property 'manifest'")
            __props__.__dict__["manifest"] = manifest
            __props__.__dict__["tags"] = tags
            if version is None and not opts.urn:
                raise TypeError("Missing required property 'version'")
            __props__.__dict__["version"] = version
            __props__.__dict__["arn"] = None
            __props__.__dict__["drift_status"] = None
            __props__.__dict__["landing_zone_identifier"] = None
            __props__.__dict__["latest_available_version"] = None
            __props__.__dict__["status"] = None
        super(LandingZone, __self__).__init__(
            'aws-native:controltower:LandingZone',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'LandingZone':
        """
        Get an existing LandingZone resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = LandingZoneArgs.__new__(LandingZoneArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["drift_status"] = None
        __props__.__dict__["landing_zone_identifier"] = None
        __props__.__dict__["latest_available_version"] = None
        __props__.__dict__["manifest"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["version"] = None
        return LandingZone(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="driftStatus")
    def drift_status(self) -> pulumi.Output['LandingZoneDriftStatus']:
        return pulumi.get(self, "drift_status")

    @property
    @pulumi.getter(name="landingZoneIdentifier")
    def landing_zone_identifier(self) -> pulumi.Output[str]:
        return pulumi.get(self, "landing_zone_identifier")

    @property
    @pulumi.getter(name="latestAvailableVersion")
    def latest_available_version(self) -> pulumi.Output[str]:
        return pulumi.get(self, "latest_available_version")

    @property
    @pulumi.getter
    def manifest(self) -> pulumi.Output[Any]:
        """
        Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::ControlTower::LandingZone` for more information about the expected schema for this property.
        """
        return pulumi.get(self, "manifest")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output['LandingZoneStatus']:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[str]:
        return pulumi.get(self, "version")

