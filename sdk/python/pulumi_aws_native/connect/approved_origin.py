# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ApprovedOriginArgs', 'ApprovedOrigin']

@pulumi.input_type
class ApprovedOriginArgs:
    def __init__(__self__, *,
                 instance_id: pulumi.Input[str],
                 origin: pulumi.Input[str]):
        """
        The set of arguments for constructing a ApprovedOrigin resource.
        """
        pulumi.set(__self__, "instance_id", instance_id)
        pulumi.set(__self__, "origin", origin)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "instance_id", value)

    @property
    @pulumi.getter
    def origin(self) -> pulumi.Input[str]:
        return pulumi.get(self, "origin")

    @origin.setter
    def origin(self, value: pulumi.Input[str]):
        pulumi.set(self, "origin", value)


class ApprovedOrigin(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 origin: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Connect::ApprovedOrigin

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ApprovedOriginArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Connect::ApprovedOrigin

        :param str resource_name: The name of the resource.
        :param ApprovedOriginArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ApprovedOriginArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 origin: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ApprovedOriginArgs.__new__(ApprovedOriginArgs)

            if instance_id is None and not opts.urn:
                raise TypeError("Missing required property 'instance_id'")
            __props__.__dict__["instance_id"] = instance_id
            if origin is None and not opts.urn:
                raise TypeError("Missing required property 'origin'")
            __props__.__dict__["origin"] = origin
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["instance_id", "origin"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(ApprovedOrigin, __self__).__init__(
            'aws-native:connect:ApprovedOrigin',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ApprovedOrigin':
        """
        Get an existing ApprovedOrigin resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ApprovedOriginArgs.__new__(ApprovedOriginArgs)

        __props__.__dict__["instance_id"] = None
        __props__.__dict__["origin"] = None
        return ApprovedOrigin(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter
    def origin(self) -> pulumi.Output[str]:
        return pulumi.get(self, "origin")

