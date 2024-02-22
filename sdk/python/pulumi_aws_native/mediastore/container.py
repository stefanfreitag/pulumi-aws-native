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
from .. import _inputs as _root_inputs
from .. import outputs as _root_outputs
from ._inputs import *

__all__ = ['ContainerArgs', 'Container']

@pulumi.input_type
class ContainerArgs:
    def __init__(__self__, *,
                 access_logging_enabled: Optional[pulumi.Input[bool]] = None,
                 container_name: Optional[pulumi.Input[str]] = None,
                 cors_policy: Optional[pulumi.Input[Sequence[pulumi.Input['ContainerCorsRuleArgs']]]] = None,
                 lifecycle_policy: Optional[pulumi.Input[str]] = None,
                 metric_policy: Optional[pulumi.Input['ContainerMetricPolicyArgs']] = None,
                 policy: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a Container resource.
        """
        if access_logging_enabled is not None:
            pulumi.set(__self__, "access_logging_enabled", access_logging_enabled)
        if container_name is not None:
            pulumi.set(__self__, "container_name", container_name)
        if cors_policy is not None:
            pulumi.set(__self__, "cors_policy", cors_policy)
        if lifecycle_policy is not None:
            pulumi.set(__self__, "lifecycle_policy", lifecycle_policy)
        if metric_policy is not None:
            pulumi.set(__self__, "metric_policy", metric_policy)
        if policy is not None:
            pulumi.set(__self__, "policy", policy)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="accessLoggingEnabled")
    def access_logging_enabled(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "access_logging_enabled")

    @access_logging_enabled.setter
    def access_logging_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "access_logging_enabled", value)

    @property
    @pulumi.getter(name="containerName")
    def container_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "container_name")

    @container_name.setter
    def container_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "container_name", value)

    @property
    @pulumi.getter(name="corsPolicy")
    def cors_policy(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ContainerCorsRuleArgs']]]]:
        return pulumi.get(self, "cors_policy")

    @cors_policy.setter
    def cors_policy(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ContainerCorsRuleArgs']]]]):
        pulumi.set(self, "cors_policy", value)

    @property
    @pulumi.getter(name="lifecyclePolicy")
    def lifecycle_policy(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "lifecycle_policy")

    @lifecycle_policy.setter
    def lifecycle_policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "lifecycle_policy", value)

    @property
    @pulumi.getter(name="metricPolicy")
    def metric_policy(self) -> Optional[pulumi.Input['ContainerMetricPolicyArgs']]:
        return pulumi.get(self, "metric_policy")

    @metric_policy.setter
    def metric_policy(self, value: Optional[pulumi.Input['ContainerMetricPolicyArgs']]):
        pulumi.set(self, "metric_policy", value)

    @property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "policy")

    @policy.setter
    def policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)


warnings.warn("""Container is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class Container(pulumi.CustomResource):
    warnings.warn("""Container is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_logging_enabled: Optional[pulumi.Input[bool]] = None,
                 container_name: Optional[pulumi.Input[str]] = None,
                 cors_policy: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ContainerCorsRuleArgs']]]]] = None,
                 lifecycle_policy: Optional[pulumi.Input[str]] = None,
                 metric_policy: Optional[pulumi.Input[pulumi.InputType['ContainerMetricPolicyArgs']]] = None,
                 policy: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::MediaStore::Container

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ContainerArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::MediaStore::Container

        :param str resource_name: The name of the resource.
        :param ContainerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ContainerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_logging_enabled: Optional[pulumi.Input[bool]] = None,
                 container_name: Optional[pulumi.Input[str]] = None,
                 cors_policy: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ContainerCorsRuleArgs']]]]] = None,
                 lifecycle_policy: Optional[pulumi.Input[str]] = None,
                 metric_policy: Optional[pulumi.Input[pulumi.InputType['ContainerMetricPolicyArgs']]] = None,
                 policy: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        pulumi.log.warn("""Container is deprecated: Container is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ContainerArgs.__new__(ContainerArgs)

            __props__.__dict__["access_logging_enabled"] = access_logging_enabled
            __props__.__dict__["container_name"] = container_name
            __props__.__dict__["cors_policy"] = cors_policy
            __props__.__dict__["lifecycle_policy"] = lifecycle_policy
            __props__.__dict__["metric_policy"] = metric_policy
            __props__.__dict__["policy"] = policy
            __props__.__dict__["tags"] = tags
            __props__.__dict__["endpoint"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["container_name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Container, __self__).__init__(
            'aws-native:mediastore:Container',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Container':
        """
        Get an existing Container resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ContainerArgs.__new__(ContainerArgs)

        __props__.__dict__["access_logging_enabled"] = None
        __props__.__dict__["container_name"] = None
        __props__.__dict__["cors_policy"] = None
        __props__.__dict__["endpoint"] = None
        __props__.__dict__["lifecycle_policy"] = None
        __props__.__dict__["metric_policy"] = None
        __props__.__dict__["policy"] = None
        __props__.__dict__["tags"] = None
        return Container(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessLoggingEnabled")
    def access_logging_enabled(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "access_logging_enabled")

    @property
    @pulumi.getter(name="containerName")
    def container_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "container_name")

    @property
    @pulumi.getter(name="corsPolicy")
    def cors_policy(self) -> pulumi.Output[Optional[Sequence['outputs.ContainerCorsRule']]]:
        return pulumi.get(self, "cors_policy")

    @property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[str]:
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter(name="lifecyclePolicy")
    def lifecycle_policy(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "lifecycle_policy")

    @property
    @pulumi.getter(name="metricPolicy")
    def metric_policy(self) -> pulumi.Output[Optional['outputs.ContainerMetricPolicy']]:
        return pulumi.get(self, "metric_policy")

    @property
    @pulumi.getter
    def policy(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "policy")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        return pulumi.get(self, "tags")

