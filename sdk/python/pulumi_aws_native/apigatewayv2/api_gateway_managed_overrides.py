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
from ._inputs import *

__all__ = ['ApiGatewayManagedOverridesArgs', 'ApiGatewayManagedOverrides']

@pulumi.input_type
class ApiGatewayManagedOverridesArgs:
    def __init__(__self__, *,
                 api_id: pulumi.Input[str],
                 integration: Optional[pulumi.Input['ApiGatewayManagedOverridesIntegrationOverridesArgs']] = None,
                 route: Optional[pulumi.Input['ApiGatewayManagedOverridesRouteOverridesArgs']] = None,
                 stage: Optional[pulumi.Input['ApiGatewayManagedOverridesStageOverridesArgs']] = None):
        """
        The set of arguments for constructing a ApiGatewayManagedOverrides resource.
        """
        ApiGatewayManagedOverridesArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            api_id=api_id,
            integration=integration,
            route=route,
            stage=stage,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             api_id: pulumi.Input[str],
             integration: Optional[pulumi.Input['ApiGatewayManagedOverridesIntegrationOverridesArgs']] = None,
             route: Optional[pulumi.Input['ApiGatewayManagedOverridesRouteOverridesArgs']] = None,
             stage: Optional[pulumi.Input['ApiGatewayManagedOverridesStageOverridesArgs']] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("api_id", api_id)
        if integration is not None:
            _setter("integration", integration)
        if route is not None:
            _setter("route", route)
        if stage is not None:
            _setter("stage", stage)

    @property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "api_id")

    @api_id.setter
    def api_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "api_id", value)

    @property
    @pulumi.getter
    def integration(self) -> Optional[pulumi.Input['ApiGatewayManagedOverridesIntegrationOverridesArgs']]:
        return pulumi.get(self, "integration")

    @integration.setter
    def integration(self, value: Optional[pulumi.Input['ApiGatewayManagedOverridesIntegrationOverridesArgs']]):
        pulumi.set(self, "integration", value)

    @property
    @pulumi.getter
    def route(self) -> Optional[pulumi.Input['ApiGatewayManagedOverridesRouteOverridesArgs']]:
        return pulumi.get(self, "route")

    @route.setter
    def route(self, value: Optional[pulumi.Input['ApiGatewayManagedOverridesRouteOverridesArgs']]):
        pulumi.set(self, "route", value)

    @property
    @pulumi.getter
    def stage(self) -> Optional[pulumi.Input['ApiGatewayManagedOverridesStageOverridesArgs']]:
        return pulumi.get(self, "stage")

    @stage.setter
    def stage(self, value: Optional[pulumi.Input['ApiGatewayManagedOverridesStageOverridesArgs']]):
        pulumi.set(self, "stage", value)


warnings.warn("""ApiGatewayManagedOverrides is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class ApiGatewayManagedOverrides(pulumi.CustomResource):
    warnings.warn("""ApiGatewayManagedOverrides is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_id: Optional[pulumi.Input[str]] = None,
                 integration: Optional[pulumi.Input[pulumi.InputType['ApiGatewayManagedOverridesIntegrationOverridesArgs']]] = None,
                 route: Optional[pulumi.Input[pulumi.InputType['ApiGatewayManagedOverridesRouteOverridesArgs']]] = None,
                 stage: Optional[pulumi.Input[pulumi.InputType['ApiGatewayManagedOverridesStageOverridesArgs']]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::ApiGatewayV2::ApiGatewayManagedOverrides

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ApiGatewayManagedOverridesArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::ApiGatewayV2::ApiGatewayManagedOverrides

        :param str resource_name: The name of the resource.
        :param ApiGatewayManagedOverridesArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ApiGatewayManagedOverridesArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ApiGatewayManagedOverridesArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_id: Optional[pulumi.Input[str]] = None,
                 integration: Optional[pulumi.Input[pulumi.InputType['ApiGatewayManagedOverridesIntegrationOverridesArgs']]] = None,
                 route: Optional[pulumi.Input[pulumi.InputType['ApiGatewayManagedOverridesRouteOverridesArgs']]] = None,
                 stage: Optional[pulumi.Input[pulumi.InputType['ApiGatewayManagedOverridesStageOverridesArgs']]] = None,
                 __props__=None):
        pulumi.log.warn("""ApiGatewayManagedOverrides is deprecated: ApiGatewayManagedOverrides is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ApiGatewayManagedOverridesArgs.__new__(ApiGatewayManagedOverridesArgs)

            if api_id is None and not opts.urn:
                raise TypeError("Missing required property 'api_id'")
            __props__.__dict__["api_id"] = api_id
            if integration is not None and not isinstance(integration, ApiGatewayManagedOverridesIntegrationOverridesArgs):
                integration = integration or {}
                def _setter(key, value):
                    integration[key] = value
                ApiGatewayManagedOverridesIntegrationOverridesArgs._configure(_setter, **integration)
            __props__.__dict__["integration"] = integration
            if route is not None and not isinstance(route, ApiGatewayManagedOverridesRouteOverridesArgs):
                route = route or {}
                def _setter(key, value):
                    route[key] = value
                ApiGatewayManagedOverridesRouteOverridesArgs._configure(_setter, **route)
            __props__.__dict__["route"] = route
            if stage is not None and not isinstance(stage, ApiGatewayManagedOverridesStageOverridesArgs):
                stage = stage or {}
                def _setter(key, value):
                    stage[key] = value
                ApiGatewayManagedOverridesStageOverridesArgs._configure(_setter, **stage)
            __props__.__dict__["stage"] = stage
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["api_id"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(ApiGatewayManagedOverrides, __self__).__init__(
            'aws-native:apigatewayv2:ApiGatewayManagedOverrides',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ApiGatewayManagedOverrides':
        """
        Get an existing ApiGatewayManagedOverrides resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ApiGatewayManagedOverridesArgs.__new__(ApiGatewayManagedOverridesArgs)

        __props__.__dict__["api_id"] = None
        __props__.__dict__["integration"] = None
        __props__.__dict__["route"] = None
        __props__.__dict__["stage"] = None
        return ApiGatewayManagedOverrides(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "api_id")

    @property
    @pulumi.getter
    def integration(self) -> pulumi.Output[Optional['outputs.ApiGatewayManagedOverridesIntegrationOverrides']]:
        return pulumi.get(self, "integration")

    @property
    @pulumi.getter
    def route(self) -> pulumi.Output[Optional['outputs.ApiGatewayManagedOverridesRouteOverrides']]:
        return pulumi.get(self, "route")

    @property
    @pulumi.getter
    def stage(self) -> pulumi.Output[Optional['outputs.ApiGatewayManagedOverridesStageOverrides']]:
        return pulumi.get(self, "stage")

