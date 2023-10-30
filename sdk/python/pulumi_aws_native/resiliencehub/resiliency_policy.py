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

__all__ = ['ResiliencyPolicyArgs', 'ResiliencyPolicy']

@pulumi.input_type
class ResiliencyPolicyArgs:
    def __init__(__self__, *,
                 policy: pulumi.Input['ResiliencyPolicyPolicyMapArgs'],
                 policy_name: pulumi.Input[str],
                 tier: pulumi.Input['ResiliencyPolicyTier'],
                 data_location_constraint: Optional[pulumi.Input['ResiliencyPolicyDataLocationConstraint']] = None,
                 policy_description: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input['ResiliencyPolicyTagMapArgs']] = None):
        """
        The set of arguments for constructing a ResiliencyPolicy resource.
        :param pulumi.Input[str] policy_name: Name of Resiliency Policy.
        :param pulumi.Input['ResiliencyPolicyTier'] tier: Resiliency Policy Tier.
        :param pulumi.Input['ResiliencyPolicyDataLocationConstraint'] data_location_constraint: Data Location Constraint of the Policy.
        :param pulumi.Input[str] policy_description: Description of Resiliency Policy.
        """
        pulumi.set(__self__, "policy", policy)
        pulumi.set(__self__, "policy_name", policy_name)
        pulumi.set(__self__, "tier", tier)
        if data_location_constraint is not None:
            pulumi.set(__self__, "data_location_constraint", data_location_constraint)
        if policy_description is not None:
            pulumi.set(__self__, "policy_description", policy_description)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def policy(self) -> pulumi.Input['ResiliencyPolicyPolicyMapArgs']:
        return pulumi.get(self, "policy")

    @policy.setter
    def policy(self, value: pulumi.Input['ResiliencyPolicyPolicyMapArgs']):
        pulumi.set(self, "policy", value)

    @property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> pulumi.Input[str]:
        """
        Name of Resiliency Policy.
        """
        return pulumi.get(self, "policy_name")

    @policy_name.setter
    def policy_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "policy_name", value)

    @property
    @pulumi.getter
    def tier(self) -> pulumi.Input['ResiliencyPolicyTier']:
        """
        Resiliency Policy Tier.
        """
        return pulumi.get(self, "tier")

    @tier.setter
    def tier(self, value: pulumi.Input['ResiliencyPolicyTier']):
        pulumi.set(self, "tier", value)

    @property
    @pulumi.getter(name="dataLocationConstraint")
    def data_location_constraint(self) -> Optional[pulumi.Input['ResiliencyPolicyDataLocationConstraint']]:
        """
        Data Location Constraint of the Policy.
        """
        return pulumi.get(self, "data_location_constraint")

    @data_location_constraint.setter
    def data_location_constraint(self, value: Optional[pulumi.Input['ResiliencyPolicyDataLocationConstraint']]):
        pulumi.set(self, "data_location_constraint", value)

    @property
    @pulumi.getter(name="policyDescription")
    def policy_description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of Resiliency Policy.
        """
        return pulumi.get(self, "policy_description")

    @policy_description.setter
    def policy_description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_description", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input['ResiliencyPolicyTagMapArgs']]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input['ResiliencyPolicyTagMapArgs']]):
        pulumi.set(self, "tags", value)


class ResiliencyPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data_location_constraint: Optional[pulumi.Input['ResiliencyPolicyDataLocationConstraint']] = None,
                 policy: Optional[pulumi.Input[pulumi.InputType['ResiliencyPolicyPolicyMapArgs']]] = None,
                 policy_description: Optional[pulumi.Input[str]] = None,
                 policy_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[pulumi.InputType['ResiliencyPolicyTagMapArgs']]] = None,
                 tier: Optional[pulumi.Input['ResiliencyPolicyTier']] = None,
                 __props__=None):
        """
        Resource Type Definition for Resiliency Policy.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input['ResiliencyPolicyDataLocationConstraint'] data_location_constraint: Data Location Constraint of the Policy.
        :param pulumi.Input[str] policy_description: Description of Resiliency Policy.
        :param pulumi.Input[str] policy_name: Name of Resiliency Policy.
        :param pulumi.Input['ResiliencyPolicyTier'] tier: Resiliency Policy Tier.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ResiliencyPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type Definition for Resiliency Policy.

        :param str resource_name: The name of the resource.
        :param ResiliencyPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ResiliencyPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data_location_constraint: Optional[pulumi.Input['ResiliencyPolicyDataLocationConstraint']] = None,
                 policy: Optional[pulumi.Input[pulumi.InputType['ResiliencyPolicyPolicyMapArgs']]] = None,
                 policy_description: Optional[pulumi.Input[str]] = None,
                 policy_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[pulumi.InputType['ResiliencyPolicyTagMapArgs']]] = None,
                 tier: Optional[pulumi.Input['ResiliencyPolicyTier']] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ResiliencyPolicyArgs.__new__(ResiliencyPolicyArgs)

            __props__.__dict__["data_location_constraint"] = data_location_constraint
            if policy is None and not opts.urn:
                raise TypeError("Missing required property 'policy'")
            __props__.__dict__["policy"] = policy
            __props__.__dict__["policy_description"] = policy_description
            if policy_name is None and not opts.urn:
                raise TypeError("Missing required property 'policy_name'")
            __props__.__dict__["policy_name"] = policy_name
            __props__.__dict__["tags"] = tags
            if tier is None and not opts.urn:
                raise TypeError("Missing required property 'tier'")
            __props__.__dict__["tier"] = tier
            __props__.__dict__["policy_arn"] = None
        super(ResiliencyPolicy, __self__).__init__(
            'aws-native:resiliencehub:ResiliencyPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ResiliencyPolicy':
        """
        Get an existing ResiliencyPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ResiliencyPolicyArgs.__new__(ResiliencyPolicyArgs)

        __props__.__dict__["data_location_constraint"] = None
        __props__.__dict__["policy"] = None
        __props__.__dict__["policy_arn"] = None
        __props__.__dict__["policy_description"] = None
        __props__.__dict__["policy_name"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["tier"] = None
        return ResiliencyPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dataLocationConstraint")
    def data_location_constraint(self) -> pulumi.Output[Optional['ResiliencyPolicyDataLocationConstraint']]:
        """
        Data Location Constraint of the Policy.
        """
        return pulumi.get(self, "data_location_constraint")

    @property
    @pulumi.getter
    def policy(self) -> pulumi.Output['outputs.ResiliencyPolicyPolicyMap']:
        return pulumi.get(self, "policy")

    @property
    @pulumi.getter(name="policyArn")
    def policy_arn(self) -> pulumi.Output[str]:
        """
        Amazon Resource Name (ARN) of the Resiliency Policy.
        """
        return pulumi.get(self, "policy_arn")

    @property
    @pulumi.getter(name="policyDescription")
    def policy_description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of Resiliency Policy.
        """
        return pulumi.get(self, "policy_description")

    @property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> pulumi.Output[str]:
        """
        Name of Resiliency Policy.
        """
        return pulumi.get(self, "policy_name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional['outputs.ResiliencyPolicyTagMap']]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def tier(self) -> pulumi.Output['ResiliencyPolicyTier']:
        """
        Resiliency Policy Tier.
        """
        return pulumi.get(self, "tier")

