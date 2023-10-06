# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['DataQualityRulesetArgs', 'DataQualityRuleset']

@pulumi.input_type
class DataQualityRulesetArgs:
    def __init__(__self__, *,
                 client_token: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 ruleset: Optional[pulumi.Input[str]] = None,
                 tags: Optional[Any] = None,
                 target_table: Optional[pulumi.Input['DataQualityRulesetDataQualityTargetTableArgs']] = None):
        """
        The set of arguments for constructing a DataQualityRuleset resource.
        """
        DataQualityRulesetArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            client_token=client_token,
            description=description,
            name=name,
            ruleset=ruleset,
            tags=tags,
            target_table=target_table,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             client_token: Optional[pulumi.Input[str]] = None,
             description: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             ruleset: Optional[pulumi.Input[str]] = None,
             tags: Optional[Any] = None,
             target_table: Optional[pulumi.Input['DataQualityRulesetDataQualityTargetTableArgs']] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if client_token is not None:
            _setter("client_token", client_token)
        if description is not None:
            _setter("description", description)
        if name is not None:
            _setter("name", name)
        if ruleset is not None:
            _setter("ruleset", ruleset)
        if tags is not None:
            _setter("tags", tags)
        if target_table is not None:
            _setter("target_table", target_table)

    @property
    @pulumi.getter(name="clientToken")
    def client_token(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "client_token")

    @client_token.setter
    def client_token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_token", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def ruleset(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "ruleset")

    @ruleset.setter
    def ruleset(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ruleset", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[Any]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[Any]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="targetTable")
    def target_table(self) -> Optional[pulumi.Input['DataQualityRulesetDataQualityTargetTableArgs']]:
        return pulumi.get(self, "target_table")

    @target_table.setter
    def target_table(self, value: Optional[pulumi.Input['DataQualityRulesetDataQualityTargetTableArgs']]):
        pulumi.set(self, "target_table", value)


warnings.warn("""DataQualityRuleset is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class DataQualityRuleset(pulumi.CustomResource):
    warnings.warn("""DataQualityRuleset is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 client_token: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 ruleset: Optional[pulumi.Input[str]] = None,
                 tags: Optional[Any] = None,
                 target_table: Optional[pulumi.Input[pulumi.InputType['DataQualityRulesetDataQualityTargetTableArgs']]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Glue::DataQualityRuleset

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[DataQualityRulesetArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Glue::DataQualityRuleset

        :param str resource_name: The name of the resource.
        :param DataQualityRulesetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DataQualityRulesetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            DataQualityRulesetArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 client_token: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 ruleset: Optional[pulumi.Input[str]] = None,
                 tags: Optional[Any] = None,
                 target_table: Optional[pulumi.Input[pulumi.InputType['DataQualityRulesetDataQualityTargetTableArgs']]] = None,
                 __props__=None):
        pulumi.log.warn("""DataQualityRuleset is deprecated: DataQualityRuleset is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DataQualityRulesetArgs.__new__(DataQualityRulesetArgs)

            __props__.__dict__["client_token"] = client_token
            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            __props__.__dict__["ruleset"] = ruleset
            __props__.__dict__["tags"] = tags
            if target_table is not None and not isinstance(target_table, DataQualityRulesetDataQualityTargetTableArgs):
                target_table = target_table or {}
                def _setter(key, value):
                    target_table[key] = value
                DataQualityRulesetDataQualityTargetTableArgs._configure(_setter, **target_table)
            __props__.__dict__["target_table"] = target_table
        super(DataQualityRuleset, __self__).__init__(
            'aws-native:glue:DataQualityRuleset',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DataQualityRuleset':
        """
        Get an existing DataQualityRuleset resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DataQualityRulesetArgs.__new__(DataQualityRulesetArgs)

        __props__.__dict__["client_token"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["ruleset"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["target_table"] = None
        return DataQualityRuleset(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clientToken")
    def client_token(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "client_token")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def ruleset(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "ruleset")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Any]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="targetTable")
    def target_table(self) -> pulumi.Output[Optional['outputs.DataQualityRulesetDataQualityTargetTable']]:
        return pulumi.get(self, "target_table")

