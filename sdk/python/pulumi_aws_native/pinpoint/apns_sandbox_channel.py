# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['APNSSandboxChannelArgs', 'APNSSandboxChannel']

@pulumi.input_type
class APNSSandboxChannelArgs:
    def __init__(__self__, *,
                 application_id: pulumi.Input[str],
                 bundle_id: Optional[pulumi.Input[str]] = None,
                 certificate: Optional[pulumi.Input[str]] = None,
                 default_authentication_method: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 private_key: Optional[pulumi.Input[str]] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 token_key: Optional[pulumi.Input[str]] = None,
                 token_key_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a APNSSandboxChannel resource.
        """
        pulumi.set(__self__, "application_id", application_id)
        if bundle_id is not None:
            pulumi.set(__self__, "bundle_id", bundle_id)
        if certificate is not None:
            pulumi.set(__self__, "certificate", certificate)
        if default_authentication_method is not None:
            pulumi.set(__self__, "default_authentication_method", default_authentication_method)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if private_key is not None:
            pulumi.set(__self__, "private_key", private_key)
        if team_id is not None:
            pulumi.set(__self__, "team_id", team_id)
        if token_key is not None:
            pulumi.set(__self__, "token_key", token_key)
        if token_key_id is not None:
            pulumi.set(__self__, "token_key_id", token_key_id)

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "application_id")

    @application_id.setter
    def application_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "application_id", value)

    @property
    @pulumi.getter(name="bundleId")
    def bundle_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "bundle_id")

    @bundle_id.setter
    def bundle_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bundle_id", value)

    @property
    @pulumi.getter
    def certificate(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "certificate")

    @certificate.setter
    def certificate(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "certificate", value)

    @property
    @pulumi.getter(name="defaultAuthenticationMethod")
    def default_authentication_method(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "default_authentication_method")

    @default_authentication_method.setter
    def default_authentication_method(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_authentication_method", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "private_key")

    @private_key.setter
    def private_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_key", value)

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "team_id")

    @team_id.setter
    def team_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "team_id", value)

    @property
    @pulumi.getter(name="tokenKey")
    def token_key(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "token_key")

    @token_key.setter
    def token_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "token_key", value)

    @property
    @pulumi.getter(name="tokenKeyId")
    def token_key_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "token_key_id")

    @token_key_id.setter
    def token_key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "token_key_id", value)


warnings.warn("""APNSSandboxChannel is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class APNSSandboxChannel(pulumi.CustomResource):
    warnings.warn("""APNSSandboxChannel is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_id: Optional[pulumi.Input[str]] = None,
                 bundle_id: Optional[pulumi.Input[str]] = None,
                 certificate: Optional[pulumi.Input[str]] = None,
                 default_authentication_method: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 private_key: Optional[pulumi.Input[str]] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 token_key: Optional[pulumi.Input[str]] = None,
                 token_key_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Pinpoint::APNSSandboxChannel

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: APNSSandboxChannelArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Pinpoint::APNSSandboxChannel

        :param str resource_name: The name of the resource.
        :param APNSSandboxChannelArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(APNSSandboxChannelArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_id: Optional[pulumi.Input[str]] = None,
                 bundle_id: Optional[pulumi.Input[str]] = None,
                 certificate: Optional[pulumi.Input[str]] = None,
                 default_authentication_method: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 private_key: Optional[pulumi.Input[str]] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 token_key: Optional[pulumi.Input[str]] = None,
                 token_key_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""APNSSandboxChannel is deprecated: APNSSandboxChannel is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = APNSSandboxChannelArgs.__new__(APNSSandboxChannelArgs)

            if application_id is None and not opts.urn:
                raise TypeError("Missing required property 'application_id'")
            __props__.__dict__["application_id"] = application_id
            __props__.__dict__["bundle_id"] = bundle_id
            __props__.__dict__["certificate"] = certificate
            __props__.__dict__["default_authentication_method"] = default_authentication_method
            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["private_key"] = private_key
            __props__.__dict__["team_id"] = team_id
            __props__.__dict__["token_key"] = token_key
            __props__.__dict__["token_key_id"] = token_key_id
        super(APNSSandboxChannel, __self__).__init__(
            'aws-native:pinpoint:APNSSandboxChannel',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'APNSSandboxChannel':
        """
        Get an existing APNSSandboxChannel resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = APNSSandboxChannelArgs.__new__(APNSSandboxChannelArgs)

        __props__.__dict__["application_id"] = None
        __props__.__dict__["bundle_id"] = None
        __props__.__dict__["certificate"] = None
        __props__.__dict__["default_authentication_method"] = None
        __props__.__dict__["enabled"] = None
        __props__.__dict__["private_key"] = None
        __props__.__dict__["team_id"] = None
        __props__.__dict__["token_key"] = None
        __props__.__dict__["token_key_id"] = None
        return APNSSandboxChannel(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "application_id")

    @property
    @pulumi.getter(name="bundleId")
    def bundle_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "bundle_id")

    @property
    @pulumi.getter
    def certificate(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "certificate")

    @property
    @pulumi.getter(name="defaultAuthenticationMethod")
    def default_authentication_method(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "default_authentication_method")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "private_key")

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "team_id")

    @property
    @pulumi.getter(name="tokenKey")
    def token_key(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "token_key")

    @property
    @pulumi.getter(name="tokenKeyId")
    def token_key_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "token_key_id")

