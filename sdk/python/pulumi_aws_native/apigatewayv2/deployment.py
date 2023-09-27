# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['DeploymentArgs', 'Deployment']

@pulumi.input_type
class DeploymentArgs:
    def __init__(__self__, *,
                 api_id: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 stage_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Deployment resource.
        :param pulumi.Input[str] api_id: The API identifier.
        :param pulumi.Input[str] description: The description for the deployment resource.
        :param pulumi.Input[str] stage_name: The name of an existing stage to associate with the deployment.
        """
        pulumi.set(__self__, "api_id", api_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if stage_name is not None:
            pulumi.set(__self__, "stage_name", stage_name)

    @property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Input[str]:
        """
        The API identifier.
        """
        return pulumi.get(self, "api_id")

    @api_id.setter
    def api_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "api_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description for the deployment resource.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="stageName")
    def stage_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of an existing stage to associate with the deployment.
        """
        return pulumi.get(self, "stage_name")

    @stage_name.setter
    def stage_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "stage_name", value)


class Deployment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 stage_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The ``AWS::ApiGatewayV2::Deployment`` resource creates a deployment for an API.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_id: The API identifier.
        :param pulumi.Input[str] description: The description for the deployment resource.
        :param pulumi.Input[str] stage_name: The name of an existing stage to associate with the deployment.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DeploymentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The ``AWS::ApiGatewayV2::Deployment`` resource creates a deployment for an API.

        :param str resource_name: The name of the resource.
        :param DeploymentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DeploymentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 stage_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DeploymentArgs.__new__(DeploymentArgs)

            if api_id is None and not opts.urn:
                raise TypeError("Missing required property 'api_id'")
            __props__.__dict__["api_id"] = api_id
            __props__.__dict__["description"] = description
            __props__.__dict__["stage_name"] = stage_name
            __props__.__dict__["deployment_id"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["api_id"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Deployment, __self__).__init__(
            'aws-native:apigatewayv2:Deployment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Deployment':
        """
        Get an existing Deployment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DeploymentArgs.__new__(DeploymentArgs)

        __props__.__dict__["api_id"] = None
        __props__.__dict__["deployment_id"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["stage_name"] = None
        return Deployment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Output[str]:
        """
        The API identifier.
        """
        return pulumi.get(self, "api_id")

    @property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "deployment_id")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description for the deployment resource.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="stageName")
    def stage_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of an existing stage to associate with the deployment.
        """
        return pulumi.get(self, "stage_name")

