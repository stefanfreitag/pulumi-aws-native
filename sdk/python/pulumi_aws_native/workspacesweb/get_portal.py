# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from .. import outputs as _root_outputs
from ._enums import *

__all__ = [
    'GetPortalResult',
    'AwaitableGetPortalResult',
    'get_portal',
    'get_portal_output',
]

@pulumi.output_type
class GetPortalResult:
    def __init__(__self__, authentication_type=None, browser_settings_arn=None, browser_type=None, creation_date=None, display_name=None, ip_access_settings_arn=None, network_settings_arn=None, portal_arn=None, portal_endpoint=None, portal_status=None, renderer_type=None, service_provider_saml_metadata=None, status_reason=None, tags=None, trust_store_arn=None, user_access_logging_settings_arn=None, user_settings_arn=None):
        if authentication_type and not isinstance(authentication_type, str):
            raise TypeError("Expected argument 'authentication_type' to be a str")
        pulumi.set(__self__, "authentication_type", authentication_type)
        if browser_settings_arn and not isinstance(browser_settings_arn, str):
            raise TypeError("Expected argument 'browser_settings_arn' to be a str")
        pulumi.set(__self__, "browser_settings_arn", browser_settings_arn)
        if browser_type and not isinstance(browser_type, str):
            raise TypeError("Expected argument 'browser_type' to be a str")
        pulumi.set(__self__, "browser_type", browser_type)
        if creation_date and not isinstance(creation_date, str):
            raise TypeError("Expected argument 'creation_date' to be a str")
        pulumi.set(__self__, "creation_date", creation_date)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if ip_access_settings_arn and not isinstance(ip_access_settings_arn, str):
            raise TypeError("Expected argument 'ip_access_settings_arn' to be a str")
        pulumi.set(__self__, "ip_access_settings_arn", ip_access_settings_arn)
        if network_settings_arn and not isinstance(network_settings_arn, str):
            raise TypeError("Expected argument 'network_settings_arn' to be a str")
        pulumi.set(__self__, "network_settings_arn", network_settings_arn)
        if portal_arn and not isinstance(portal_arn, str):
            raise TypeError("Expected argument 'portal_arn' to be a str")
        pulumi.set(__self__, "portal_arn", portal_arn)
        if portal_endpoint and not isinstance(portal_endpoint, str):
            raise TypeError("Expected argument 'portal_endpoint' to be a str")
        pulumi.set(__self__, "portal_endpoint", portal_endpoint)
        if portal_status and not isinstance(portal_status, str):
            raise TypeError("Expected argument 'portal_status' to be a str")
        pulumi.set(__self__, "portal_status", portal_status)
        if renderer_type and not isinstance(renderer_type, str):
            raise TypeError("Expected argument 'renderer_type' to be a str")
        pulumi.set(__self__, "renderer_type", renderer_type)
        if service_provider_saml_metadata and not isinstance(service_provider_saml_metadata, str):
            raise TypeError("Expected argument 'service_provider_saml_metadata' to be a str")
        pulumi.set(__self__, "service_provider_saml_metadata", service_provider_saml_metadata)
        if status_reason and not isinstance(status_reason, str):
            raise TypeError("Expected argument 'status_reason' to be a str")
        pulumi.set(__self__, "status_reason", status_reason)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if trust_store_arn and not isinstance(trust_store_arn, str):
            raise TypeError("Expected argument 'trust_store_arn' to be a str")
        pulumi.set(__self__, "trust_store_arn", trust_store_arn)
        if user_access_logging_settings_arn and not isinstance(user_access_logging_settings_arn, str):
            raise TypeError("Expected argument 'user_access_logging_settings_arn' to be a str")
        pulumi.set(__self__, "user_access_logging_settings_arn", user_access_logging_settings_arn)
        if user_settings_arn and not isinstance(user_settings_arn, str):
            raise TypeError("Expected argument 'user_settings_arn' to be a str")
        pulumi.set(__self__, "user_settings_arn", user_settings_arn)

    @property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> Optional['PortalAuthenticationType']:
        return pulumi.get(self, "authentication_type")

    @property
    @pulumi.getter(name="browserSettingsArn")
    def browser_settings_arn(self) -> Optional[str]:
        return pulumi.get(self, "browser_settings_arn")

    @property
    @pulumi.getter(name="browserType")
    def browser_type(self) -> Optional['PortalBrowserType']:
        return pulumi.get(self, "browser_type")

    @property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> Optional[str]:
        return pulumi.get(self, "creation_date")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="ipAccessSettingsArn")
    def ip_access_settings_arn(self) -> Optional[str]:
        return pulumi.get(self, "ip_access_settings_arn")

    @property
    @pulumi.getter(name="networkSettingsArn")
    def network_settings_arn(self) -> Optional[str]:
        return pulumi.get(self, "network_settings_arn")

    @property
    @pulumi.getter(name="portalArn")
    def portal_arn(self) -> Optional[str]:
        return pulumi.get(self, "portal_arn")

    @property
    @pulumi.getter(name="portalEndpoint")
    def portal_endpoint(self) -> Optional[str]:
        return pulumi.get(self, "portal_endpoint")

    @property
    @pulumi.getter(name="portalStatus")
    def portal_status(self) -> Optional['PortalStatus']:
        return pulumi.get(self, "portal_status")

    @property
    @pulumi.getter(name="rendererType")
    def renderer_type(self) -> Optional['PortalRendererType']:
        return pulumi.get(self, "renderer_type")

    @property
    @pulumi.getter(name="serviceProviderSamlMetadata")
    def service_provider_saml_metadata(self) -> Optional[str]:
        return pulumi.get(self, "service_provider_saml_metadata")

    @property
    @pulumi.getter(name="statusReason")
    def status_reason(self) -> Optional[str]:
        return pulumi.get(self, "status_reason")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="trustStoreArn")
    def trust_store_arn(self) -> Optional[str]:
        return pulumi.get(self, "trust_store_arn")

    @property
    @pulumi.getter(name="userAccessLoggingSettingsArn")
    def user_access_logging_settings_arn(self) -> Optional[str]:
        return pulumi.get(self, "user_access_logging_settings_arn")

    @property
    @pulumi.getter(name="userSettingsArn")
    def user_settings_arn(self) -> Optional[str]:
        return pulumi.get(self, "user_settings_arn")


class AwaitableGetPortalResult(GetPortalResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPortalResult(
            authentication_type=self.authentication_type,
            browser_settings_arn=self.browser_settings_arn,
            browser_type=self.browser_type,
            creation_date=self.creation_date,
            display_name=self.display_name,
            ip_access_settings_arn=self.ip_access_settings_arn,
            network_settings_arn=self.network_settings_arn,
            portal_arn=self.portal_arn,
            portal_endpoint=self.portal_endpoint,
            portal_status=self.portal_status,
            renderer_type=self.renderer_type,
            service_provider_saml_metadata=self.service_provider_saml_metadata,
            status_reason=self.status_reason,
            tags=self.tags,
            trust_store_arn=self.trust_store_arn,
            user_access_logging_settings_arn=self.user_access_logging_settings_arn,
            user_settings_arn=self.user_settings_arn)


def get_portal(portal_arn: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPortalResult:
    """
    Definition of AWS::WorkSpacesWeb::Portal Resource Type
    """
    __args__ = dict()
    __args__['portalArn'] = portal_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:workspacesweb:getPortal', __args__, opts=opts, typ=GetPortalResult).value

    return AwaitableGetPortalResult(
        authentication_type=pulumi.get(__ret__, 'authentication_type'),
        browser_settings_arn=pulumi.get(__ret__, 'browser_settings_arn'),
        browser_type=pulumi.get(__ret__, 'browser_type'),
        creation_date=pulumi.get(__ret__, 'creation_date'),
        display_name=pulumi.get(__ret__, 'display_name'),
        ip_access_settings_arn=pulumi.get(__ret__, 'ip_access_settings_arn'),
        network_settings_arn=pulumi.get(__ret__, 'network_settings_arn'),
        portal_arn=pulumi.get(__ret__, 'portal_arn'),
        portal_endpoint=pulumi.get(__ret__, 'portal_endpoint'),
        portal_status=pulumi.get(__ret__, 'portal_status'),
        renderer_type=pulumi.get(__ret__, 'renderer_type'),
        service_provider_saml_metadata=pulumi.get(__ret__, 'service_provider_saml_metadata'),
        status_reason=pulumi.get(__ret__, 'status_reason'),
        tags=pulumi.get(__ret__, 'tags'),
        trust_store_arn=pulumi.get(__ret__, 'trust_store_arn'),
        user_access_logging_settings_arn=pulumi.get(__ret__, 'user_access_logging_settings_arn'),
        user_settings_arn=pulumi.get(__ret__, 'user_settings_arn'))


@_utilities.lift_output_func(get_portal)
def get_portal_output(portal_arn: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPortalResult]:
    """
    Definition of AWS::WorkSpacesWeb::Portal Resource Type
    """
    ...
