# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ElasticLoadBalancerAttachmentArgs', 'ElasticLoadBalancerAttachment']

@pulumi.input_type
class ElasticLoadBalancerAttachmentArgs:
    def __init__(__self__, *,
                 elastic_load_balancer_name: pulumi.Input[str],
                 layer_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a ElasticLoadBalancerAttachment resource.
        """
        pulumi.set(__self__, "elastic_load_balancer_name", elastic_load_balancer_name)
        pulumi.set(__self__, "layer_id", layer_id)

    @property
    @pulumi.getter(name="elasticLoadBalancerName")
    def elastic_load_balancer_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "elastic_load_balancer_name")

    @elastic_load_balancer_name.setter
    def elastic_load_balancer_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "elastic_load_balancer_name", value)

    @property
    @pulumi.getter(name="layerId")
    def layer_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "layer_id")

    @layer_id.setter
    def layer_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "layer_id", value)


warnings.warn("""ElasticLoadBalancerAttachment is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class ElasticLoadBalancerAttachment(pulumi.CustomResource):
    warnings.warn("""ElasticLoadBalancerAttachment is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 elastic_load_balancer_name: Optional[pulumi.Input[str]] = None,
                 layer_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::OpsWorks::ElasticLoadBalancerAttachment

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ElasticLoadBalancerAttachmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::OpsWorks::ElasticLoadBalancerAttachment

        :param str resource_name: The name of the resource.
        :param ElasticLoadBalancerAttachmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ElasticLoadBalancerAttachmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 elastic_load_balancer_name: Optional[pulumi.Input[str]] = None,
                 layer_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""ElasticLoadBalancerAttachment is deprecated: ElasticLoadBalancerAttachment is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ElasticLoadBalancerAttachmentArgs.__new__(ElasticLoadBalancerAttachmentArgs)

            if elastic_load_balancer_name is None and not opts.urn:
                raise TypeError("Missing required property 'elastic_load_balancer_name'")
            __props__.__dict__["elastic_load_balancer_name"] = elastic_load_balancer_name
            if layer_id is None and not opts.urn:
                raise TypeError("Missing required property 'layer_id'")
            __props__.__dict__["layer_id"] = layer_id
        super(ElasticLoadBalancerAttachment, __self__).__init__(
            'aws-native:opsworks:ElasticLoadBalancerAttachment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ElasticLoadBalancerAttachment':
        """
        Get an existing ElasticLoadBalancerAttachment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ElasticLoadBalancerAttachmentArgs.__new__(ElasticLoadBalancerAttachmentArgs)

        __props__.__dict__["elastic_load_balancer_name"] = None
        __props__.__dict__["layer_id"] = None
        return ElasticLoadBalancerAttachment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="elasticLoadBalancerName")
    def elastic_load_balancer_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "elastic_load_balancer_name")

    @property
    @pulumi.getter(name="layerId")
    def layer_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "layer_id")

