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

__all__ = ['AnalyzerArgs', 'Analyzer']

@pulumi.input_type
class AnalyzerArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 analyzer_configuration: Optional[pulumi.Input['AnalyzerConfigurationPropertiesArgs']] = None,
                 analyzer_name: Optional[pulumi.Input[str]] = None,
                 archive_rules: Optional[pulumi.Input[Sequence[pulumi.Input['AnalyzerArchiveRuleArgs']]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['AnalyzerTagArgs']]]] = None):
        """
        The set of arguments for constructing a Analyzer resource.
        :param pulumi.Input[str] type: The type of the analyzer, must be one of ACCOUNT, ORGANIZATION, ACCOUNT_UNUSED_ACCESS or ORGANIZATION_UNUSED_ACCESS
        :param pulumi.Input['AnalyzerConfigurationPropertiesArgs'] analyzer_configuration: The configuration for the analyzer
        :param pulumi.Input[str] analyzer_name: Analyzer name
        :param pulumi.Input[Sequence[pulumi.Input['AnalyzerTagArgs']]] tags: An array of key-value pairs to apply to this resource.
        """
        pulumi.set(__self__, "type", type)
        if analyzer_configuration is not None:
            pulumi.set(__self__, "analyzer_configuration", analyzer_configuration)
        if analyzer_name is not None:
            pulumi.set(__self__, "analyzer_name", analyzer_name)
        if archive_rules is not None:
            pulumi.set(__self__, "archive_rules", archive_rules)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The type of the analyzer, must be one of ACCOUNT, ORGANIZATION, ACCOUNT_UNUSED_ACCESS or ORGANIZATION_UNUSED_ACCESS
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="analyzerConfiguration")
    def analyzer_configuration(self) -> Optional[pulumi.Input['AnalyzerConfigurationPropertiesArgs']]:
        """
        The configuration for the analyzer
        """
        return pulumi.get(self, "analyzer_configuration")

    @analyzer_configuration.setter
    def analyzer_configuration(self, value: Optional[pulumi.Input['AnalyzerConfigurationPropertiesArgs']]):
        pulumi.set(self, "analyzer_configuration", value)

    @property
    @pulumi.getter(name="analyzerName")
    def analyzer_name(self) -> Optional[pulumi.Input[str]]:
        """
        Analyzer name
        """
        return pulumi.get(self, "analyzer_name")

    @analyzer_name.setter
    def analyzer_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "analyzer_name", value)

    @property
    @pulumi.getter(name="archiveRules")
    def archive_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AnalyzerArchiveRuleArgs']]]]:
        return pulumi.get(self, "archive_rules")

    @archive_rules.setter
    def archive_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AnalyzerArchiveRuleArgs']]]]):
        pulumi.set(self, "archive_rules", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AnalyzerTagArgs']]]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AnalyzerTagArgs']]]]):
        pulumi.set(self, "tags", value)


class Analyzer(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 analyzer_configuration: Optional[pulumi.Input[pulumi.InputType['AnalyzerConfigurationPropertiesArgs']]] = None,
                 analyzer_name: Optional[pulumi.Input[str]] = None,
                 archive_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AnalyzerArchiveRuleArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AnalyzerTagArgs']]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The AWS::AccessAnalyzer::Analyzer type specifies an analyzer of the user's account

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['AnalyzerConfigurationPropertiesArgs']] analyzer_configuration: The configuration for the analyzer
        :param pulumi.Input[str] analyzer_name: Analyzer name
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AnalyzerTagArgs']]]] tags: An array of key-value pairs to apply to this resource.
        :param pulumi.Input[str] type: The type of the analyzer, must be one of ACCOUNT, ORGANIZATION, ACCOUNT_UNUSED_ACCESS or ORGANIZATION_UNUSED_ACCESS
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AnalyzerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The AWS::AccessAnalyzer::Analyzer type specifies an analyzer of the user's account

        :param str resource_name: The name of the resource.
        :param AnalyzerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AnalyzerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 analyzer_configuration: Optional[pulumi.Input[pulumi.InputType['AnalyzerConfigurationPropertiesArgs']]] = None,
                 analyzer_name: Optional[pulumi.Input[str]] = None,
                 archive_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AnalyzerArchiveRuleArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AnalyzerTagArgs']]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AnalyzerArgs.__new__(AnalyzerArgs)

            __props__.__dict__["analyzer_configuration"] = analyzer_configuration
            __props__.__dict__["analyzer_name"] = analyzer_name
            __props__.__dict__["archive_rules"] = archive_rules
            __props__.__dict__["tags"] = tags
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
            __props__.__dict__["arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["analyzer_configuration", "analyzer_name", "type"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Analyzer, __self__).__init__(
            'aws-native:accessanalyzer:Analyzer',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Analyzer':
        """
        Get an existing Analyzer resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AnalyzerArgs.__new__(AnalyzerArgs)

        __props__.__dict__["analyzer_configuration"] = None
        __props__.__dict__["analyzer_name"] = None
        __props__.__dict__["archive_rules"] = None
        __props__.__dict__["arn"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return Analyzer(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="analyzerConfiguration")
    def analyzer_configuration(self) -> pulumi.Output[Optional['outputs.AnalyzerConfigurationProperties']]:
        """
        The configuration for the analyzer
        """
        return pulumi.get(self, "analyzer_configuration")

    @property
    @pulumi.getter(name="analyzerName")
    def analyzer_name(self) -> pulumi.Output[Optional[str]]:
        """
        Analyzer name
        """
        return pulumi.get(self, "analyzer_name")

    @property
    @pulumi.getter(name="archiveRules")
    def archive_rules(self) -> pulumi.Output[Optional[Sequence['outputs.AnalyzerArchiveRule']]]:
        return pulumi.get(self, "archive_rules")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        Amazon Resource Name (ARN) of the analyzer
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.AnalyzerTag']]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the analyzer, must be one of ACCOUNT, ORGANIZATION, ACCOUNT_UNUSED_ACCESS or ORGANIZATION_UNUSED_ACCESS
        """
        return pulumi.get(self, "type")

