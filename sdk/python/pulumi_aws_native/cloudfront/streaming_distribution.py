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

__all__ = ['StreamingDistributionArgs', 'StreamingDistribution']

@pulumi.input_type
class StreamingDistributionArgs:
    def __init__(__self__, *,
                 streaming_distribution_config: pulumi.Input['StreamingDistributionConfigArgs'],
                 tags: pulumi.Input[Sequence[pulumi.Input['StreamingDistributionTagArgs']]]):
        """
        The set of arguments for constructing a StreamingDistribution resource.
        """
        pulumi.set(__self__, "streaming_distribution_config", streaming_distribution_config)
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="streamingDistributionConfig")
    def streaming_distribution_config(self) -> pulumi.Input['StreamingDistributionConfigArgs']:
        return pulumi.get(self, "streaming_distribution_config")

    @streaming_distribution_config.setter
    def streaming_distribution_config(self, value: pulumi.Input['StreamingDistributionConfigArgs']):
        pulumi.set(self, "streaming_distribution_config", value)

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Input[Sequence[pulumi.Input['StreamingDistributionTagArgs']]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: pulumi.Input[Sequence[pulumi.Input['StreamingDistributionTagArgs']]]):
        pulumi.set(self, "tags", value)


warnings.warn("""StreamingDistribution is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class StreamingDistribution(pulumi.CustomResource):
    warnings.warn("""StreamingDistribution is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 streaming_distribution_config: Optional[pulumi.Input[pulumi.InputType['StreamingDistributionConfigArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StreamingDistributionTagArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::CloudFront::StreamingDistribution

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: StreamingDistributionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::CloudFront::StreamingDistribution

        :param str resource_name: The name of the resource.
        :param StreamingDistributionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(StreamingDistributionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 streaming_distribution_config: Optional[pulumi.Input[pulumi.InputType['StreamingDistributionConfigArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StreamingDistributionTagArgs']]]]] = None,
                 __props__=None):
        pulumi.log.warn("""StreamingDistribution is deprecated: StreamingDistribution is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = StreamingDistributionArgs.__new__(StreamingDistributionArgs)

            if streaming_distribution_config is None and not opts.urn:
                raise TypeError("Missing required property 'streaming_distribution_config'")
            __props__.__dict__["streaming_distribution_config"] = streaming_distribution_config
            if tags is None and not opts.urn:
                raise TypeError("Missing required property 'tags'")
            __props__.__dict__["tags"] = tags
            __props__.__dict__["domain_name"] = None
        super(StreamingDistribution, __self__).__init__(
            'aws-native:cloudfront:StreamingDistribution',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'StreamingDistribution':
        """
        Get an existing StreamingDistribution resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = StreamingDistributionArgs.__new__(StreamingDistributionArgs)

        __props__.__dict__["domain_name"] = None
        __props__.__dict__["streaming_distribution_config"] = None
        __props__.__dict__["tags"] = None
        return StreamingDistribution(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "domain_name")

    @property
    @pulumi.getter(name="streamingDistributionConfig")
    def streaming_distribution_config(self) -> pulumi.Output['outputs.StreamingDistributionConfig']:
        return pulumi.get(self, "streaming_distribution_config")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Sequence['outputs.StreamingDistributionTag']]:
        return pulumi.get(self, "tags")

