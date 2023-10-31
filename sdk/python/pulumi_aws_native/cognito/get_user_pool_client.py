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

__all__ = [
    'GetUserPoolClientResult',
    'AwaitableGetUserPoolClientResult',
    'get_user_pool_client',
    'get_user_pool_client_output',
]

@pulumi.output_type
class GetUserPoolClientResult:
    def __init__(__self__, access_token_validity=None, allowed_o_auth_flows=None, allowed_o_auth_flows_user_pool_client=None, allowed_o_auth_scopes=None, analytics_configuration=None, auth_session_validity=None, callback_urls=None, client_id=None, client_name=None, client_secret=None, default_redirect_uri=None, enable_propagate_additional_user_context_data=None, enable_token_revocation=None, explicit_auth_flows=None, id_token_validity=None, logout_urls=None, name=None, prevent_user_existence_errors=None, read_attributes=None, refresh_token_validity=None, supported_identity_providers=None, token_validity_units=None, write_attributes=None):
        if access_token_validity and not isinstance(access_token_validity, int):
            raise TypeError("Expected argument 'access_token_validity' to be a int")
        pulumi.set(__self__, "access_token_validity", access_token_validity)
        if allowed_o_auth_flows and not isinstance(allowed_o_auth_flows, list):
            raise TypeError("Expected argument 'allowed_o_auth_flows' to be a list")
        pulumi.set(__self__, "allowed_o_auth_flows", allowed_o_auth_flows)
        if allowed_o_auth_flows_user_pool_client and not isinstance(allowed_o_auth_flows_user_pool_client, bool):
            raise TypeError("Expected argument 'allowed_o_auth_flows_user_pool_client' to be a bool")
        pulumi.set(__self__, "allowed_o_auth_flows_user_pool_client", allowed_o_auth_flows_user_pool_client)
        if allowed_o_auth_scopes and not isinstance(allowed_o_auth_scopes, list):
            raise TypeError("Expected argument 'allowed_o_auth_scopes' to be a list")
        pulumi.set(__self__, "allowed_o_auth_scopes", allowed_o_auth_scopes)
        if analytics_configuration and not isinstance(analytics_configuration, dict):
            raise TypeError("Expected argument 'analytics_configuration' to be a dict")
        pulumi.set(__self__, "analytics_configuration", analytics_configuration)
        if auth_session_validity and not isinstance(auth_session_validity, int):
            raise TypeError("Expected argument 'auth_session_validity' to be a int")
        pulumi.set(__self__, "auth_session_validity", auth_session_validity)
        if callback_urls and not isinstance(callback_urls, list):
            raise TypeError("Expected argument 'callback_urls' to be a list")
        pulumi.set(__self__, "callback_urls", callback_urls)
        if client_id and not isinstance(client_id, str):
            raise TypeError("Expected argument 'client_id' to be a str")
        pulumi.set(__self__, "client_id", client_id)
        if client_name and not isinstance(client_name, str):
            raise TypeError("Expected argument 'client_name' to be a str")
        pulumi.set(__self__, "client_name", client_name)
        if client_secret and not isinstance(client_secret, str):
            raise TypeError("Expected argument 'client_secret' to be a str")
        pulumi.set(__self__, "client_secret", client_secret)
        if default_redirect_uri and not isinstance(default_redirect_uri, str):
            raise TypeError("Expected argument 'default_redirect_uri' to be a str")
        pulumi.set(__self__, "default_redirect_uri", default_redirect_uri)
        if enable_propagate_additional_user_context_data and not isinstance(enable_propagate_additional_user_context_data, bool):
            raise TypeError("Expected argument 'enable_propagate_additional_user_context_data' to be a bool")
        pulumi.set(__self__, "enable_propagate_additional_user_context_data", enable_propagate_additional_user_context_data)
        if enable_token_revocation and not isinstance(enable_token_revocation, bool):
            raise TypeError("Expected argument 'enable_token_revocation' to be a bool")
        pulumi.set(__self__, "enable_token_revocation", enable_token_revocation)
        if explicit_auth_flows and not isinstance(explicit_auth_flows, list):
            raise TypeError("Expected argument 'explicit_auth_flows' to be a list")
        pulumi.set(__self__, "explicit_auth_flows", explicit_auth_flows)
        if id_token_validity and not isinstance(id_token_validity, int):
            raise TypeError("Expected argument 'id_token_validity' to be a int")
        pulumi.set(__self__, "id_token_validity", id_token_validity)
        if logout_urls and not isinstance(logout_urls, list):
            raise TypeError("Expected argument 'logout_urls' to be a list")
        pulumi.set(__self__, "logout_urls", logout_urls)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if prevent_user_existence_errors and not isinstance(prevent_user_existence_errors, str):
            raise TypeError("Expected argument 'prevent_user_existence_errors' to be a str")
        pulumi.set(__self__, "prevent_user_existence_errors", prevent_user_existence_errors)
        if read_attributes and not isinstance(read_attributes, list):
            raise TypeError("Expected argument 'read_attributes' to be a list")
        pulumi.set(__self__, "read_attributes", read_attributes)
        if refresh_token_validity and not isinstance(refresh_token_validity, int):
            raise TypeError("Expected argument 'refresh_token_validity' to be a int")
        pulumi.set(__self__, "refresh_token_validity", refresh_token_validity)
        if supported_identity_providers and not isinstance(supported_identity_providers, list):
            raise TypeError("Expected argument 'supported_identity_providers' to be a list")
        pulumi.set(__self__, "supported_identity_providers", supported_identity_providers)
        if token_validity_units and not isinstance(token_validity_units, dict):
            raise TypeError("Expected argument 'token_validity_units' to be a dict")
        pulumi.set(__self__, "token_validity_units", token_validity_units)
        if write_attributes and not isinstance(write_attributes, list):
            raise TypeError("Expected argument 'write_attributes' to be a list")
        pulumi.set(__self__, "write_attributes", write_attributes)

    @property
    @pulumi.getter(name="accessTokenValidity")
    def access_token_validity(self) -> Optional[int]:
        return pulumi.get(self, "access_token_validity")

    @property
    @pulumi.getter(name="allowedOAuthFlows")
    def allowed_o_auth_flows(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "allowed_o_auth_flows")

    @property
    @pulumi.getter(name="allowedOAuthFlowsUserPoolClient")
    def allowed_o_auth_flows_user_pool_client(self) -> Optional[bool]:
        return pulumi.get(self, "allowed_o_auth_flows_user_pool_client")

    @property
    @pulumi.getter(name="allowedOAuthScopes")
    def allowed_o_auth_scopes(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "allowed_o_auth_scopes")

    @property
    @pulumi.getter(name="analyticsConfiguration")
    def analytics_configuration(self) -> Optional['outputs.UserPoolClientAnalyticsConfiguration']:
        return pulumi.get(self, "analytics_configuration")

    @property
    @pulumi.getter(name="authSessionValidity")
    def auth_session_validity(self) -> Optional[int]:
        return pulumi.get(self, "auth_session_validity")

    @property
    @pulumi.getter(name="callbackUrls")
    def callback_urls(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "callback_urls")

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[str]:
        return pulumi.get(self, "client_id")

    @property
    @pulumi.getter(name="clientName")
    def client_name(self) -> Optional[str]:
        return pulumi.get(self, "client_name")

    @property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[str]:
        return pulumi.get(self, "client_secret")

    @property
    @pulumi.getter(name="defaultRedirectUri")
    def default_redirect_uri(self) -> Optional[str]:
        return pulumi.get(self, "default_redirect_uri")

    @property
    @pulumi.getter(name="enablePropagateAdditionalUserContextData")
    def enable_propagate_additional_user_context_data(self) -> Optional[bool]:
        return pulumi.get(self, "enable_propagate_additional_user_context_data")

    @property
    @pulumi.getter(name="enableTokenRevocation")
    def enable_token_revocation(self) -> Optional[bool]:
        return pulumi.get(self, "enable_token_revocation")

    @property
    @pulumi.getter(name="explicitAuthFlows")
    def explicit_auth_flows(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "explicit_auth_flows")

    @property
    @pulumi.getter(name="idTokenValidity")
    def id_token_validity(self) -> Optional[int]:
        return pulumi.get(self, "id_token_validity")

    @property
    @pulumi.getter(name="logoutUrls")
    def logout_urls(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "logout_urls")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="preventUserExistenceErrors")
    def prevent_user_existence_errors(self) -> Optional[str]:
        return pulumi.get(self, "prevent_user_existence_errors")

    @property
    @pulumi.getter(name="readAttributes")
    def read_attributes(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "read_attributes")

    @property
    @pulumi.getter(name="refreshTokenValidity")
    def refresh_token_validity(self) -> Optional[int]:
        return pulumi.get(self, "refresh_token_validity")

    @property
    @pulumi.getter(name="supportedIdentityProviders")
    def supported_identity_providers(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "supported_identity_providers")

    @property
    @pulumi.getter(name="tokenValidityUnits")
    def token_validity_units(self) -> Optional['outputs.UserPoolClientTokenValidityUnits']:
        return pulumi.get(self, "token_validity_units")

    @property
    @pulumi.getter(name="writeAttributes")
    def write_attributes(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "write_attributes")


class AwaitableGetUserPoolClientResult(GetUserPoolClientResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetUserPoolClientResult(
            access_token_validity=self.access_token_validity,
            allowed_o_auth_flows=self.allowed_o_auth_flows,
            allowed_o_auth_flows_user_pool_client=self.allowed_o_auth_flows_user_pool_client,
            allowed_o_auth_scopes=self.allowed_o_auth_scopes,
            analytics_configuration=self.analytics_configuration,
            auth_session_validity=self.auth_session_validity,
            callback_urls=self.callback_urls,
            client_id=self.client_id,
            client_name=self.client_name,
            client_secret=self.client_secret,
            default_redirect_uri=self.default_redirect_uri,
            enable_propagate_additional_user_context_data=self.enable_propagate_additional_user_context_data,
            enable_token_revocation=self.enable_token_revocation,
            explicit_auth_flows=self.explicit_auth_flows,
            id_token_validity=self.id_token_validity,
            logout_urls=self.logout_urls,
            name=self.name,
            prevent_user_existence_errors=self.prevent_user_existence_errors,
            read_attributes=self.read_attributes,
            refresh_token_validity=self.refresh_token_validity,
            supported_identity_providers=self.supported_identity_providers,
            token_validity_units=self.token_validity_units,
            write_attributes=self.write_attributes)


def get_user_pool_client(client_id: Optional[str] = None,
                         user_pool_id: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetUserPoolClientResult:
    """
    Resource Type definition for AWS::Cognito::UserPoolClient
    """
    __args__ = dict()
    __args__['clientId'] = client_id
    __args__['userPoolId'] = user_pool_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:cognito:getUserPoolClient', __args__, opts=opts, typ=GetUserPoolClientResult).value

    return AwaitableGetUserPoolClientResult(
        access_token_validity=pulumi.get(__ret__, 'access_token_validity'),
        allowed_o_auth_flows=pulumi.get(__ret__, 'allowed_o_auth_flows'),
        allowed_o_auth_flows_user_pool_client=pulumi.get(__ret__, 'allowed_o_auth_flows_user_pool_client'),
        allowed_o_auth_scopes=pulumi.get(__ret__, 'allowed_o_auth_scopes'),
        analytics_configuration=pulumi.get(__ret__, 'analytics_configuration'),
        auth_session_validity=pulumi.get(__ret__, 'auth_session_validity'),
        callback_urls=pulumi.get(__ret__, 'callback_urls'),
        client_id=pulumi.get(__ret__, 'client_id'),
        client_name=pulumi.get(__ret__, 'client_name'),
        client_secret=pulumi.get(__ret__, 'client_secret'),
        default_redirect_uri=pulumi.get(__ret__, 'default_redirect_uri'),
        enable_propagate_additional_user_context_data=pulumi.get(__ret__, 'enable_propagate_additional_user_context_data'),
        enable_token_revocation=pulumi.get(__ret__, 'enable_token_revocation'),
        explicit_auth_flows=pulumi.get(__ret__, 'explicit_auth_flows'),
        id_token_validity=pulumi.get(__ret__, 'id_token_validity'),
        logout_urls=pulumi.get(__ret__, 'logout_urls'),
        name=pulumi.get(__ret__, 'name'),
        prevent_user_existence_errors=pulumi.get(__ret__, 'prevent_user_existence_errors'),
        read_attributes=pulumi.get(__ret__, 'read_attributes'),
        refresh_token_validity=pulumi.get(__ret__, 'refresh_token_validity'),
        supported_identity_providers=pulumi.get(__ret__, 'supported_identity_providers'),
        token_validity_units=pulumi.get(__ret__, 'token_validity_units'),
        write_attributes=pulumi.get(__ret__, 'write_attributes'))


@_utilities.lift_output_func(get_user_pool_client)
def get_user_pool_client_output(client_id: Optional[pulumi.Input[str]] = None,
                                user_pool_id: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetUserPoolClientResult]:
    """
    Resource Type definition for AWS::Cognito::UserPoolClient
    """
    ...
