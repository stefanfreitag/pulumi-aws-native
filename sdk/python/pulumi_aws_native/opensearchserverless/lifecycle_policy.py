# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = ['LifecyclePolicyArgs', 'LifecyclePolicy']

@pulumi.input_type
class LifecyclePolicyArgs:
    def __init__(__self__, *,
                 policy: pulumi.Input[str],
                 type: pulumi.Input['LifecyclePolicyType'],
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a LifecyclePolicy resource.
        :param pulumi.Input[str] policy: The JSON policy document that is the content for the policy
        :param pulumi.Input[str] description: The description of the policy
        :param pulumi.Input[str] name: The name of the policy
        """
        pulumi.set(__self__, "policy", policy)
        pulumi.set(__self__, "type", type)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def policy(self) -> pulumi.Input[str]:
        """
        The JSON policy document that is the content for the policy
        """
        return pulumi.get(self, "policy")

    @policy.setter
    def policy(self, value: pulumi.Input[str]):
        pulumi.set(self, "policy", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input['LifecyclePolicyType']:
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input['LifecyclePolicyType']):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the policy
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the policy
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class LifecyclePolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 policy: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input['LifecyclePolicyType']] = None,
                 __props__=None):
        """
        Amazon OpenSearchServerless lifecycle policy resource

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the policy
        :param pulumi.Input[str] name: The name of the policy
        :param pulumi.Input[str] policy: The JSON policy document that is the content for the policy
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LifecyclePolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Amazon OpenSearchServerless lifecycle policy resource

        :param str resource_name: The name of the resource.
        :param LifecyclePolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LifecyclePolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 policy: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input['LifecyclePolicyType']] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LifecyclePolicyArgs.__new__(LifecyclePolicyArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            if policy is None and not opts.urn:
                raise TypeError("Missing required property 'policy'")
            __props__.__dict__["policy"] = policy
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["name", "type"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(LifecyclePolicy, __self__).__init__(
            'aws-native:opensearchserverless:LifecyclePolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'LifecyclePolicy':
        """
        Get an existing LifecyclePolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = LifecyclePolicyArgs.__new__(LifecyclePolicyArgs)

        __props__.__dict__["description"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["policy"] = None
        __props__.__dict__["type"] = None
        return LifecyclePolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the policy
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the policy
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def policy(self) -> pulumi.Output[str]:
        """
        The JSON policy document that is the content for the policy
        """
        return pulumi.get(self, "policy")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output['LifecyclePolicyType']:
        return pulumi.get(self, "type")

