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
from ._enums import *
from ._inputs import *

__all__ = ['NetworkInsightsAnalysisArgs', 'NetworkInsightsAnalysis']

@pulumi.input_type
class NetworkInsightsAnalysisArgs:
    def __init__(__self__, *,
                 network_insights_path_id: pulumi.Input[str],
                 additional_accounts: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 filter_in_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['NetworkInsightsAnalysisTagArgs']]]] = None):
        """
        The set of arguments for constructing a NetworkInsightsAnalysis resource.
        """
        NetworkInsightsAnalysisArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            network_insights_path_id=network_insights_path_id,
            additional_accounts=additional_accounts,
            filter_in_arns=filter_in_arns,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             network_insights_path_id: pulumi.Input[str],
             additional_accounts: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             filter_in_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             tags: Optional[pulumi.Input[Sequence[pulumi.Input['NetworkInsightsAnalysisTagArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("network_insights_path_id", network_insights_path_id)
        if additional_accounts is not None:
            _setter("additional_accounts", additional_accounts)
        if filter_in_arns is not None:
            _setter("filter_in_arns", filter_in_arns)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter(name="networkInsightsPathId")
    def network_insights_path_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "network_insights_path_id")

    @network_insights_path_id.setter
    def network_insights_path_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "network_insights_path_id", value)

    @property
    @pulumi.getter(name="additionalAccounts")
    def additional_accounts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "additional_accounts")

    @additional_accounts.setter
    def additional_accounts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "additional_accounts", value)

    @property
    @pulumi.getter(name="filterInArns")
    def filter_in_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "filter_in_arns")

    @filter_in_arns.setter
    def filter_in_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "filter_in_arns", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['NetworkInsightsAnalysisTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['NetworkInsightsAnalysisTagArgs']]]]):
        pulumi.set(self, "tags", value)


class NetworkInsightsAnalysis(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 additional_accounts: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 filter_in_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 network_insights_path_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkInsightsAnalysisTagArgs']]]]] = None,
                 __props__=None):
        """
        Resource schema for AWS::EC2::NetworkInsightsAnalysis

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NetworkInsightsAnalysisArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource schema for AWS::EC2::NetworkInsightsAnalysis

        :param str resource_name: The name of the resource.
        :param NetworkInsightsAnalysisArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NetworkInsightsAnalysisArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            NetworkInsightsAnalysisArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 additional_accounts: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 filter_in_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 network_insights_path_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkInsightsAnalysisTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NetworkInsightsAnalysisArgs.__new__(NetworkInsightsAnalysisArgs)

            __props__.__dict__["additional_accounts"] = additional_accounts
            __props__.__dict__["filter_in_arns"] = filter_in_arns
            if network_insights_path_id is None and not opts.urn:
                raise TypeError("Missing required property 'network_insights_path_id'")
            __props__.__dict__["network_insights_path_id"] = network_insights_path_id
            __props__.__dict__["tags"] = tags
            __props__.__dict__["alternate_path_hints"] = None
            __props__.__dict__["explanations"] = None
            __props__.__dict__["forward_path_components"] = None
            __props__.__dict__["network_insights_analysis_arn"] = None
            __props__.__dict__["network_insights_analysis_id"] = None
            __props__.__dict__["network_path_found"] = None
            __props__.__dict__["return_path_components"] = None
            __props__.__dict__["start_date"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["status_message"] = None
            __props__.__dict__["suggested_accounts"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["filter_in_arns[*]", "network_insights_path_id"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(NetworkInsightsAnalysis, __self__).__init__(
            'aws-native:ec2:NetworkInsightsAnalysis',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'NetworkInsightsAnalysis':
        """
        Get an existing NetworkInsightsAnalysis resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = NetworkInsightsAnalysisArgs.__new__(NetworkInsightsAnalysisArgs)

        __props__.__dict__["additional_accounts"] = None
        __props__.__dict__["alternate_path_hints"] = None
        __props__.__dict__["explanations"] = None
        __props__.__dict__["filter_in_arns"] = None
        __props__.__dict__["forward_path_components"] = None
        __props__.__dict__["network_insights_analysis_arn"] = None
        __props__.__dict__["network_insights_analysis_id"] = None
        __props__.__dict__["network_insights_path_id"] = None
        __props__.__dict__["network_path_found"] = None
        __props__.__dict__["return_path_components"] = None
        __props__.__dict__["start_date"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["status_message"] = None
        __props__.__dict__["suggested_accounts"] = None
        __props__.__dict__["tags"] = None
        return NetworkInsightsAnalysis(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="additionalAccounts")
    def additional_accounts(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "additional_accounts")

    @property
    @pulumi.getter(name="alternatePathHints")
    def alternate_path_hints(self) -> pulumi.Output[Sequence['outputs.NetworkInsightsAnalysisAlternatePathHint']]:
        return pulumi.get(self, "alternate_path_hints")

    @property
    @pulumi.getter
    def explanations(self) -> pulumi.Output[Sequence['outputs.NetworkInsightsAnalysisExplanation']]:
        return pulumi.get(self, "explanations")

    @property
    @pulumi.getter(name="filterInArns")
    def filter_in_arns(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "filter_in_arns")

    @property
    @pulumi.getter(name="forwardPathComponents")
    def forward_path_components(self) -> pulumi.Output[Sequence['outputs.NetworkInsightsAnalysisPathComponent']]:
        return pulumi.get(self, "forward_path_components")

    @property
    @pulumi.getter(name="networkInsightsAnalysisArn")
    def network_insights_analysis_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "network_insights_analysis_arn")

    @property
    @pulumi.getter(name="networkInsightsAnalysisId")
    def network_insights_analysis_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "network_insights_analysis_id")

    @property
    @pulumi.getter(name="networkInsightsPathId")
    def network_insights_path_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "network_insights_path_id")

    @property
    @pulumi.getter(name="networkPathFound")
    def network_path_found(self) -> pulumi.Output[bool]:
        return pulumi.get(self, "network_path_found")

    @property
    @pulumi.getter(name="returnPathComponents")
    def return_path_components(self) -> pulumi.Output[Sequence['outputs.NetworkInsightsAnalysisPathComponent']]:
        return pulumi.get(self, "return_path_components")

    @property
    @pulumi.getter(name="startDate")
    def start_date(self) -> pulumi.Output[str]:
        return pulumi.get(self, "start_date")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output['NetworkInsightsAnalysisStatus']:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> pulumi.Output[str]:
        return pulumi.get(self, "status_message")

    @property
    @pulumi.getter(name="suggestedAccounts")
    def suggested_accounts(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "suggested_accounts")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.NetworkInsightsAnalysisTag']]]:
        return pulumi.get(self, "tags")

