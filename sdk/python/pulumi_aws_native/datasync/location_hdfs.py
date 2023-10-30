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
from ._enums import *
from ._inputs import *

__all__ = ['LocationHdfsArgs', 'LocationHdfs']

@pulumi.input_type
class LocationHdfsArgs:
    def __init__(__self__, *,
                 agent_arns: pulumi.Input[Sequence[pulumi.Input[str]]],
                 authentication_type: pulumi.Input['LocationHdfsAuthenticationType'],
                 name_nodes: pulumi.Input[Sequence[pulumi.Input['LocationHdfsNameNodeArgs']]],
                 block_size: Optional[pulumi.Input[int]] = None,
                 kerberos_keytab: Optional[pulumi.Input[str]] = None,
                 kerberos_krb5_conf: Optional[pulumi.Input[str]] = None,
                 kerberos_principal: Optional[pulumi.Input[str]] = None,
                 kms_key_provider_uri: Optional[pulumi.Input[str]] = None,
                 qop_configuration: Optional[pulumi.Input['LocationHdfsQopConfigurationArgs']] = None,
                 replication_factor: Optional[pulumi.Input[int]] = None,
                 simple_user: Optional[pulumi.Input[str]] = None,
                 subdirectory: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['LocationHdfsTagArgs']]]] = None):
        """
        The set of arguments for constructing a LocationHdfs resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] agent_arns: ARN(s) of the agent(s) to use for an HDFS location.
        :param pulumi.Input['LocationHdfsAuthenticationType'] authentication_type: The authentication mode used to determine identity of user.
        :param pulumi.Input[Sequence[pulumi.Input['LocationHdfsNameNodeArgs']]] name_nodes: An array of Name Node(s) of the HDFS location.
        :param pulumi.Input[int] block_size: Size of chunks (blocks) in bytes that the data is divided into when stored in the HDFS cluster.
        :param pulumi.Input[str] kerberos_keytab: The Base64 string representation of the Keytab file.
        :param pulumi.Input[str] kerberos_krb5_conf: The string representation of the Krb5Conf file, or the presigned URL to access the Krb5.conf file within an S3 bucket.
        :param pulumi.Input[str] kerberos_principal: The unique identity, or principal, to which Kerberos can assign tickets.
        :param pulumi.Input[str] kms_key_provider_uri: The identifier for the Key Management Server where the encryption keys that encrypt data inside HDFS clusters are stored.
        :param pulumi.Input[int] replication_factor: Number of copies of each block that exists inside the HDFS cluster.
        :param pulumi.Input[str] simple_user: The user name that has read and write permissions on the specified HDFS cluster.
        :param pulumi.Input[str] subdirectory: The subdirectory in HDFS that is used to read data from the HDFS source location or write data to the HDFS destination.
        :param pulumi.Input[Sequence[pulumi.Input['LocationHdfsTagArgs']]] tags: An array of key-value pairs to apply to this resource.
        """
        pulumi.set(__self__, "agent_arns", agent_arns)
        pulumi.set(__self__, "authentication_type", authentication_type)
        pulumi.set(__self__, "name_nodes", name_nodes)
        if block_size is not None:
            pulumi.set(__self__, "block_size", block_size)
        if kerberos_keytab is not None:
            pulumi.set(__self__, "kerberos_keytab", kerberos_keytab)
        if kerberos_krb5_conf is not None:
            pulumi.set(__self__, "kerberos_krb5_conf", kerberos_krb5_conf)
        if kerberos_principal is not None:
            pulumi.set(__self__, "kerberos_principal", kerberos_principal)
        if kms_key_provider_uri is not None:
            pulumi.set(__self__, "kms_key_provider_uri", kms_key_provider_uri)
        if qop_configuration is not None:
            pulumi.set(__self__, "qop_configuration", qop_configuration)
        if replication_factor is not None:
            pulumi.set(__self__, "replication_factor", replication_factor)
        if simple_user is not None:
            pulumi.set(__self__, "simple_user", simple_user)
        if subdirectory is not None:
            pulumi.set(__self__, "subdirectory", subdirectory)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="agentArns")
    def agent_arns(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        ARN(s) of the agent(s) to use for an HDFS location.
        """
        return pulumi.get(self, "agent_arns")

    @agent_arns.setter
    def agent_arns(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "agent_arns", value)

    @property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> pulumi.Input['LocationHdfsAuthenticationType']:
        """
        The authentication mode used to determine identity of user.
        """
        return pulumi.get(self, "authentication_type")

    @authentication_type.setter
    def authentication_type(self, value: pulumi.Input['LocationHdfsAuthenticationType']):
        pulumi.set(self, "authentication_type", value)

    @property
    @pulumi.getter(name="nameNodes")
    def name_nodes(self) -> pulumi.Input[Sequence[pulumi.Input['LocationHdfsNameNodeArgs']]]:
        """
        An array of Name Node(s) of the HDFS location.
        """
        return pulumi.get(self, "name_nodes")

    @name_nodes.setter
    def name_nodes(self, value: pulumi.Input[Sequence[pulumi.Input['LocationHdfsNameNodeArgs']]]):
        pulumi.set(self, "name_nodes", value)

    @property
    @pulumi.getter(name="blockSize")
    def block_size(self) -> Optional[pulumi.Input[int]]:
        """
        Size of chunks (blocks) in bytes that the data is divided into when stored in the HDFS cluster.
        """
        return pulumi.get(self, "block_size")

    @block_size.setter
    def block_size(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "block_size", value)

    @property
    @pulumi.getter(name="kerberosKeytab")
    def kerberos_keytab(self) -> Optional[pulumi.Input[str]]:
        """
        The Base64 string representation of the Keytab file.
        """
        return pulumi.get(self, "kerberos_keytab")

    @kerberos_keytab.setter
    def kerberos_keytab(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kerberos_keytab", value)

    @property
    @pulumi.getter(name="kerberosKrb5Conf")
    def kerberos_krb5_conf(self) -> Optional[pulumi.Input[str]]:
        """
        The string representation of the Krb5Conf file, or the presigned URL to access the Krb5.conf file within an S3 bucket.
        """
        return pulumi.get(self, "kerberos_krb5_conf")

    @kerberos_krb5_conf.setter
    def kerberos_krb5_conf(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kerberos_krb5_conf", value)

    @property
    @pulumi.getter(name="kerberosPrincipal")
    def kerberos_principal(self) -> Optional[pulumi.Input[str]]:
        """
        The unique identity, or principal, to which Kerberos can assign tickets.
        """
        return pulumi.get(self, "kerberos_principal")

    @kerberos_principal.setter
    def kerberos_principal(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kerberos_principal", value)

    @property
    @pulumi.getter(name="kmsKeyProviderUri")
    def kms_key_provider_uri(self) -> Optional[pulumi.Input[str]]:
        """
        The identifier for the Key Management Server where the encryption keys that encrypt data inside HDFS clusters are stored.
        """
        return pulumi.get(self, "kms_key_provider_uri")

    @kms_key_provider_uri.setter
    def kms_key_provider_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_key_provider_uri", value)

    @property
    @pulumi.getter(name="qopConfiguration")
    def qop_configuration(self) -> Optional[pulumi.Input['LocationHdfsQopConfigurationArgs']]:
        return pulumi.get(self, "qop_configuration")

    @qop_configuration.setter
    def qop_configuration(self, value: Optional[pulumi.Input['LocationHdfsQopConfigurationArgs']]):
        pulumi.set(self, "qop_configuration", value)

    @property
    @pulumi.getter(name="replicationFactor")
    def replication_factor(self) -> Optional[pulumi.Input[int]]:
        """
        Number of copies of each block that exists inside the HDFS cluster.
        """
        return pulumi.get(self, "replication_factor")

    @replication_factor.setter
    def replication_factor(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "replication_factor", value)

    @property
    @pulumi.getter(name="simpleUser")
    def simple_user(self) -> Optional[pulumi.Input[str]]:
        """
        The user name that has read and write permissions on the specified HDFS cluster.
        """
        return pulumi.get(self, "simple_user")

    @simple_user.setter
    def simple_user(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "simple_user", value)

    @property
    @pulumi.getter
    def subdirectory(self) -> Optional[pulumi.Input[str]]:
        """
        The subdirectory in HDFS that is used to read data from the HDFS source location or write data to the HDFS destination.
        """
        return pulumi.get(self, "subdirectory")

    @subdirectory.setter
    def subdirectory(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subdirectory", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['LocationHdfsTagArgs']]]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['LocationHdfsTagArgs']]]]):
        pulumi.set(self, "tags", value)


class LocationHdfs(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 agent_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 authentication_type: Optional[pulumi.Input['LocationHdfsAuthenticationType']] = None,
                 block_size: Optional[pulumi.Input[int]] = None,
                 kerberos_keytab: Optional[pulumi.Input[str]] = None,
                 kerberos_krb5_conf: Optional[pulumi.Input[str]] = None,
                 kerberos_principal: Optional[pulumi.Input[str]] = None,
                 kms_key_provider_uri: Optional[pulumi.Input[str]] = None,
                 name_nodes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LocationHdfsNameNodeArgs']]]]] = None,
                 qop_configuration: Optional[pulumi.Input[pulumi.InputType['LocationHdfsQopConfigurationArgs']]] = None,
                 replication_factor: Optional[pulumi.Input[int]] = None,
                 simple_user: Optional[pulumi.Input[str]] = None,
                 subdirectory: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LocationHdfsTagArgs']]]]] = None,
                 __props__=None):
        """
        Resource schema for AWS::DataSync::LocationHDFS.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] agent_arns: ARN(s) of the agent(s) to use for an HDFS location.
        :param pulumi.Input['LocationHdfsAuthenticationType'] authentication_type: The authentication mode used to determine identity of user.
        :param pulumi.Input[int] block_size: Size of chunks (blocks) in bytes that the data is divided into when stored in the HDFS cluster.
        :param pulumi.Input[str] kerberos_keytab: The Base64 string representation of the Keytab file.
        :param pulumi.Input[str] kerberos_krb5_conf: The string representation of the Krb5Conf file, or the presigned URL to access the Krb5.conf file within an S3 bucket.
        :param pulumi.Input[str] kerberos_principal: The unique identity, or principal, to which Kerberos can assign tickets.
        :param pulumi.Input[str] kms_key_provider_uri: The identifier for the Key Management Server where the encryption keys that encrypt data inside HDFS clusters are stored.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LocationHdfsNameNodeArgs']]]] name_nodes: An array of Name Node(s) of the HDFS location.
        :param pulumi.Input[int] replication_factor: Number of copies of each block that exists inside the HDFS cluster.
        :param pulumi.Input[str] simple_user: The user name that has read and write permissions on the specified HDFS cluster.
        :param pulumi.Input[str] subdirectory: The subdirectory in HDFS that is used to read data from the HDFS source location or write data to the HDFS destination.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LocationHdfsTagArgs']]]] tags: An array of key-value pairs to apply to this resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LocationHdfsArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource schema for AWS::DataSync::LocationHDFS.

        :param str resource_name: The name of the resource.
        :param LocationHdfsArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LocationHdfsArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 agent_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 authentication_type: Optional[pulumi.Input['LocationHdfsAuthenticationType']] = None,
                 block_size: Optional[pulumi.Input[int]] = None,
                 kerberos_keytab: Optional[pulumi.Input[str]] = None,
                 kerberos_krb5_conf: Optional[pulumi.Input[str]] = None,
                 kerberos_principal: Optional[pulumi.Input[str]] = None,
                 kms_key_provider_uri: Optional[pulumi.Input[str]] = None,
                 name_nodes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LocationHdfsNameNodeArgs']]]]] = None,
                 qop_configuration: Optional[pulumi.Input[pulumi.InputType['LocationHdfsQopConfigurationArgs']]] = None,
                 replication_factor: Optional[pulumi.Input[int]] = None,
                 simple_user: Optional[pulumi.Input[str]] = None,
                 subdirectory: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LocationHdfsTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LocationHdfsArgs.__new__(LocationHdfsArgs)

            if agent_arns is None and not opts.urn:
                raise TypeError("Missing required property 'agent_arns'")
            __props__.__dict__["agent_arns"] = agent_arns
            if authentication_type is None and not opts.urn:
                raise TypeError("Missing required property 'authentication_type'")
            __props__.__dict__["authentication_type"] = authentication_type
            __props__.__dict__["block_size"] = block_size
            __props__.__dict__["kerberos_keytab"] = kerberos_keytab
            __props__.__dict__["kerberos_krb5_conf"] = kerberos_krb5_conf
            __props__.__dict__["kerberos_principal"] = kerberos_principal
            __props__.__dict__["kms_key_provider_uri"] = kms_key_provider_uri
            if name_nodes is None and not opts.urn:
                raise TypeError("Missing required property 'name_nodes'")
            __props__.__dict__["name_nodes"] = name_nodes
            __props__.__dict__["qop_configuration"] = qop_configuration
            __props__.__dict__["replication_factor"] = replication_factor
            __props__.__dict__["simple_user"] = simple_user
            __props__.__dict__["subdirectory"] = subdirectory
            __props__.__dict__["tags"] = tags
            __props__.__dict__["location_arn"] = None
            __props__.__dict__["location_uri"] = None
        super(LocationHdfs, __self__).__init__(
            'aws-native:datasync:LocationHdfs',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'LocationHdfs':
        """
        Get an existing LocationHdfs resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = LocationHdfsArgs.__new__(LocationHdfsArgs)

        __props__.__dict__["agent_arns"] = None
        __props__.__dict__["authentication_type"] = None
        __props__.__dict__["block_size"] = None
        __props__.__dict__["kerberos_keytab"] = None
        __props__.__dict__["kerberos_krb5_conf"] = None
        __props__.__dict__["kerberos_principal"] = None
        __props__.__dict__["kms_key_provider_uri"] = None
        __props__.__dict__["location_arn"] = None
        __props__.__dict__["location_uri"] = None
        __props__.__dict__["name_nodes"] = None
        __props__.__dict__["qop_configuration"] = None
        __props__.__dict__["replication_factor"] = None
        __props__.__dict__["simple_user"] = None
        __props__.__dict__["subdirectory"] = None
        __props__.__dict__["tags"] = None
        return LocationHdfs(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="agentArns")
    def agent_arns(self) -> pulumi.Output[Sequence[str]]:
        """
        ARN(s) of the agent(s) to use for an HDFS location.
        """
        return pulumi.get(self, "agent_arns")

    @property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> pulumi.Output['LocationHdfsAuthenticationType']:
        """
        The authentication mode used to determine identity of user.
        """
        return pulumi.get(self, "authentication_type")

    @property
    @pulumi.getter(name="blockSize")
    def block_size(self) -> pulumi.Output[Optional[int]]:
        """
        Size of chunks (blocks) in bytes that the data is divided into when stored in the HDFS cluster.
        """
        return pulumi.get(self, "block_size")

    @property
    @pulumi.getter(name="kerberosKeytab")
    def kerberos_keytab(self) -> pulumi.Output[Optional[str]]:
        """
        The Base64 string representation of the Keytab file.
        """
        return pulumi.get(self, "kerberos_keytab")

    @property
    @pulumi.getter(name="kerberosKrb5Conf")
    def kerberos_krb5_conf(self) -> pulumi.Output[Optional[str]]:
        """
        The string representation of the Krb5Conf file, or the presigned URL to access the Krb5.conf file within an S3 bucket.
        """
        return pulumi.get(self, "kerberos_krb5_conf")

    @property
    @pulumi.getter(name="kerberosPrincipal")
    def kerberos_principal(self) -> pulumi.Output[Optional[str]]:
        """
        The unique identity, or principal, to which Kerberos can assign tickets.
        """
        return pulumi.get(self, "kerberos_principal")

    @property
    @pulumi.getter(name="kmsKeyProviderUri")
    def kms_key_provider_uri(self) -> pulumi.Output[Optional[str]]:
        """
        The identifier for the Key Management Server where the encryption keys that encrypt data inside HDFS clusters are stored.
        """
        return pulumi.get(self, "kms_key_provider_uri")

    @property
    @pulumi.getter(name="locationArn")
    def location_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the HDFS location.
        """
        return pulumi.get(self, "location_arn")

    @property
    @pulumi.getter(name="locationUri")
    def location_uri(self) -> pulumi.Output[str]:
        """
        The URL of the HDFS location that was described.
        """
        return pulumi.get(self, "location_uri")

    @property
    @pulumi.getter(name="nameNodes")
    def name_nodes(self) -> pulumi.Output[Sequence['outputs.LocationHdfsNameNode']]:
        """
        An array of Name Node(s) of the HDFS location.
        """
        return pulumi.get(self, "name_nodes")

    @property
    @pulumi.getter(name="qopConfiguration")
    def qop_configuration(self) -> pulumi.Output[Optional['outputs.LocationHdfsQopConfiguration']]:
        return pulumi.get(self, "qop_configuration")

    @property
    @pulumi.getter(name="replicationFactor")
    def replication_factor(self) -> pulumi.Output[Optional[int]]:
        """
        Number of copies of each block that exists inside the HDFS cluster.
        """
        return pulumi.get(self, "replication_factor")

    @property
    @pulumi.getter(name="simpleUser")
    def simple_user(self) -> pulumi.Output[Optional[str]]:
        """
        The user name that has read and write permissions on the specified HDFS cluster.
        """
        return pulumi.get(self, "simple_user")

    @property
    @pulumi.getter
    def subdirectory(self) -> pulumi.Output[Optional[str]]:
        """
        The subdirectory in HDFS that is used to read data from the HDFS source location or write data to the HDFS destination.
        """
        return pulumi.get(self, "subdirectory")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.LocationHdfsTag']]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

