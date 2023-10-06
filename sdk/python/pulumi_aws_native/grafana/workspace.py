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

__all__ = ['WorkspaceArgs', 'Workspace']

@pulumi.input_type
class WorkspaceArgs:
    def __init__(__self__, *,
                 account_access_type: pulumi.Input['WorkspaceAccountAccessType'],
                 authentication_providers: pulumi.Input[Sequence[pulumi.Input['WorkspaceAuthenticationProviderTypes']]],
                 permission_type: pulumi.Input['WorkspacePermissionType'],
                 client_token: Optional[pulumi.Input[str]] = None,
                 data_sources: Optional[pulumi.Input[Sequence[pulumi.Input['WorkspaceDataSourceType']]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 grafana_version: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_access_control: Optional[pulumi.Input['WorkspaceNetworkAccessControlArgs']] = None,
                 notification_destinations: Optional[pulumi.Input[Sequence[pulumi.Input['WorkspaceNotificationDestinationType']]]] = None,
                 organization_role_name: Optional[pulumi.Input[str]] = None,
                 organizational_units: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 saml_configuration: Optional[pulumi.Input['WorkspaceSamlConfigurationArgs']] = None,
                 stack_set_name: Optional[pulumi.Input[str]] = None,
                 vpc_configuration: Optional[pulumi.Input['WorkspaceVpcConfigurationArgs']] = None):
        """
        The set of arguments for constructing a Workspace resource.
        :param pulumi.Input[Sequence[pulumi.Input['WorkspaceAuthenticationProviderTypes']]] authentication_providers: List of authentication providers to enable.
        :param pulumi.Input[str] client_token: A unique, case-sensitive, user-provided identifier to ensure the idempotency of the request.
        :param pulumi.Input[Sequence[pulumi.Input['WorkspaceDataSourceType']]] data_sources: List of data sources on the service managed IAM role.
        :param pulumi.Input[str] description: Description of a workspace.
        :param pulumi.Input[str] grafana_version: The version of Grafana to support in your workspace.
        :param pulumi.Input[str] name: The user friendly name of a workspace.
        :param pulumi.Input[Sequence[pulumi.Input['WorkspaceNotificationDestinationType']]] notification_destinations: List of notification destinations on the customers service managed IAM role that the Grafana workspace can query.
        :param pulumi.Input[str] organization_role_name: The name of an IAM role that already exists to use with AWS Organizations to access AWS data sources and notification channels in other accounts in an organization.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] organizational_units: List of Organizational Units containing AWS accounts the Grafana workspace can pull data from.
        :param pulumi.Input[str] role_arn: IAM Role that will be used to grant the Grafana workspace access to a customers AWS resources.
        :param pulumi.Input[str] stack_set_name: The name of the AWS CloudFormation stack set to use to generate IAM roles to be used for this workspace.
        """
        WorkspaceArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            account_access_type=account_access_type,
            authentication_providers=authentication_providers,
            permission_type=permission_type,
            client_token=client_token,
            data_sources=data_sources,
            description=description,
            grafana_version=grafana_version,
            name=name,
            network_access_control=network_access_control,
            notification_destinations=notification_destinations,
            organization_role_name=organization_role_name,
            organizational_units=organizational_units,
            role_arn=role_arn,
            saml_configuration=saml_configuration,
            stack_set_name=stack_set_name,
            vpc_configuration=vpc_configuration,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             account_access_type: pulumi.Input['WorkspaceAccountAccessType'],
             authentication_providers: pulumi.Input[Sequence[pulumi.Input['WorkspaceAuthenticationProviderTypes']]],
             permission_type: pulumi.Input['WorkspacePermissionType'],
             client_token: Optional[pulumi.Input[str]] = None,
             data_sources: Optional[pulumi.Input[Sequence[pulumi.Input['WorkspaceDataSourceType']]]] = None,
             description: Optional[pulumi.Input[str]] = None,
             grafana_version: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             network_access_control: Optional[pulumi.Input['WorkspaceNetworkAccessControlArgs']] = None,
             notification_destinations: Optional[pulumi.Input[Sequence[pulumi.Input['WorkspaceNotificationDestinationType']]]] = None,
             organization_role_name: Optional[pulumi.Input[str]] = None,
             organizational_units: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             role_arn: Optional[pulumi.Input[str]] = None,
             saml_configuration: Optional[pulumi.Input['WorkspaceSamlConfigurationArgs']] = None,
             stack_set_name: Optional[pulumi.Input[str]] = None,
             vpc_configuration: Optional[pulumi.Input['WorkspaceVpcConfigurationArgs']] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("account_access_type", account_access_type)
        _setter("authentication_providers", authentication_providers)
        _setter("permission_type", permission_type)
        if client_token is not None:
            _setter("client_token", client_token)
        if data_sources is not None:
            _setter("data_sources", data_sources)
        if description is not None:
            _setter("description", description)
        if grafana_version is not None:
            _setter("grafana_version", grafana_version)
        if name is not None:
            _setter("name", name)
        if network_access_control is not None:
            _setter("network_access_control", network_access_control)
        if notification_destinations is not None:
            _setter("notification_destinations", notification_destinations)
        if organization_role_name is not None:
            _setter("organization_role_name", organization_role_name)
        if organizational_units is not None:
            _setter("organizational_units", organizational_units)
        if role_arn is not None:
            _setter("role_arn", role_arn)
        if saml_configuration is not None:
            _setter("saml_configuration", saml_configuration)
        if stack_set_name is not None:
            _setter("stack_set_name", stack_set_name)
        if vpc_configuration is not None:
            _setter("vpc_configuration", vpc_configuration)

    @property
    @pulumi.getter(name="accountAccessType")
    def account_access_type(self) -> pulumi.Input['WorkspaceAccountAccessType']:
        return pulumi.get(self, "account_access_type")

    @account_access_type.setter
    def account_access_type(self, value: pulumi.Input['WorkspaceAccountAccessType']):
        pulumi.set(self, "account_access_type", value)

    @property
    @pulumi.getter(name="authenticationProviders")
    def authentication_providers(self) -> pulumi.Input[Sequence[pulumi.Input['WorkspaceAuthenticationProviderTypes']]]:
        """
        List of authentication providers to enable.
        """
        return pulumi.get(self, "authentication_providers")

    @authentication_providers.setter
    def authentication_providers(self, value: pulumi.Input[Sequence[pulumi.Input['WorkspaceAuthenticationProviderTypes']]]):
        pulumi.set(self, "authentication_providers", value)

    @property
    @pulumi.getter(name="permissionType")
    def permission_type(self) -> pulumi.Input['WorkspacePermissionType']:
        return pulumi.get(self, "permission_type")

    @permission_type.setter
    def permission_type(self, value: pulumi.Input['WorkspacePermissionType']):
        pulumi.set(self, "permission_type", value)

    @property
    @pulumi.getter(name="clientToken")
    def client_token(self) -> Optional[pulumi.Input[str]]:
        """
        A unique, case-sensitive, user-provided identifier to ensure the idempotency of the request.
        """
        return pulumi.get(self, "client_token")

    @client_token.setter
    def client_token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_token", value)

    @property
    @pulumi.getter(name="dataSources")
    def data_sources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['WorkspaceDataSourceType']]]]:
        """
        List of data sources on the service managed IAM role.
        """
        return pulumi.get(self, "data_sources")

    @data_sources.setter
    def data_sources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['WorkspaceDataSourceType']]]]):
        pulumi.set(self, "data_sources", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of a workspace.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="grafanaVersion")
    def grafana_version(self) -> Optional[pulumi.Input[str]]:
        """
        The version of Grafana to support in your workspace.
        """
        return pulumi.get(self, "grafana_version")

    @grafana_version.setter
    def grafana_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "grafana_version", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The user friendly name of a workspace.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="networkAccessControl")
    def network_access_control(self) -> Optional[pulumi.Input['WorkspaceNetworkAccessControlArgs']]:
        return pulumi.get(self, "network_access_control")

    @network_access_control.setter
    def network_access_control(self, value: Optional[pulumi.Input['WorkspaceNetworkAccessControlArgs']]):
        pulumi.set(self, "network_access_control", value)

    @property
    @pulumi.getter(name="notificationDestinations")
    def notification_destinations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['WorkspaceNotificationDestinationType']]]]:
        """
        List of notification destinations on the customers service managed IAM role that the Grafana workspace can query.
        """
        return pulumi.get(self, "notification_destinations")

    @notification_destinations.setter
    def notification_destinations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['WorkspaceNotificationDestinationType']]]]):
        pulumi.set(self, "notification_destinations", value)

    @property
    @pulumi.getter(name="organizationRoleName")
    def organization_role_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of an IAM role that already exists to use with AWS Organizations to access AWS data sources and notification channels in other accounts in an organization.
        """
        return pulumi.get(self, "organization_role_name")

    @organization_role_name.setter
    def organization_role_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "organization_role_name", value)

    @property
    @pulumi.getter(name="organizationalUnits")
    def organizational_units(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of Organizational Units containing AWS accounts the Grafana workspace can pull data from.
        """
        return pulumi.get(self, "organizational_units")

    @organizational_units.setter
    def organizational_units(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "organizational_units", value)

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[str]]:
        """
        IAM Role that will be used to grant the Grafana workspace access to a customers AWS resources.
        """
        return pulumi.get(self, "role_arn")

    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role_arn", value)

    @property
    @pulumi.getter(name="samlConfiguration")
    def saml_configuration(self) -> Optional[pulumi.Input['WorkspaceSamlConfigurationArgs']]:
        return pulumi.get(self, "saml_configuration")

    @saml_configuration.setter
    def saml_configuration(self, value: Optional[pulumi.Input['WorkspaceSamlConfigurationArgs']]):
        pulumi.set(self, "saml_configuration", value)

    @property
    @pulumi.getter(name="stackSetName")
    def stack_set_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the AWS CloudFormation stack set to use to generate IAM roles to be used for this workspace.
        """
        return pulumi.get(self, "stack_set_name")

    @stack_set_name.setter
    def stack_set_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "stack_set_name", value)

    @property
    @pulumi.getter(name="vpcConfiguration")
    def vpc_configuration(self) -> Optional[pulumi.Input['WorkspaceVpcConfigurationArgs']]:
        return pulumi.get(self, "vpc_configuration")

    @vpc_configuration.setter
    def vpc_configuration(self, value: Optional[pulumi.Input['WorkspaceVpcConfigurationArgs']]):
        pulumi.set(self, "vpc_configuration", value)


class Workspace(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_access_type: Optional[pulumi.Input['WorkspaceAccountAccessType']] = None,
                 authentication_providers: Optional[pulumi.Input[Sequence[pulumi.Input['WorkspaceAuthenticationProviderTypes']]]] = None,
                 client_token: Optional[pulumi.Input[str]] = None,
                 data_sources: Optional[pulumi.Input[Sequence[pulumi.Input['WorkspaceDataSourceType']]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 grafana_version: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_access_control: Optional[pulumi.Input[pulumi.InputType['WorkspaceNetworkAccessControlArgs']]] = None,
                 notification_destinations: Optional[pulumi.Input[Sequence[pulumi.Input['WorkspaceNotificationDestinationType']]]] = None,
                 organization_role_name: Optional[pulumi.Input[str]] = None,
                 organizational_units: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 permission_type: Optional[pulumi.Input['WorkspacePermissionType']] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 saml_configuration: Optional[pulumi.Input[pulumi.InputType['WorkspaceSamlConfigurationArgs']]] = None,
                 stack_set_name: Optional[pulumi.Input[str]] = None,
                 vpc_configuration: Optional[pulumi.Input[pulumi.InputType['WorkspaceVpcConfigurationArgs']]] = None,
                 __props__=None):
        """
        Definition of AWS::Grafana::Workspace Resource Type

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input['WorkspaceAuthenticationProviderTypes']]] authentication_providers: List of authentication providers to enable.
        :param pulumi.Input[str] client_token: A unique, case-sensitive, user-provided identifier to ensure the idempotency of the request.
        :param pulumi.Input[Sequence[pulumi.Input['WorkspaceDataSourceType']]] data_sources: List of data sources on the service managed IAM role.
        :param pulumi.Input[str] description: Description of a workspace.
        :param pulumi.Input[str] grafana_version: The version of Grafana to support in your workspace.
        :param pulumi.Input[str] name: The user friendly name of a workspace.
        :param pulumi.Input[Sequence[pulumi.Input['WorkspaceNotificationDestinationType']]] notification_destinations: List of notification destinations on the customers service managed IAM role that the Grafana workspace can query.
        :param pulumi.Input[str] organization_role_name: The name of an IAM role that already exists to use with AWS Organizations to access AWS data sources and notification channels in other accounts in an organization.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] organizational_units: List of Organizational Units containing AWS accounts the Grafana workspace can pull data from.
        :param pulumi.Input[str] role_arn: IAM Role that will be used to grant the Grafana workspace access to a customers AWS resources.
        :param pulumi.Input[str] stack_set_name: The name of the AWS CloudFormation stack set to use to generate IAM roles to be used for this workspace.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WorkspaceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Definition of AWS::Grafana::Workspace Resource Type

        :param str resource_name: The name of the resource.
        :param WorkspaceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WorkspaceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            WorkspaceArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_access_type: Optional[pulumi.Input['WorkspaceAccountAccessType']] = None,
                 authentication_providers: Optional[pulumi.Input[Sequence[pulumi.Input['WorkspaceAuthenticationProviderTypes']]]] = None,
                 client_token: Optional[pulumi.Input[str]] = None,
                 data_sources: Optional[pulumi.Input[Sequence[pulumi.Input['WorkspaceDataSourceType']]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 grafana_version: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_access_control: Optional[pulumi.Input[pulumi.InputType['WorkspaceNetworkAccessControlArgs']]] = None,
                 notification_destinations: Optional[pulumi.Input[Sequence[pulumi.Input['WorkspaceNotificationDestinationType']]]] = None,
                 organization_role_name: Optional[pulumi.Input[str]] = None,
                 organizational_units: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 permission_type: Optional[pulumi.Input['WorkspacePermissionType']] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 saml_configuration: Optional[pulumi.Input[pulumi.InputType['WorkspaceSamlConfigurationArgs']]] = None,
                 stack_set_name: Optional[pulumi.Input[str]] = None,
                 vpc_configuration: Optional[pulumi.Input[pulumi.InputType['WorkspaceVpcConfigurationArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WorkspaceArgs.__new__(WorkspaceArgs)

            if account_access_type is None and not opts.urn:
                raise TypeError("Missing required property 'account_access_type'")
            __props__.__dict__["account_access_type"] = account_access_type
            if authentication_providers is None and not opts.urn:
                raise TypeError("Missing required property 'authentication_providers'")
            __props__.__dict__["authentication_providers"] = authentication_providers
            __props__.__dict__["client_token"] = client_token
            __props__.__dict__["data_sources"] = data_sources
            __props__.__dict__["description"] = description
            __props__.__dict__["grafana_version"] = grafana_version
            __props__.__dict__["name"] = name
            if network_access_control is not None and not isinstance(network_access_control, WorkspaceNetworkAccessControlArgs):
                network_access_control = network_access_control or {}
                def _setter(key, value):
                    network_access_control[key] = value
                WorkspaceNetworkAccessControlArgs._configure(_setter, **network_access_control)
            __props__.__dict__["network_access_control"] = network_access_control
            __props__.__dict__["notification_destinations"] = notification_destinations
            __props__.__dict__["organization_role_name"] = organization_role_name
            __props__.__dict__["organizational_units"] = organizational_units
            if permission_type is None and not opts.urn:
                raise TypeError("Missing required property 'permission_type'")
            __props__.__dict__["permission_type"] = permission_type
            __props__.__dict__["role_arn"] = role_arn
            if saml_configuration is not None and not isinstance(saml_configuration, WorkspaceSamlConfigurationArgs):
                saml_configuration = saml_configuration or {}
                def _setter(key, value):
                    saml_configuration[key] = value
                WorkspaceSamlConfigurationArgs._configure(_setter, **saml_configuration)
            __props__.__dict__["saml_configuration"] = saml_configuration
            __props__.__dict__["stack_set_name"] = stack_set_name
            if vpc_configuration is not None and not isinstance(vpc_configuration, WorkspaceVpcConfigurationArgs):
                vpc_configuration = vpc_configuration or {}
                def _setter(key, value):
                    vpc_configuration[key] = value
                WorkspaceVpcConfigurationArgs._configure(_setter, **vpc_configuration)
            __props__.__dict__["vpc_configuration"] = vpc_configuration
            __props__.__dict__["creation_timestamp"] = None
            __props__.__dict__["endpoint"] = None
            __props__.__dict__["modification_timestamp"] = None
            __props__.__dict__["saml_configuration_status"] = None
            __props__.__dict__["sso_client_id"] = None
            __props__.__dict__["status"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["client_token"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Workspace, __self__).__init__(
            'aws-native:grafana:Workspace',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Workspace':
        """
        Get an existing Workspace resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = WorkspaceArgs.__new__(WorkspaceArgs)

        __props__.__dict__["account_access_type"] = None
        __props__.__dict__["authentication_providers"] = None
        __props__.__dict__["client_token"] = None
        __props__.__dict__["creation_timestamp"] = None
        __props__.__dict__["data_sources"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["endpoint"] = None
        __props__.__dict__["grafana_version"] = None
        __props__.__dict__["modification_timestamp"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["network_access_control"] = None
        __props__.__dict__["notification_destinations"] = None
        __props__.__dict__["organization_role_name"] = None
        __props__.__dict__["organizational_units"] = None
        __props__.__dict__["permission_type"] = None
        __props__.__dict__["role_arn"] = None
        __props__.__dict__["saml_configuration"] = None
        __props__.__dict__["saml_configuration_status"] = None
        __props__.__dict__["sso_client_id"] = None
        __props__.__dict__["stack_set_name"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["vpc_configuration"] = None
        return Workspace(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountAccessType")
    def account_access_type(self) -> pulumi.Output['WorkspaceAccountAccessType']:
        return pulumi.get(self, "account_access_type")

    @property
    @pulumi.getter(name="authenticationProviders")
    def authentication_providers(self) -> pulumi.Output[Sequence['WorkspaceAuthenticationProviderTypes']]:
        """
        List of authentication providers to enable.
        """
        return pulumi.get(self, "authentication_providers")

    @property
    @pulumi.getter(name="clientToken")
    def client_token(self) -> pulumi.Output[Optional[str]]:
        """
        A unique, case-sensitive, user-provided identifier to ensure the idempotency of the request.
        """
        return pulumi.get(self, "client_token")

    @property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[str]:
        """
        Timestamp when the workspace was created.
        """
        return pulumi.get(self, "creation_timestamp")

    @property
    @pulumi.getter(name="dataSources")
    def data_sources(self) -> pulumi.Output[Optional[Sequence['WorkspaceDataSourceType']]]:
        """
        List of data sources on the service managed IAM role.
        """
        return pulumi.get(self, "data_sources")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of a workspace.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[str]:
        """
        Endpoint for the Grafana workspace.
        """
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter(name="grafanaVersion")
    def grafana_version(self) -> pulumi.Output[Optional[str]]:
        """
        The version of Grafana to support in your workspace.
        """
        return pulumi.get(self, "grafana_version")

    @property
    @pulumi.getter(name="modificationTimestamp")
    def modification_timestamp(self) -> pulumi.Output[str]:
        """
        Timestamp when the workspace was last modified
        """
        return pulumi.get(self, "modification_timestamp")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        The user friendly name of a workspace.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkAccessControl")
    def network_access_control(self) -> pulumi.Output[Optional['outputs.WorkspaceNetworkAccessControl']]:
        return pulumi.get(self, "network_access_control")

    @property
    @pulumi.getter(name="notificationDestinations")
    def notification_destinations(self) -> pulumi.Output[Optional[Sequence['WorkspaceNotificationDestinationType']]]:
        """
        List of notification destinations on the customers service managed IAM role that the Grafana workspace can query.
        """
        return pulumi.get(self, "notification_destinations")

    @property
    @pulumi.getter(name="organizationRoleName")
    def organization_role_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of an IAM role that already exists to use with AWS Organizations to access AWS data sources and notification channels in other accounts in an organization.
        """
        return pulumi.get(self, "organization_role_name")

    @property
    @pulumi.getter(name="organizationalUnits")
    def organizational_units(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of Organizational Units containing AWS accounts the Grafana workspace can pull data from.
        """
        return pulumi.get(self, "organizational_units")

    @property
    @pulumi.getter(name="permissionType")
    def permission_type(self) -> pulumi.Output['WorkspacePermissionType']:
        return pulumi.get(self, "permission_type")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[Optional[str]]:
        """
        IAM Role that will be used to grant the Grafana workspace access to a customers AWS resources.
        """
        return pulumi.get(self, "role_arn")

    @property
    @pulumi.getter(name="samlConfiguration")
    def saml_configuration(self) -> pulumi.Output[Optional['outputs.WorkspaceSamlConfiguration']]:
        return pulumi.get(self, "saml_configuration")

    @property
    @pulumi.getter(name="samlConfigurationStatus")
    def saml_configuration_status(self) -> pulumi.Output['WorkspaceSamlConfigurationStatus']:
        return pulumi.get(self, "saml_configuration_status")

    @property
    @pulumi.getter(name="ssoClientId")
    def sso_client_id(self) -> pulumi.Output[str]:
        """
        The client ID of the AWS SSO Managed Application.
        """
        return pulumi.get(self, "sso_client_id")

    @property
    @pulumi.getter(name="stackSetName")
    def stack_set_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the AWS CloudFormation stack set to use to generate IAM roles to be used for this workspace.
        """
        return pulumi.get(self, "stack_set_name")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output['WorkspaceStatus']:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="vpcConfiguration")
    def vpc_configuration(self) -> pulumi.Output[Optional['outputs.WorkspaceVpcConfiguration']]:
        return pulumi.get(self, "vpc_configuration")

