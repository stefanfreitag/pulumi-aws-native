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

__all__ = ['PolicyArgs', 'Policy']

@pulumi.input_type
class PolicyArgs:
    def __init__(__self__, *,
                 definition: pulumi.Input[Union['PolicyDefinition0PropertiesArgs', 'PolicyDefinition1PropertiesArgs']],
                 policy_store_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a Policy resource.
        """
        pulumi.set(__self__, "definition", definition)
        pulumi.set(__self__, "policy_store_id", policy_store_id)

    @property
    @pulumi.getter
    def definition(self) -> pulumi.Input[Union['PolicyDefinition0PropertiesArgs', 'PolicyDefinition1PropertiesArgs']]:
        return pulumi.get(self, "definition")

    @definition.setter
    def definition(self, value: pulumi.Input[Union['PolicyDefinition0PropertiesArgs', 'PolicyDefinition1PropertiesArgs']]):
        pulumi.set(self, "definition", value)

    @property
    @pulumi.getter(name="policyStoreId")
    def policy_store_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "policy_store_id")

    @policy_store_id.setter
    def policy_store_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "policy_store_id", value)


class Policy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 definition: Optional[pulumi.Input[Union[pulumi.InputType['PolicyDefinition0PropertiesArgs'], pulumi.InputType['PolicyDefinition1PropertiesArgs']]]] = None,
                 policy_store_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Definition of AWS::VerifiedPermissions::Policy Resource Type

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Definition of AWS::VerifiedPermissions::Policy Resource Type

        :param str resource_name: The name of the resource.
        :param PolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 definition: Optional[pulumi.Input[Union[pulumi.InputType['PolicyDefinition0PropertiesArgs'], pulumi.InputType['PolicyDefinition1PropertiesArgs']]]] = None,
                 policy_store_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PolicyArgs.__new__(PolicyArgs)

            if definition is None and not opts.urn:
                raise TypeError("Missing required property 'definition'")
            __props__.__dict__["definition"] = definition
            if policy_store_id is None and not opts.urn:
                raise TypeError("Missing required property 'policy_store_id'")
            __props__.__dict__["policy_store_id"] = policy_store_id
            __props__.__dict__["policy_id"] = None
            __props__.__dict__["policy_type"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["policy_store_id"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Policy, __self__).__init__(
            'aws-native:verifiedpermissions:Policy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Policy':
        """
        Get an existing Policy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PolicyArgs.__new__(PolicyArgs)

        __props__.__dict__["definition"] = None
        __props__.__dict__["policy_id"] = None
        __props__.__dict__["policy_store_id"] = None
        __props__.__dict__["policy_type"] = None
        return Policy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def definition(self) -> pulumi.Output[Any]:
        return pulumi.get(self, "definition")

    @property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "policy_id")

    @property
    @pulumi.getter(name="policyStoreId")
    def policy_store_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "policy_store_id")

    @property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> pulumi.Output['PolicyType']:
        return pulumi.get(self, "policy_type")

