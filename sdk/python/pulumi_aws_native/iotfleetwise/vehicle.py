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
from ._inputs import *

__all__ = ['VehicleArgs', 'Vehicle']

@pulumi.input_type
class VehicleArgs:
    def __init__(__self__, *,
                 decoder_manifest_arn: pulumi.Input[str],
                 model_manifest_arn: pulumi.Input[str],
                 association_behavior: Optional[pulumi.Input['VehicleAssociationBehavior']] = None,
                 attributes: Optional[pulumi.Input['VehicleattributesMapArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['VehicleTagArgs']]]] = None):
        """
        The set of arguments for constructing a Vehicle resource.
        """
        pulumi.set(__self__, "decoder_manifest_arn", decoder_manifest_arn)
        pulumi.set(__self__, "model_manifest_arn", model_manifest_arn)
        if association_behavior is not None:
            pulumi.set(__self__, "association_behavior", association_behavior)
        if attributes is not None:
            pulumi.set(__self__, "attributes", attributes)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="decoderManifestArn")
    def decoder_manifest_arn(self) -> pulumi.Input[str]:
        return pulumi.get(self, "decoder_manifest_arn")

    @decoder_manifest_arn.setter
    def decoder_manifest_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "decoder_manifest_arn", value)

    @property
    @pulumi.getter(name="modelManifestArn")
    def model_manifest_arn(self) -> pulumi.Input[str]:
        return pulumi.get(self, "model_manifest_arn")

    @model_manifest_arn.setter
    def model_manifest_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "model_manifest_arn", value)

    @property
    @pulumi.getter(name="associationBehavior")
    def association_behavior(self) -> Optional[pulumi.Input['VehicleAssociationBehavior']]:
        return pulumi.get(self, "association_behavior")

    @association_behavior.setter
    def association_behavior(self, value: Optional[pulumi.Input['VehicleAssociationBehavior']]):
        pulumi.set(self, "association_behavior", value)

    @property
    @pulumi.getter
    def attributes(self) -> Optional[pulumi.Input['VehicleattributesMapArgs']]:
        return pulumi.get(self, "attributes")

    @attributes.setter
    def attributes(self, value: Optional[pulumi.Input['VehicleattributesMapArgs']]):
        pulumi.set(self, "attributes", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['VehicleTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['VehicleTagArgs']]]]):
        pulumi.set(self, "tags", value)


warnings.warn("""Vehicle is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class Vehicle(pulumi.CustomResource):
    warnings.warn("""Vehicle is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 association_behavior: Optional[pulumi.Input['VehicleAssociationBehavior']] = None,
                 attributes: Optional[pulumi.Input[pulumi.InputType['VehicleattributesMapArgs']]] = None,
                 decoder_manifest_arn: Optional[pulumi.Input[str]] = None,
                 model_manifest_arn: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VehicleTagArgs']]]]] = None,
                 __props__=None):
        """
        Definition of AWS::IoTFleetWise::Vehicle Resource Type

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VehicleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Definition of AWS::IoTFleetWise::Vehicle Resource Type

        :param str resource_name: The name of the resource.
        :param VehicleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VehicleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 association_behavior: Optional[pulumi.Input['VehicleAssociationBehavior']] = None,
                 attributes: Optional[pulumi.Input[pulumi.InputType['VehicleattributesMapArgs']]] = None,
                 decoder_manifest_arn: Optional[pulumi.Input[str]] = None,
                 model_manifest_arn: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VehicleTagArgs']]]]] = None,
                 __props__=None):
        pulumi.log.warn("""Vehicle is deprecated: Vehicle is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VehicleArgs.__new__(VehicleArgs)

            __props__.__dict__["association_behavior"] = association_behavior
            __props__.__dict__["attributes"] = attributes
            if decoder_manifest_arn is None and not opts.urn:
                raise TypeError("Missing required property 'decoder_manifest_arn'")
            __props__.__dict__["decoder_manifest_arn"] = decoder_manifest_arn
            if model_manifest_arn is None and not opts.urn:
                raise TypeError("Missing required property 'model_manifest_arn'")
            __props__.__dict__["model_manifest_arn"] = model_manifest_arn
            __props__.__dict__["name"] = name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
            __props__.__dict__["creation_time"] = None
            __props__.__dict__["last_modification_time"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Vehicle, __self__).__init__(
            'aws-native:iotfleetwise:Vehicle',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Vehicle':
        """
        Get an existing Vehicle resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VehicleArgs.__new__(VehicleArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["association_behavior"] = None
        __props__.__dict__["attributes"] = None
        __props__.__dict__["creation_time"] = None
        __props__.__dict__["decoder_manifest_arn"] = None
        __props__.__dict__["last_modification_time"] = None
        __props__.__dict__["model_manifest_arn"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["tags"] = None
        return Vehicle(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="associationBehavior")
    def association_behavior(self) -> pulumi.Output[Optional['VehicleAssociationBehavior']]:
        return pulumi.get(self, "association_behavior")

    @property
    @pulumi.getter
    def attributes(self) -> pulumi.Output[Optional['outputs.VehicleattributesMap']]:
        return pulumi.get(self, "attributes")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[str]:
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="decoderManifestArn")
    def decoder_manifest_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "decoder_manifest_arn")

    @property
    @pulumi.getter(name="lastModificationTime")
    def last_modification_time(self) -> pulumi.Output[str]:
        return pulumi.get(self, "last_modification_time")

    @property
    @pulumi.getter(name="modelManifestArn")
    def model_manifest_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "model_manifest_arn")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.VehicleTag']]]:
        return pulumi.get(self, "tags")

