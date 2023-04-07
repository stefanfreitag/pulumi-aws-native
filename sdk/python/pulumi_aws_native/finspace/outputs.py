# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = [
    'EnvironmentFederationParameters',
    'EnvironmentSuperuserParameters',
]

@pulumi.output_type
class EnvironmentFederationParameters(dict):
    """
    Additional parameters to identify Federation mode
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "applicationCallBackURL":
            suggest = "application_call_back_url"
        elif key == "attributeMap":
            suggest = "attribute_map"
        elif key == "federationProviderName":
            suggest = "federation_provider_name"
        elif key == "federationURN":
            suggest = "federation_urn"
        elif key == "samlMetadataDocument":
            suggest = "saml_metadata_document"
        elif key == "samlMetadataURL":
            suggest = "saml_metadata_url"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in EnvironmentFederationParameters. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        EnvironmentFederationParameters.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        EnvironmentFederationParameters.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 application_call_back_url: Optional[str] = None,
                 attribute_map: Optional[Any] = None,
                 federation_provider_name: Optional[str] = None,
                 federation_urn: Optional[str] = None,
                 saml_metadata_document: Optional[str] = None,
                 saml_metadata_url: Optional[str] = None):
        """
        Additional parameters to identify Federation mode
        :param str application_call_back_url: SAML metadata URL to link with the Environment
        :param Any attribute_map: Attribute map for SAML configuration
        :param str federation_provider_name: Federation provider name to link with the Environment
        :param str federation_urn: SAML metadata URL to link with the Environment
        :param str saml_metadata_document: SAML metadata document to link the federation provider to the Environment
        :param str saml_metadata_url: SAML metadata URL to link with the Environment
        """
        if application_call_back_url is not None:
            pulumi.set(__self__, "application_call_back_url", application_call_back_url)
        if attribute_map is not None:
            pulumi.set(__self__, "attribute_map", attribute_map)
        if federation_provider_name is not None:
            pulumi.set(__self__, "federation_provider_name", federation_provider_name)
        if federation_urn is not None:
            pulumi.set(__self__, "federation_urn", federation_urn)
        if saml_metadata_document is not None:
            pulumi.set(__self__, "saml_metadata_document", saml_metadata_document)
        if saml_metadata_url is not None:
            pulumi.set(__self__, "saml_metadata_url", saml_metadata_url)

    @property
    @pulumi.getter(name="applicationCallBackURL")
    def application_call_back_url(self) -> Optional[str]:
        """
        SAML metadata URL to link with the Environment
        """
        return pulumi.get(self, "application_call_back_url")

    @property
    @pulumi.getter(name="attributeMap")
    def attribute_map(self) -> Optional[Any]:
        """
        Attribute map for SAML configuration
        """
        return pulumi.get(self, "attribute_map")

    @property
    @pulumi.getter(name="federationProviderName")
    def federation_provider_name(self) -> Optional[str]:
        """
        Federation provider name to link with the Environment
        """
        return pulumi.get(self, "federation_provider_name")

    @property
    @pulumi.getter(name="federationURN")
    def federation_urn(self) -> Optional[str]:
        """
        SAML metadata URL to link with the Environment
        """
        return pulumi.get(self, "federation_urn")

    @property
    @pulumi.getter(name="samlMetadataDocument")
    def saml_metadata_document(self) -> Optional[str]:
        """
        SAML metadata document to link the federation provider to the Environment
        """
        return pulumi.get(self, "saml_metadata_document")

    @property
    @pulumi.getter(name="samlMetadataURL")
    def saml_metadata_url(self) -> Optional[str]:
        """
        SAML metadata URL to link with the Environment
        """
        return pulumi.get(self, "saml_metadata_url")


@pulumi.output_type
class EnvironmentSuperuserParameters(dict):
    """
    Parameters of the first Superuser for the FinSpace Environment
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "emailAddress":
            suggest = "email_address"
        elif key == "firstName":
            suggest = "first_name"
        elif key == "lastName":
            suggest = "last_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in EnvironmentSuperuserParameters. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        EnvironmentSuperuserParameters.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        EnvironmentSuperuserParameters.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 email_address: Optional[str] = None,
                 first_name: Optional[str] = None,
                 last_name: Optional[str] = None):
        """
        Parameters of the first Superuser for the FinSpace Environment
        :param str email_address: Email address
        :param str first_name: First name
        :param str last_name: Last name
        """
        if email_address is not None:
            pulumi.set(__self__, "email_address", email_address)
        if first_name is not None:
            pulumi.set(__self__, "first_name", first_name)
        if last_name is not None:
            pulumi.set(__self__, "last_name", last_name)

    @property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> Optional[str]:
        """
        Email address
        """
        return pulumi.get(self, "email_address")

    @property
    @pulumi.getter(name="firstName")
    def first_name(self) -> Optional[str]:
        """
        First name
        """
        return pulumi.get(self, "first_name")

    @property
    @pulumi.getter(name="lastName")
    def last_name(self) -> Optional[str]:
        """
        Last name
        """
        return pulumi.get(self, "last_name")


