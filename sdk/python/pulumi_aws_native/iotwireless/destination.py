# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['DestinationArgs', 'Destination']

@pulumi.input_type
class DestinationArgs:
    def __init__(__self__, *,
                 expression: pulumi.Input[str],
                 expression_type: pulumi.Input['DestinationExpressionType'],
                 name: pulumi.Input[str],
                 role_arn: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['DestinationTagArgs']]]] = None):
        """
        The set of arguments for constructing a Destination resource.
        :param pulumi.Input[str] expression: Destination expression
        :param pulumi.Input['DestinationExpressionType'] expression_type: Must be RuleName
        :param pulumi.Input[str] name: Unique name of destination
        :param pulumi.Input[str] role_arn: AWS role ARN that grants access
        :param pulumi.Input[str] description: Destination description
        :param pulumi.Input[Sequence[pulumi.Input['DestinationTagArgs']]] tags: A list of key-value pairs that contain metadata for the destination.
        """
        pulumi.set(__self__, "expression", expression)
        pulumi.set(__self__, "expression_type", expression_type)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "role_arn", role_arn)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def expression(self) -> pulumi.Input[str]:
        """
        Destination expression
        """
        return pulumi.get(self, "expression")

    @expression.setter
    def expression(self, value: pulumi.Input[str]):
        pulumi.set(self, "expression", value)

    @property
    @pulumi.getter(name="expressionType")
    def expression_type(self) -> pulumi.Input['DestinationExpressionType']:
        """
        Must be RuleName
        """
        return pulumi.get(self, "expression_type")

    @expression_type.setter
    def expression_type(self, value: pulumi.Input['DestinationExpressionType']):
        pulumi.set(self, "expression_type", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        Unique name of destination
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[str]:
        """
        AWS role ARN that grants access
        """
        return pulumi.get(self, "role_arn")

    @role_arn.setter
    def role_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "role_arn", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Destination description
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DestinationTagArgs']]]]:
        """
        A list of key-value pairs that contain metadata for the destination.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DestinationTagArgs']]]]):
        pulumi.set(self, "tags", value)


class Destination(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 expression: Optional[pulumi.Input[str]] = None,
                 expression_type: Optional[pulumi.Input['DestinationExpressionType']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DestinationTagArgs']]]]] = None,
                 __props__=None):
        """
        Destination's resource schema demonstrating some basic constructs and validation rules.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Destination description
        :param pulumi.Input[str] expression: Destination expression
        :param pulumi.Input['DestinationExpressionType'] expression_type: Must be RuleName
        :param pulumi.Input[str] name: Unique name of destination
        :param pulumi.Input[str] role_arn: AWS role ARN that grants access
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DestinationTagArgs']]]] tags: A list of key-value pairs that contain metadata for the destination.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DestinationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Destination's resource schema demonstrating some basic constructs and validation rules.

        :param str resource_name: The name of the resource.
        :param DestinationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DestinationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 expression: Optional[pulumi.Input[str]] = None,
                 expression_type: Optional[pulumi.Input['DestinationExpressionType']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DestinationTagArgs']]]]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DestinationArgs.__new__(DestinationArgs)

            __props__.__dict__["description"] = description
            if expression is None and not opts.urn:
                raise TypeError("Missing required property 'expression'")
            __props__.__dict__["expression"] = expression
            if expression_type is None and not opts.urn:
                raise TypeError("Missing required property 'expression_type'")
            __props__.__dict__["expression_type"] = expression_type
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            if role_arn is None and not opts.urn:
                raise TypeError("Missing required property 'role_arn'")
            __props__.__dict__["role_arn"] = role_arn
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
        super(Destination, __self__).__init__(
            'aws-native:iotwireless:Destination',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Destination':
        """
        Get an existing Destination resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DestinationArgs.__new__(DestinationArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["expression"] = None
        __props__.__dict__["expression_type"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["role_arn"] = None
        __props__.__dict__["tags"] = None
        return Destination(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        Destination arn. Returned after successful create.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Destination description
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def expression(self) -> pulumi.Output[str]:
        """
        Destination expression
        """
        return pulumi.get(self, "expression")

    @property
    @pulumi.getter(name="expressionType")
    def expression_type(self) -> pulumi.Output['DestinationExpressionType']:
        """
        Must be RuleName
        """
        return pulumi.get(self, "expression_type")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Unique name of destination
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[str]:
        """
        AWS role ARN that grants access
        """
        return pulumi.get(self, "role_arn")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.DestinationTag']]]:
        """
        A list of key-value pairs that contain metadata for the destination.
        """
        return pulumi.get(self, "tags")

