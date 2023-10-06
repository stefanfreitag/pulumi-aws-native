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

__all__ = ['KeyPairArgs', 'KeyPair']

@pulumi.input_type
class KeyPairArgs:
    def __init__(__self__, *,
                 key_name: pulumi.Input[str],
                 key_format: Optional[pulumi.Input['KeyPairKeyFormat']] = None,
                 key_type: Optional[pulumi.Input['KeyPairKeyType']] = None,
                 public_key_material: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['KeyPairTagArgs']]]] = None):
        """
        The set of arguments for constructing a KeyPair resource.
        :param pulumi.Input[str] key_name: The name of the SSH key pair
        :param pulumi.Input['KeyPairKeyFormat'] key_format: The format of the private key
        :param pulumi.Input['KeyPairKeyType'] key_type: The crypto-system used to generate a key pair.
        :param pulumi.Input[str] public_key_material: Plain text public key to import
        :param pulumi.Input[Sequence[pulumi.Input['KeyPairTagArgs']]] tags: An array of key-value pairs to apply to this resource.
        """
        KeyPairArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            key_name=key_name,
            key_format=key_format,
            key_type=key_type,
            public_key_material=public_key_material,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             key_name: pulumi.Input[str],
             key_format: Optional[pulumi.Input['KeyPairKeyFormat']] = None,
             key_type: Optional[pulumi.Input['KeyPairKeyType']] = None,
             public_key_material: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Sequence[pulumi.Input['KeyPairTagArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("key_name", key_name)
        if key_format is not None:
            _setter("key_format", key_format)
        if key_type is not None:
            _setter("key_type", key_type)
        if public_key_material is not None:
            _setter("public_key_material", public_key_material)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter(name="keyName")
    def key_name(self) -> pulumi.Input[str]:
        """
        The name of the SSH key pair
        """
        return pulumi.get(self, "key_name")

    @key_name.setter
    def key_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "key_name", value)

    @property
    @pulumi.getter(name="keyFormat")
    def key_format(self) -> Optional[pulumi.Input['KeyPairKeyFormat']]:
        """
        The format of the private key
        """
        return pulumi.get(self, "key_format")

    @key_format.setter
    def key_format(self, value: Optional[pulumi.Input['KeyPairKeyFormat']]):
        pulumi.set(self, "key_format", value)

    @property
    @pulumi.getter(name="keyType")
    def key_type(self) -> Optional[pulumi.Input['KeyPairKeyType']]:
        """
        The crypto-system used to generate a key pair.
        """
        return pulumi.get(self, "key_type")

    @key_type.setter
    def key_type(self, value: Optional[pulumi.Input['KeyPairKeyType']]):
        pulumi.set(self, "key_type", value)

    @property
    @pulumi.getter(name="publicKeyMaterial")
    def public_key_material(self) -> Optional[pulumi.Input[str]]:
        """
        Plain text public key to import
        """
        return pulumi.get(self, "public_key_material")

    @public_key_material.setter
    def public_key_material(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "public_key_material", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['KeyPairTagArgs']]]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['KeyPairTagArgs']]]]):
        pulumi.set(self, "tags", value)


class KeyPair(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 key_format: Optional[pulumi.Input['KeyPairKeyFormat']] = None,
                 key_name: Optional[pulumi.Input[str]] = None,
                 key_type: Optional[pulumi.Input['KeyPairKeyType']] = None,
                 public_key_material: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['KeyPairTagArgs']]]]] = None,
                 __props__=None):
        """
        The AWS::EC2::KeyPair creates an SSH key pair

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input['KeyPairKeyFormat'] key_format: The format of the private key
        :param pulumi.Input[str] key_name: The name of the SSH key pair
        :param pulumi.Input['KeyPairKeyType'] key_type: The crypto-system used to generate a key pair.
        :param pulumi.Input[str] public_key_material: Plain text public key to import
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['KeyPairTagArgs']]]] tags: An array of key-value pairs to apply to this resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: KeyPairArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The AWS::EC2::KeyPair creates an SSH key pair

        :param str resource_name: The name of the resource.
        :param KeyPairArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(KeyPairArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            KeyPairArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 key_format: Optional[pulumi.Input['KeyPairKeyFormat']] = None,
                 key_name: Optional[pulumi.Input[str]] = None,
                 key_type: Optional[pulumi.Input['KeyPairKeyType']] = None,
                 public_key_material: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['KeyPairTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = KeyPairArgs.__new__(KeyPairArgs)

            __props__.__dict__["key_format"] = key_format
            if key_name is None and not opts.urn:
                raise TypeError("Missing required property 'key_name'")
            __props__.__dict__["key_name"] = key_name
            __props__.__dict__["key_type"] = key_type
            __props__.__dict__["public_key_material"] = public_key_material
            __props__.__dict__["tags"] = tags
            __props__.__dict__["key_fingerprint"] = None
            __props__.__dict__["key_pair_id"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["key_format", "key_name", "key_type", "public_key_material", "tags[*]"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(KeyPair, __self__).__init__(
            'aws-native:ec2:KeyPair',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'KeyPair':
        """
        Get an existing KeyPair resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = KeyPairArgs.__new__(KeyPairArgs)

        __props__.__dict__["key_fingerprint"] = None
        __props__.__dict__["key_format"] = None
        __props__.__dict__["key_name"] = None
        __props__.__dict__["key_pair_id"] = None
        __props__.__dict__["key_type"] = None
        __props__.__dict__["public_key_material"] = None
        __props__.__dict__["tags"] = None
        return KeyPair(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="keyFingerprint")
    def key_fingerprint(self) -> pulumi.Output[str]:
        """
        A short sequence of bytes used for public key verification
        """
        return pulumi.get(self, "key_fingerprint")

    @property
    @pulumi.getter(name="keyFormat")
    def key_format(self) -> pulumi.Output[Optional['KeyPairKeyFormat']]:
        """
        The format of the private key
        """
        return pulumi.get(self, "key_format")

    @property
    @pulumi.getter(name="keyName")
    def key_name(self) -> pulumi.Output[str]:
        """
        The name of the SSH key pair
        """
        return pulumi.get(self, "key_name")

    @property
    @pulumi.getter(name="keyPairId")
    def key_pair_id(self) -> pulumi.Output[str]:
        """
        An AWS generated ID for the key pair
        """
        return pulumi.get(self, "key_pair_id")

    @property
    @pulumi.getter(name="keyType")
    def key_type(self) -> pulumi.Output[Optional['KeyPairKeyType']]:
        """
        The crypto-system used to generate a key pair.
        """
        return pulumi.get(self, "key_type")

    @property
    @pulumi.getter(name="publicKeyMaterial")
    def public_key_material(self) -> pulumi.Output[Optional[str]]:
        """
        Plain text public key to import
        """
        return pulumi.get(self, "public_key_material")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.KeyPairTag']]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

