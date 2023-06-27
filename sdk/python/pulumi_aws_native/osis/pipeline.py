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

__all__ = ['PipelineArgs', 'Pipeline']

@pulumi.input_type
class PipelineArgs:
    def __init__(__self__, *,
                 max_units: pulumi.Input[int],
                 min_units: pulumi.Input[int],
                 pipeline_configuration_body: pulumi.Input[str],
                 log_publishing_options: Optional[pulumi.Input['PipelineLogPublishingOptionsArgs']] = None,
                 pipeline_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['PipelineTagArgs']]]] = None,
                 vpc_options: Optional[pulumi.Input['PipelineVpcOptionsArgs']] = None):
        """
        The set of arguments for constructing a Pipeline resource.
        :param pulumi.Input[int] max_units: The maximum pipeline capacity, in Ingestion Compute Units (ICUs).
        :param pulumi.Input[int] min_units: The minimum pipeline capacity, in Ingestion Compute Units (ICUs).
        :param pulumi.Input[str] pipeline_configuration_body: The Data Prepper pipeline configuration in YAML format.
        :param pulumi.Input[str] pipeline_name: Name of the OpenSearch Ingestion Service pipeline to create. Pipeline names are unique across the pipelines owned by an account within an AWS Region.
        :param pulumi.Input[Sequence[pulumi.Input['PipelineTagArgs']]] tags: An array of key-value pairs to apply to this resource.
        """
        pulumi.set(__self__, "max_units", max_units)
        pulumi.set(__self__, "min_units", min_units)
        pulumi.set(__self__, "pipeline_configuration_body", pipeline_configuration_body)
        if log_publishing_options is not None:
            pulumi.set(__self__, "log_publishing_options", log_publishing_options)
        if pipeline_name is not None:
            pulumi.set(__self__, "pipeline_name", pipeline_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if vpc_options is not None:
            pulumi.set(__self__, "vpc_options", vpc_options)

    @property
    @pulumi.getter(name="maxUnits")
    def max_units(self) -> pulumi.Input[int]:
        """
        The maximum pipeline capacity, in Ingestion Compute Units (ICUs).
        """
        return pulumi.get(self, "max_units")

    @max_units.setter
    def max_units(self, value: pulumi.Input[int]):
        pulumi.set(self, "max_units", value)

    @property
    @pulumi.getter(name="minUnits")
    def min_units(self) -> pulumi.Input[int]:
        """
        The minimum pipeline capacity, in Ingestion Compute Units (ICUs).
        """
        return pulumi.get(self, "min_units")

    @min_units.setter
    def min_units(self, value: pulumi.Input[int]):
        pulumi.set(self, "min_units", value)

    @property
    @pulumi.getter(name="pipelineConfigurationBody")
    def pipeline_configuration_body(self) -> pulumi.Input[str]:
        """
        The Data Prepper pipeline configuration in YAML format.
        """
        return pulumi.get(self, "pipeline_configuration_body")

    @pipeline_configuration_body.setter
    def pipeline_configuration_body(self, value: pulumi.Input[str]):
        pulumi.set(self, "pipeline_configuration_body", value)

    @property
    @pulumi.getter(name="logPublishingOptions")
    def log_publishing_options(self) -> Optional[pulumi.Input['PipelineLogPublishingOptionsArgs']]:
        return pulumi.get(self, "log_publishing_options")

    @log_publishing_options.setter
    def log_publishing_options(self, value: Optional[pulumi.Input['PipelineLogPublishingOptionsArgs']]):
        pulumi.set(self, "log_publishing_options", value)

    @property
    @pulumi.getter(name="pipelineName")
    def pipeline_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the OpenSearch Ingestion Service pipeline to create. Pipeline names are unique across the pipelines owned by an account within an AWS Region.
        """
        return pulumi.get(self, "pipeline_name")

    @pipeline_name.setter
    def pipeline_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pipeline_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PipelineTagArgs']]]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PipelineTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="vpcOptions")
    def vpc_options(self) -> Optional[pulumi.Input['PipelineVpcOptionsArgs']]:
        return pulumi.get(self, "vpc_options")

    @vpc_options.setter
    def vpc_options(self, value: Optional[pulumi.Input['PipelineVpcOptionsArgs']]):
        pulumi.set(self, "vpc_options", value)


class Pipeline(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 log_publishing_options: Optional[pulumi.Input[pulumi.InputType['PipelineLogPublishingOptionsArgs']]] = None,
                 max_units: Optional[pulumi.Input[int]] = None,
                 min_units: Optional[pulumi.Input[int]] = None,
                 pipeline_configuration_body: Optional[pulumi.Input[str]] = None,
                 pipeline_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PipelineTagArgs']]]]] = None,
                 vpc_options: Optional[pulumi.Input[pulumi.InputType['PipelineVpcOptionsArgs']]] = None,
                 __props__=None):
        """
        An OpenSearch Ingestion Service Data Prepper pipeline running Data Prepper.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] max_units: The maximum pipeline capacity, in Ingestion Compute Units (ICUs).
        :param pulumi.Input[int] min_units: The minimum pipeline capacity, in Ingestion Compute Units (ICUs).
        :param pulumi.Input[str] pipeline_configuration_body: The Data Prepper pipeline configuration in YAML format.
        :param pulumi.Input[str] pipeline_name: Name of the OpenSearch Ingestion Service pipeline to create. Pipeline names are unique across the pipelines owned by an account within an AWS Region.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PipelineTagArgs']]]] tags: An array of key-value pairs to apply to this resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PipelineArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An OpenSearch Ingestion Service Data Prepper pipeline running Data Prepper.

        :param str resource_name: The name of the resource.
        :param PipelineArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PipelineArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 log_publishing_options: Optional[pulumi.Input[pulumi.InputType['PipelineLogPublishingOptionsArgs']]] = None,
                 max_units: Optional[pulumi.Input[int]] = None,
                 min_units: Optional[pulumi.Input[int]] = None,
                 pipeline_configuration_body: Optional[pulumi.Input[str]] = None,
                 pipeline_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PipelineTagArgs']]]]] = None,
                 vpc_options: Optional[pulumi.Input[pulumi.InputType['PipelineVpcOptionsArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PipelineArgs.__new__(PipelineArgs)

            __props__.__dict__["log_publishing_options"] = log_publishing_options
            if max_units is None and not opts.urn:
                raise TypeError("Missing required property 'max_units'")
            __props__.__dict__["max_units"] = max_units
            if min_units is None and not opts.urn:
                raise TypeError("Missing required property 'min_units'")
            __props__.__dict__["min_units"] = min_units
            if pipeline_configuration_body is None and not opts.urn:
                raise TypeError("Missing required property 'pipeline_configuration_body'")
            __props__.__dict__["pipeline_configuration_body"] = pipeline_configuration_body
            __props__.__dict__["pipeline_name"] = pipeline_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["vpc_options"] = vpc_options
            __props__.__dict__["ingest_endpoint_urls"] = None
            __props__.__dict__["pipeline_arn"] = None
            __props__.__dict__["vpc_endpoints"] = None
        super(Pipeline, __self__).__init__(
            'aws-native:osis:Pipeline',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Pipeline':
        """
        Get an existing Pipeline resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PipelineArgs.__new__(PipelineArgs)

        __props__.__dict__["ingest_endpoint_urls"] = None
        __props__.__dict__["log_publishing_options"] = None
        __props__.__dict__["max_units"] = None
        __props__.__dict__["min_units"] = None
        __props__.__dict__["pipeline_arn"] = None
        __props__.__dict__["pipeline_configuration_body"] = None
        __props__.__dict__["pipeline_name"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["vpc_endpoints"] = None
        __props__.__dict__["vpc_options"] = None
        return Pipeline(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="ingestEndpointUrls")
    def ingest_endpoint_urls(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of endpoints that can be used for ingesting data into a pipeline
        """
        return pulumi.get(self, "ingest_endpoint_urls")

    @property
    @pulumi.getter(name="logPublishingOptions")
    def log_publishing_options(self) -> pulumi.Output[Optional['outputs.PipelineLogPublishingOptions']]:
        return pulumi.get(self, "log_publishing_options")

    @property
    @pulumi.getter(name="maxUnits")
    def max_units(self) -> pulumi.Output[int]:
        """
        The maximum pipeline capacity, in Ingestion Compute Units (ICUs).
        """
        return pulumi.get(self, "max_units")

    @property
    @pulumi.getter(name="minUnits")
    def min_units(self) -> pulumi.Output[int]:
        """
        The minimum pipeline capacity, in Ingestion Compute Units (ICUs).
        """
        return pulumi.get(self, "min_units")

    @property
    @pulumi.getter(name="pipelineArn")
    def pipeline_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the pipeline.
        """
        return pulumi.get(self, "pipeline_arn")

    @property
    @pulumi.getter(name="pipelineConfigurationBody")
    def pipeline_configuration_body(self) -> pulumi.Output[str]:
        """
        The Data Prepper pipeline configuration in YAML format.
        """
        return pulumi.get(self, "pipeline_configuration_body")

    @property
    @pulumi.getter(name="pipelineName")
    def pipeline_name(self) -> pulumi.Output[str]:
        """
        Name of the OpenSearch Ingestion Service pipeline to create. Pipeline names are unique across the pipelines owned by an account within an AWS Region.
        """
        return pulumi.get(self, "pipeline_name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.PipelineTag']]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="vpcEndpoints")
    def vpc_endpoints(self) -> pulumi.Output[Sequence['outputs.PipelineVpcEndpoint']]:
        """
        The VPC interface endpoints that have access to the pipeline.
        """
        return pulumi.get(self, "vpc_endpoints")

    @property
    @pulumi.getter(name="vpcOptions")
    def vpc_options(self) -> pulumi.Output[Optional['outputs.PipelineVpcOptions']]:
        return pulumi.get(self, "vpc_options")

