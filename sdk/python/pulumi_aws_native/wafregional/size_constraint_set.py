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
from ._inputs import *

__all__ = ['SizeConstraintSetArgs', 'SizeConstraintSet']

@pulumi.input_type
class SizeConstraintSetArgs:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 size_constraints: Optional[pulumi.Input[Sequence[pulumi.Input['SizeConstraintSetSizeConstraintArgs']]]] = None):
        """
        The set of arguments for constructing a SizeConstraintSet resource.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if size_constraints is not None:
            pulumi.set(__self__, "size_constraints", size_constraints)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="sizeConstraints")
    def size_constraints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SizeConstraintSetSizeConstraintArgs']]]]:
        return pulumi.get(self, "size_constraints")

    @size_constraints.setter
    def size_constraints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SizeConstraintSetSizeConstraintArgs']]]]):
        pulumi.set(self, "size_constraints", value)


warnings.warn("""SizeConstraintSet is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class SizeConstraintSet(pulumi.CustomResource):
    warnings.warn("""SizeConstraintSet is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 size_constraints: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SizeConstraintSetSizeConstraintArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::WAFRegional::SizeConstraintSet

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[SizeConstraintSetArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::WAFRegional::SizeConstraintSet

        :param str resource_name: The name of the resource.
        :param SizeConstraintSetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SizeConstraintSetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 size_constraints: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SizeConstraintSetSizeConstraintArgs']]]]] = None,
                 __props__=None):
        pulumi.log.warn("""SizeConstraintSet is deprecated: SizeConstraintSet is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SizeConstraintSetArgs.__new__(SizeConstraintSetArgs)

            __props__.__dict__["name"] = name
            __props__.__dict__["size_constraints"] = size_constraints
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(SizeConstraintSet, __self__).__init__(
            'aws-native:wafregional:SizeConstraintSet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SizeConstraintSet':
        """
        Get an existing SizeConstraintSet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SizeConstraintSetArgs.__new__(SizeConstraintSetArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["size_constraints"] = None
        return SizeConstraintSet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="sizeConstraints")
    def size_constraints(self) -> pulumi.Output[Optional[Sequence['outputs.SizeConstraintSetSizeConstraint']]]:
        return pulumi.get(self, "size_constraints")

