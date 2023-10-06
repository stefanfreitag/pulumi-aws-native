# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['PolicyTemplateArgs', 'PolicyTemplate']

@pulumi.input_type
class PolicyTemplateArgs:
    def __init__(__self__, *,
                 statement: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 policy_store_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a PolicyTemplate resource.
        """
        PolicyTemplateArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            statement=statement,
            description=description,
            policy_store_id=policy_store_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             statement: pulumi.Input[str],
             description: Optional[pulumi.Input[str]] = None,
             policy_store_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("statement", statement)
        if description is not None:
            _setter("description", description)
        if policy_store_id is not None:
            _setter("policy_store_id", policy_store_id)

    @property
    @pulumi.getter
    def statement(self) -> pulumi.Input[str]:
        return pulumi.get(self, "statement")

    @statement.setter
    def statement(self, value: pulumi.Input[str]):
        pulumi.set(self, "statement", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="policyStoreId")
    def policy_store_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "policy_store_id")

    @policy_store_id.setter
    def policy_store_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_store_id", value)


class PolicyTemplate(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 policy_store_id: Optional[pulumi.Input[str]] = None,
                 statement: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Definition of AWS::VerifiedPermissions::PolicyTemplate Resource Type

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PolicyTemplateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Definition of AWS::VerifiedPermissions::PolicyTemplate Resource Type

        :param str resource_name: The name of the resource.
        :param PolicyTemplateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PolicyTemplateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            PolicyTemplateArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 policy_store_id: Optional[pulumi.Input[str]] = None,
                 statement: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PolicyTemplateArgs.__new__(PolicyTemplateArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["policy_store_id"] = policy_store_id
            if statement is None and not opts.urn:
                raise TypeError("Missing required property 'statement'")
            __props__.__dict__["statement"] = statement
            __props__.__dict__["policy_template_id"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["policy_store_id"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(PolicyTemplate, __self__).__init__(
            'aws-native:verifiedpermissions:PolicyTemplate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PolicyTemplate':
        """
        Get an existing PolicyTemplate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PolicyTemplateArgs.__new__(PolicyTemplateArgs)

        __props__.__dict__["description"] = None
        __props__.__dict__["policy_store_id"] = None
        __props__.__dict__["policy_template_id"] = None
        __props__.__dict__["statement"] = None
        return PolicyTemplate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="policyStoreId")
    def policy_store_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "policy_store_id")

    @property
    @pulumi.getter(name="policyTemplateId")
    def policy_template_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "policy_template_id")

    @property
    @pulumi.getter
    def statement(self) -> pulumi.Output[str]:
        return pulumi.get(self, "statement")

