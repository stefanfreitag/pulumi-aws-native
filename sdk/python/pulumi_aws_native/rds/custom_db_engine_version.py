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

__all__ = ['CustomDbEngineVersionArgs', 'CustomDbEngineVersion']

@pulumi.input_type
class CustomDbEngineVersionArgs:
    def __init__(__self__, *,
                 database_installation_files_s3_bucket_name: pulumi.Input[str],
                 engine: pulumi.Input[str],
                 engine_version: pulumi.Input[str],
                 database_installation_files_s3_prefix: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 manifest: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input['CustomDbEngineVersionStatus']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['CustomDbEngineVersionTagArgs']]]] = None):
        """
        The set of arguments for constructing a CustomDbEngineVersion resource.
        :param pulumi.Input[str] database_installation_files_s3_bucket_name: The name of an Amazon S3 bucket that contains database installation files for your CEV. For example, a valid bucket name is `my-custom-installation-files`.
        :param pulumi.Input[str] engine: The database engine to use for your custom engine version (CEV). The only supported value is `custom-oracle-ee`.
        :param pulumi.Input[str] engine_version: The name of your CEV. The name format is 19.customized_string . For example, a valid name is 19.my_cev1. This setting is required for RDS Custom for Oracle, but optional for Amazon RDS. The combination of Engine and EngineVersion is unique per customer per Region.
        :param pulumi.Input[str] database_installation_files_s3_prefix: The Amazon S3 directory that contains the database installation files for your CEV. For example, a valid bucket name is `123456789012/cev1`. If this setting isn't specified, no prefix is assumed.
        :param pulumi.Input[str] description: An optional description of your CEV.
        :param pulumi.Input[str] kms_key_id: The AWS KMS key identifier for an encrypted CEV. A symmetric KMS key is required for RDS Custom, but optional for Amazon RDS.
        :param pulumi.Input[str] manifest: The CEV manifest, which is a JSON document that describes the installation .zip files stored in Amazon S3. Specify the name/value pairs in a file or a quoted string. RDS Custom applies the patches in the order in which they are listed.
        :param pulumi.Input['CustomDbEngineVersionStatus'] status: The availability status to be assigned to the CEV.
        :param pulumi.Input[Sequence[pulumi.Input['CustomDbEngineVersionTagArgs']]] tags: An array of key-value pairs to apply to this resource.
        """
        CustomDbEngineVersionArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            database_installation_files_s3_bucket_name=database_installation_files_s3_bucket_name,
            engine=engine,
            engine_version=engine_version,
            database_installation_files_s3_prefix=database_installation_files_s3_prefix,
            description=description,
            kms_key_id=kms_key_id,
            manifest=manifest,
            status=status,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             database_installation_files_s3_bucket_name: pulumi.Input[str],
             engine: pulumi.Input[str],
             engine_version: pulumi.Input[str],
             database_installation_files_s3_prefix: Optional[pulumi.Input[str]] = None,
             description: Optional[pulumi.Input[str]] = None,
             kms_key_id: Optional[pulumi.Input[str]] = None,
             manifest: Optional[pulumi.Input[str]] = None,
             status: Optional[pulumi.Input['CustomDbEngineVersionStatus']] = None,
             tags: Optional[pulumi.Input[Sequence[pulumi.Input['CustomDbEngineVersionTagArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("database_installation_files_s3_bucket_name", database_installation_files_s3_bucket_name)
        _setter("engine", engine)
        _setter("engine_version", engine_version)
        if database_installation_files_s3_prefix is not None:
            _setter("database_installation_files_s3_prefix", database_installation_files_s3_prefix)
        if description is not None:
            _setter("description", description)
        if kms_key_id is not None:
            _setter("kms_key_id", kms_key_id)
        if manifest is not None:
            _setter("manifest", manifest)
        if status is not None:
            _setter("status", status)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter(name="databaseInstallationFilesS3BucketName")
    def database_installation_files_s3_bucket_name(self) -> pulumi.Input[str]:
        """
        The name of an Amazon S3 bucket that contains database installation files for your CEV. For example, a valid bucket name is `my-custom-installation-files`.
        """
        return pulumi.get(self, "database_installation_files_s3_bucket_name")

    @database_installation_files_s3_bucket_name.setter
    def database_installation_files_s3_bucket_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "database_installation_files_s3_bucket_name", value)

    @property
    @pulumi.getter
    def engine(self) -> pulumi.Input[str]:
        """
        The database engine to use for your custom engine version (CEV). The only supported value is `custom-oracle-ee`.
        """
        return pulumi.get(self, "engine")

    @engine.setter
    def engine(self, value: pulumi.Input[str]):
        pulumi.set(self, "engine", value)

    @property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> pulumi.Input[str]:
        """
        The name of your CEV. The name format is 19.customized_string . For example, a valid name is 19.my_cev1. This setting is required for RDS Custom for Oracle, but optional for Amazon RDS. The combination of Engine and EngineVersion is unique per customer per Region.
        """
        return pulumi.get(self, "engine_version")

    @engine_version.setter
    def engine_version(self, value: pulumi.Input[str]):
        pulumi.set(self, "engine_version", value)

    @property
    @pulumi.getter(name="databaseInstallationFilesS3Prefix")
    def database_installation_files_s3_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        The Amazon S3 directory that contains the database installation files for your CEV. For example, a valid bucket name is `123456789012/cev1`. If this setting isn't specified, no prefix is assumed.
        """
        return pulumi.get(self, "database_installation_files_s3_prefix")

    @database_installation_files_s3_prefix.setter
    def database_installation_files_s3_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "database_installation_files_s3_prefix", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        An optional description of your CEV.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[str]]:
        """
        The AWS KMS key identifier for an encrypted CEV. A symmetric KMS key is required for RDS Custom, but optional for Amazon RDS.
        """
        return pulumi.get(self, "kms_key_id")

    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_key_id", value)

    @property
    @pulumi.getter
    def manifest(self) -> Optional[pulumi.Input[str]]:
        """
        The CEV manifest, which is a JSON document that describes the installation .zip files stored in Amazon S3. Specify the name/value pairs in a file or a quoted string. RDS Custom applies the patches in the order in which they are listed.
        """
        return pulumi.get(self, "manifest")

    @manifest.setter
    def manifest(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "manifest", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input['CustomDbEngineVersionStatus']]:
        """
        The availability status to be assigned to the CEV.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input['CustomDbEngineVersionStatus']]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CustomDbEngineVersionTagArgs']]]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CustomDbEngineVersionTagArgs']]]]):
        pulumi.set(self, "tags", value)


class CustomDbEngineVersion(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 database_installation_files_s3_bucket_name: Optional[pulumi.Input[str]] = None,
                 database_installation_files_s3_prefix: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 engine: Optional[pulumi.Input[str]] = None,
                 engine_version: Optional[pulumi.Input[str]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 manifest: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input['CustomDbEngineVersionStatus']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CustomDbEngineVersionTagArgs']]]]] = None,
                 __props__=None):
        """
        The AWS::RDS::CustomDBEngineVersion resource creates an Amazon RDS custom DB engine version.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] database_installation_files_s3_bucket_name: The name of an Amazon S3 bucket that contains database installation files for your CEV. For example, a valid bucket name is `my-custom-installation-files`.
        :param pulumi.Input[str] database_installation_files_s3_prefix: The Amazon S3 directory that contains the database installation files for your CEV. For example, a valid bucket name is `123456789012/cev1`. If this setting isn't specified, no prefix is assumed.
        :param pulumi.Input[str] description: An optional description of your CEV.
        :param pulumi.Input[str] engine: The database engine to use for your custom engine version (CEV). The only supported value is `custom-oracle-ee`.
        :param pulumi.Input[str] engine_version: The name of your CEV. The name format is 19.customized_string . For example, a valid name is 19.my_cev1. This setting is required for RDS Custom for Oracle, but optional for Amazon RDS. The combination of Engine and EngineVersion is unique per customer per Region.
        :param pulumi.Input[str] kms_key_id: The AWS KMS key identifier for an encrypted CEV. A symmetric KMS key is required for RDS Custom, but optional for Amazon RDS.
        :param pulumi.Input[str] manifest: The CEV manifest, which is a JSON document that describes the installation .zip files stored in Amazon S3. Specify the name/value pairs in a file or a quoted string. RDS Custom applies the patches in the order in which they are listed.
        :param pulumi.Input['CustomDbEngineVersionStatus'] status: The availability status to be assigned to the CEV.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CustomDbEngineVersionTagArgs']]]] tags: An array of key-value pairs to apply to this resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CustomDbEngineVersionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The AWS::RDS::CustomDBEngineVersion resource creates an Amazon RDS custom DB engine version.

        :param str resource_name: The name of the resource.
        :param CustomDbEngineVersionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CustomDbEngineVersionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            CustomDbEngineVersionArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 database_installation_files_s3_bucket_name: Optional[pulumi.Input[str]] = None,
                 database_installation_files_s3_prefix: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 engine: Optional[pulumi.Input[str]] = None,
                 engine_version: Optional[pulumi.Input[str]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 manifest: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input['CustomDbEngineVersionStatus']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CustomDbEngineVersionTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CustomDbEngineVersionArgs.__new__(CustomDbEngineVersionArgs)

            if database_installation_files_s3_bucket_name is None and not opts.urn:
                raise TypeError("Missing required property 'database_installation_files_s3_bucket_name'")
            __props__.__dict__["database_installation_files_s3_bucket_name"] = database_installation_files_s3_bucket_name
            __props__.__dict__["database_installation_files_s3_prefix"] = database_installation_files_s3_prefix
            __props__.__dict__["description"] = description
            if engine is None and not opts.urn:
                raise TypeError("Missing required property 'engine'")
            __props__.__dict__["engine"] = engine
            if engine_version is None and not opts.urn:
                raise TypeError("Missing required property 'engine_version'")
            __props__.__dict__["engine_version"] = engine_version
            __props__.__dict__["kms_key_id"] = kms_key_id
            __props__.__dict__["manifest"] = manifest
            __props__.__dict__["status"] = status
            __props__.__dict__["tags"] = tags
            __props__.__dict__["db_engine_version_arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["database_installation_files_s3_bucket_name", "database_installation_files_s3_prefix", "engine", "engine_version", "kms_key_id", "manifest"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(CustomDbEngineVersion, __self__).__init__(
            'aws-native:rds:CustomDbEngineVersion',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'CustomDbEngineVersion':
        """
        Get an existing CustomDbEngineVersion resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CustomDbEngineVersionArgs.__new__(CustomDbEngineVersionArgs)

        __props__.__dict__["database_installation_files_s3_bucket_name"] = None
        __props__.__dict__["database_installation_files_s3_prefix"] = None
        __props__.__dict__["db_engine_version_arn"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["engine"] = None
        __props__.__dict__["engine_version"] = None
        __props__.__dict__["kms_key_id"] = None
        __props__.__dict__["manifest"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["tags"] = None
        return CustomDbEngineVersion(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="databaseInstallationFilesS3BucketName")
    def database_installation_files_s3_bucket_name(self) -> pulumi.Output[str]:
        """
        The name of an Amazon S3 bucket that contains database installation files for your CEV. For example, a valid bucket name is `my-custom-installation-files`.
        """
        return pulumi.get(self, "database_installation_files_s3_bucket_name")

    @property
    @pulumi.getter(name="databaseInstallationFilesS3Prefix")
    def database_installation_files_s3_prefix(self) -> pulumi.Output[Optional[str]]:
        """
        The Amazon S3 directory that contains the database installation files for your CEV. For example, a valid bucket name is `123456789012/cev1`. If this setting isn't specified, no prefix is assumed.
        """
        return pulumi.get(self, "database_installation_files_s3_prefix")

    @property
    @pulumi.getter(name="dbEngineVersionArn")
    def db_engine_version_arn(self) -> pulumi.Output[str]:
        """
        The ARN of the custom engine version.
        """
        return pulumi.get(self, "db_engine_version_arn")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        An optional description of your CEV.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def engine(self) -> pulumi.Output[str]:
        """
        The database engine to use for your custom engine version (CEV). The only supported value is `custom-oracle-ee`.
        """
        return pulumi.get(self, "engine")

    @property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> pulumi.Output[str]:
        """
        The name of your CEV. The name format is 19.customized_string . For example, a valid name is 19.my_cev1. This setting is required for RDS Custom for Oracle, but optional for Amazon RDS. The combination of Engine and EngineVersion is unique per customer per Region.
        """
        return pulumi.get(self, "engine_version")

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[Optional[str]]:
        """
        The AWS KMS key identifier for an encrypted CEV. A symmetric KMS key is required for RDS Custom, but optional for Amazon RDS.
        """
        return pulumi.get(self, "kms_key_id")

    @property
    @pulumi.getter
    def manifest(self) -> pulumi.Output[Optional[str]]:
        """
        The CEV manifest, which is a JSON document that describes the installation .zip files stored in Amazon S3. Specify the name/value pairs in a file or a quoted string. RDS Custom applies the patches in the order in which they are listed.
        """
        return pulumi.get(self, "manifest")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional['CustomDbEngineVersionStatus']]:
        """
        The availability status to be assigned to the CEV.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.CustomDbEngineVersionTag']]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

