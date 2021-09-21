# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['RouteResponseArgs', 'RouteResponse']

@pulumi.input_type
class RouteResponseArgs:
    def __init__(__self__, *,
                 api_id: pulumi.Input[str],
                 route_id: pulumi.Input[str],
                 route_response_key: pulumi.Input[str],
                 model_selection_expression: Optional[pulumi.Input[str]] = None,
                 response_models: Optional[Any] = None,
                 response_parameters: Optional[Any] = None):
        """
        The set of arguments for constructing a RouteResponse resource.
        """
        pulumi.set(__self__, "api_id", api_id)
        pulumi.set(__self__, "route_id", route_id)
        pulumi.set(__self__, "route_response_key", route_response_key)
        if model_selection_expression is not None:
            pulumi.set(__self__, "model_selection_expression", model_selection_expression)
        if response_models is not None:
            pulumi.set(__self__, "response_models", response_models)
        if response_parameters is not None:
            pulumi.set(__self__, "response_parameters", response_parameters)

    @property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "api_id")

    @api_id.setter
    def api_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "api_id", value)

    @property
    @pulumi.getter(name="routeId")
    def route_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "route_id")

    @route_id.setter
    def route_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "route_id", value)

    @property
    @pulumi.getter(name="routeResponseKey")
    def route_response_key(self) -> pulumi.Input[str]:
        return pulumi.get(self, "route_response_key")

    @route_response_key.setter
    def route_response_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "route_response_key", value)

    @property
    @pulumi.getter(name="modelSelectionExpression")
    def model_selection_expression(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "model_selection_expression")

    @model_selection_expression.setter
    def model_selection_expression(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "model_selection_expression", value)

    @property
    @pulumi.getter(name="responseModels")
    def response_models(self) -> Optional[Any]:
        return pulumi.get(self, "response_models")

    @response_models.setter
    def response_models(self, value: Optional[Any]):
        pulumi.set(self, "response_models", value)

    @property
    @pulumi.getter(name="responseParameters")
    def response_parameters(self) -> Optional[Any]:
        return pulumi.get(self, "response_parameters")

    @response_parameters.setter
    def response_parameters(self, value: Optional[Any]):
        pulumi.set(self, "response_parameters", value)


warnings.warn("""RouteResponse is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class RouteResponse(pulumi.CustomResource):
    warnings.warn("""RouteResponse is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_id: Optional[pulumi.Input[str]] = None,
                 model_selection_expression: Optional[pulumi.Input[str]] = None,
                 response_models: Optional[Any] = None,
                 response_parameters: Optional[Any] = None,
                 route_id: Optional[pulumi.Input[str]] = None,
                 route_response_key: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::ApiGatewayV2::RouteResponse

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RouteResponseArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::ApiGatewayV2::RouteResponse

        :param str resource_name: The name of the resource.
        :param RouteResponseArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RouteResponseArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_id: Optional[pulumi.Input[str]] = None,
                 model_selection_expression: Optional[pulumi.Input[str]] = None,
                 response_models: Optional[Any] = None,
                 response_parameters: Optional[Any] = None,
                 route_id: Optional[pulumi.Input[str]] = None,
                 route_response_key: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""RouteResponse is deprecated: RouteResponse is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RouteResponseArgs.__new__(RouteResponseArgs)

            if api_id is None and not opts.urn:
                raise TypeError("Missing required property 'api_id'")
            __props__.__dict__["api_id"] = api_id
            __props__.__dict__["model_selection_expression"] = model_selection_expression
            __props__.__dict__["response_models"] = response_models
            __props__.__dict__["response_parameters"] = response_parameters
            if route_id is None and not opts.urn:
                raise TypeError("Missing required property 'route_id'")
            __props__.__dict__["route_id"] = route_id
            if route_response_key is None and not opts.urn:
                raise TypeError("Missing required property 'route_response_key'")
            __props__.__dict__["route_response_key"] = route_response_key
        super(RouteResponse, __self__).__init__(
            'aws-native:apigatewayv2:RouteResponse',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'RouteResponse':
        """
        Get an existing RouteResponse resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = RouteResponseArgs.__new__(RouteResponseArgs)

        __props__.__dict__["api_id"] = None
        __props__.__dict__["model_selection_expression"] = None
        __props__.__dict__["response_models"] = None
        __props__.__dict__["response_parameters"] = None
        __props__.__dict__["route_id"] = None
        __props__.__dict__["route_response_key"] = None
        return RouteResponse(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "api_id")

    @property
    @pulumi.getter(name="modelSelectionExpression")
    def model_selection_expression(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "model_selection_expression")

    @property
    @pulumi.getter(name="responseModels")
    def response_models(self) -> pulumi.Output[Optional[Any]]:
        return pulumi.get(self, "response_models")

    @property
    @pulumi.getter(name="responseParameters")
    def response_parameters(self) -> pulumi.Output[Optional[Any]]:
        return pulumi.get(self, "response_parameters")

    @property
    @pulumi.getter(name="routeId")
    def route_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "route_id")

    @property
    @pulumi.getter(name="routeResponseKey")
    def route_response_key(self) -> pulumi.Output[str]:
        return pulumi.get(self, "route_response_key")

