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
    'EnvironmentFederationParametersAttributeMapItemPropertiesArgs',
    'EnvironmentFederationParametersArgs',
    'EnvironmentSuperuserParametersArgs',
    'EnvironmentTagArgs',
]

@pulumi.input_type
class EnvironmentFederationParametersAttributeMapItemPropertiesArgs:
    def __init__(__self__, *,
                 key: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] key: The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        :param pulumi.Input[str] value: The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        if key is not None:
            pulumi.set(__self__, "key", key)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        """
        The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        """
        The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class EnvironmentFederationParametersArgs:
    def __init__(__self__, *,
                 application_call_back_url: Optional[pulumi.Input[str]] = None,
                 attribute_map: Optional[pulumi.Input[Sequence[pulumi.Input['EnvironmentFederationParametersAttributeMapItemPropertiesArgs']]]] = None,
                 federation_provider_name: Optional[pulumi.Input[str]] = None,
                 federation_urn: Optional[pulumi.Input[str]] = None,
                 saml_metadata_document: Optional[pulumi.Input[str]] = None,
                 saml_metadata_url: Optional[pulumi.Input[str]] = None):
        """
        Additional parameters to identify Federation mode
        :param pulumi.Input[str] application_call_back_url: SAML metadata URL to link with the Environment
        :param pulumi.Input[Sequence[pulumi.Input['EnvironmentFederationParametersAttributeMapItemPropertiesArgs']]] attribute_map: Attribute map for SAML configuration
        :param pulumi.Input[str] federation_provider_name: Federation provider name to link with the Environment
        :param pulumi.Input[str] federation_urn: SAML metadata URL to link with the Environment
        :param pulumi.Input[str] saml_metadata_document: SAML metadata document to link the federation provider to the Environment
        :param pulumi.Input[str] saml_metadata_url: SAML metadata URL to link with the Environment
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
    @pulumi.getter(name="applicationCallBackUrl")
    def application_call_back_url(self) -> Optional[pulumi.Input[str]]:
        """
        SAML metadata URL to link with the Environment
        """
        return pulumi.get(self, "application_call_back_url")

    @application_call_back_url.setter
    def application_call_back_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "application_call_back_url", value)

    @property
    @pulumi.getter(name="attributeMap")
    def attribute_map(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['EnvironmentFederationParametersAttributeMapItemPropertiesArgs']]]]:
        """
        Attribute map for SAML configuration
        """
        return pulumi.get(self, "attribute_map")

    @attribute_map.setter
    def attribute_map(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['EnvironmentFederationParametersAttributeMapItemPropertiesArgs']]]]):
        pulumi.set(self, "attribute_map", value)

    @property
    @pulumi.getter(name="federationProviderName")
    def federation_provider_name(self) -> Optional[pulumi.Input[str]]:
        """
        Federation provider name to link with the Environment
        """
        return pulumi.get(self, "federation_provider_name")

    @federation_provider_name.setter
    def federation_provider_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "federation_provider_name", value)

    @property
    @pulumi.getter(name="federationUrn")
    def federation_urn(self) -> Optional[pulumi.Input[str]]:
        """
        SAML metadata URL to link with the Environment
        """
        return pulumi.get(self, "federation_urn")

    @federation_urn.setter
    def federation_urn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "federation_urn", value)

    @property
    @pulumi.getter(name="samlMetadataDocument")
    def saml_metadata_document(self) -> Optional[pulumi.Input[str]]:
        """
        SAML metadata document to link the federation provider to the Environment
        """
        return pulumi.get(self, "saml_metadata_document")

    @saml_metadata_document.setter
    def saml_metadata_document(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "saml_metadata_document", value)

    @property
    @pulumi.getter(name="samlMetadataUrl")
    def saml_metadata_url(self) -> Optional[pulumi.Input[str]]:
        """
        SAML metadata URL to link with the Environment
        """
        return pulumi.get(self, "saml_metadata_url")

    @saml_metadata_url.setter
    def saml_metadata_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "saml_metadata_url", value)


@pulumi.input_type
class EnvironmentSuperuserParametersArgs:
    def __init__(__self__, *,
                 email_address: Optional[pulumi.Input[str]] = None,
                 first_name: Optional[pulumi.Input[str]] = None,
                 last_name: Optional[pulumi.Input[str]] = None):
        """
        Parameters of the first Superuser for the FinSpace Environment
        :param pulumi.Input[str] email_address: Email address
        :param pulumi.Input[str] first_name: First name
        :param pulumi.Input[str] last_name: Last name
        """
        if email_address is not None:
            pulumi.set(__self__, "email_address", email_address)
        if first_name is not None:
            pulumi.set(__self__, "first_name", first_name)
        if last_name is not None:
            pulumi.set(__self__, "last_name", last_name)

    @property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> Optional[pulumi.Input[str]]:
        """
        Email address
        """
        return pulumi.get(self, "email_address")

    @email_address.setter
    def email_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "email_address", value)

    @property
    @pulumi.getter(name="firstName")
    def first_name(self) -> Optional[pulumi.Input[str]]:
        """
        First name
        """
        return pulumi.get(self, "first_name")

    @first_name.setter
    def first_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "first_name", value)

    @property
    @pulumi.getter(name="lastName")
    def last_name(self) -> Optional[pulumi.Input[str]]:
        """
        Last name
        """
        return pulumi.get(self, "last_name")

    @last_name.setter
    def last_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_name", value)


@pulumi.input_type
class EnvironmentTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        A list of all tags for a resource.
        :param pulumi.Input[str] key: The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        :param pulumi.Input[str] value: The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


