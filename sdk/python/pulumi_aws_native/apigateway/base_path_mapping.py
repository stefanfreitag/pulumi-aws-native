# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['BasePathMappingArgs', 'BasePathMapping']

@pulumi.input_type
class BasePathMappingArgs:
    def __init__(__self__, *,
                 domain_name: pulumi.Input[str],
                 base_path: Optional[pulumi.Input[str]] = None,
                 rest_api_id: Optional[pulumi.Input[str]] = None,
                 stage: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a BasePathMapping resource.
        :param pulumi.Input[str] domain_name: The domain name of the BasePathMapping resource to be described.
        :param pulumi.Input[str] base_path: The base path name that callers of the API must provide as part of the URL after the domain name.
        :param pulumi.Input[str] rest_api_id: The string identifier of the associated RestApi.
        :param pulumi.Input[str] stage: The name of the associated stage.
        """
        pulumi.set(__self__, "domain_name", domain_name)
        if base_path is not None:
            pulumi.set(__self__, "base_path", base_path)
        if rest_api_id is not None:
            pulumi.set(__self__, "rest_api_id", rest_api_id)
        if stage is not None:
            pulumi.set(__self__, "stage", stage)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[str]:
        """
        The domain name of the BasePathMapping resource to be described.
        """
        return pulumi.get(self, "domain_name")

    @domain_name.setter
    def domain_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "domain_name", value)

    @property
    @pulumi.getter(name="basePath")
    def base_path(self) -> Optional[pulumi.Input[str]]:
        """
        The base path name that callers of the API must provide as part of the URL after the domain name.
        """
        return pulumi.get(self, "base_path")

    @base_path.setter
    def base_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "base_path", value)

    @property
    @pulumi.getter(name="restApiId")
    def rest_api_id(self) -> Optional[pulumi.Input[str]]:
        """
        The string identifier of the associated RestApi.
        """
        return pulumi.get(self, "rest_api_id")

    @rest_api_id.setter
    def rest_api_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rest_api_id", value)

    @property
    @pulumi.getter
    def stage(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the associated stage.
        """
        return pulumi.get(self, "stage")

    @stage.setter
    def stage(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "stage", value)


class BasePathMapping(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 base_path: Optional[pulumi.Input[str]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 rest_api_id: Optional[pulumi.Input[str]] = None,
                 stage: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The ``AWS::ApiGateway::BasePathMapping`` resource creates a base path that clients who call your API must use in the invocation URL.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] base_path: The base path name that callers of the API must provide as part of the URL after the domain name.
        :param pulumi.Input[str] domain_name: The domain name of the BasePathMapping resource to be described.
        :param pulumi.Input[str] rest_api_id: The string identifier of the associated RestApi.
        :param pulumi.Input[str] stage: The name of the associated stage.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BasePathMappingArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The ``AWS::ApiGateway::BasePathMapping`` resource creates a base path that clients who call your API must use in the invocation URL.

        :param str resource_name: The name of the resource.
        :param BasePathMappingArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BasePathMappingArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 base_path: Optional[pulumi.Input[str]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 rest_api_id: Optional[pulumi.Input[str]] = None,
                 stage: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BasePathMappingArgs.__new__(BasePathMappingArgs)

            __props__.__dict__["base_path"] = base_path
            if domain_name is None and not opts.urn:
                raise TypeError("Missing required property 'domain_name'")
            __props__.__dict__["domain_name"] = domain_name
            __props__.__dict__["rest_api_id"] = rest_api_id
            __props__.__dict__["stage"] = stage
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["base_path", "domain_name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(BasePathMapping, __self__).__init__(
            'aws-native:apigateway:BasePathMapping',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'BasePathMapping':
        """
        Get an existing BasePathMapping resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = BasePathMappingArgs.__new__(BasePathMappingArgs)

        __props__.__dict__["base_path"] = None
        __props__.__dict__["domain_name"] = None
        __props__.__dict__["rest_api_id"] = None
        __props__.__dict__["stage"] = None
        return BasePathMapping(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="basePath")
    def base_path(self) -> pulumi.Output[Optional[str]]:
        """
        The base path name that callers of the API must provide as part of the URL after the domain name.
        """
        return pulumi.get(self, "base_path")

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[str]:
        """
        The domain name of the BasePathMapping resource to be described.
        """
        return pulumi.get(self, "domain_name")

    @property
    @pulumi.getter(name="restApiId")
    def rest_api_id(self) -> pulumi.Output[Optional[str]]:
        """
        The string identifier of the associated RestApi.
        """
        return pulumi.get(self, "rest_api_id")

    @property
    @pulumi.getter
    def stage(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the associated stage.
        """
        return pulumi.get(self, "stage")

