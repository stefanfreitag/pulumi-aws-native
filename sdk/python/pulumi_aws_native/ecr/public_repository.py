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
from .. import _inputs as _root_inputs
from .. import outputs as _root_outputs
from ._inputs import *

__all__ = ['PublicRepositoryArgs', 'PublicRepository']

@pulumi.input_type
class PublicRepositoryArgs:
    def __init__(__self__, *,
                 repository_catalog_data: Optional[pulumi.Input['RepositoryCatalogDataPropertiesArgs']] = None,
                 repository_name: Optional[pulumi.Input[str]] = None,
                 repository_policy_text: Optional[Any] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a PublicRepository resource.
        :param pulumi.Input['RepositoryCatalogDataPropertiesArgs'] repository_catalog_data: The CatalogData property type specifies Catalog data for ECR Public Repository. For information about Catalog Data, see <link>
        :param pulumi.Input[str] repository_name: The name to use for the repository. The repository name may be specified on its own (such as nginx-web-app) or it can be prepended with a namespace to group the repository into a category (such as project-a/nginx-web-app). If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the repository name. For more information, see https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html.
        :param Any repository_policy_text: The JSON repository policy text to apply to the repository. For more information, see https://docs.aws.amazon.com/AmazonECR/latest/userguide/RepositoryPolicyExamples.html in the Amazon Elastic Container Registry User Guide. 
               
               Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::ECR::PublicRepository` for more information about the expected schema for this property.
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: An array of key-value pairs to apply to this resource.
        """
        if repository_catalog_data is not None:
            pulumi.set(__self__, "repository_catalog_data", repository_catalog_data)
        if repository_name is not None:
            pulumi.set(__self__, "repository_name", repository_name)
        if repository_policy_text is not None:
            pulumi.set(__self__, "repository_policy_text", repository_policy_text)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="repositoryCatalogData")
    def repository_catalog_data(self) -> Optional[pulumi.Input['RepositoryCatalogDataPropertiesArgs']]:
        """
        The CatalogData property type specifies Catalog data for ECR Public Repository. For information about Catalog Data, see <link>
        """
        return pulumi.get(self, "repository_catalog_data")

    @repository_catalog_data.setter
    def repository_catalog_data(self, value: Optional[pulumi.Input['RepositoryCatalogDataPropertiesArgs']]):
        pulumi.set(self, "repository_catalog_data", value)

    @property
    @pulumi.getter(name="repositoryName")
    def repository_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name to use for the repository. The repository name may be specified on its own (such as nginx-web-app) or it can be prepended with a namespace to group the repository into a category (such as project-a/nginx-web-app). If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the repository name. For more information, see https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html.
        """
        return pulumi.get(self, "repository_name")

    @repository_name.setter
    def repository_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "repository_name", value)

    @property
    @pulumi.getter(name="repositoryPolicyText")
    def repository_policy_text(self) -> Optional[Any]:
        """
        The JSON repository policy text to apply to the repository. For more information, see https://docs.aws.amazon.com/AmazonECR/latest/userguide/RepositoryPolicyExamples.html in the Amazon Elastic Container Registry User Guide. 

        Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::ECR::PublicRepository` for more information about the expected schema for this property.
        """
        return pulumi.get(self, "repository_policy_text")

    @repository_policy_text.setter
    def repository_policy_text(self, value: Optional[Any]):
        pulumi.set(self, "repository_policy_text", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)


warnings.warn("""PublicRepository is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class PublicRepository(pulumi.CustomResource):
    warnings.warn("""PublicRepository is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 repository_catalog_data: Optional[pulumi.Input[pulumi.InputType['RepositoryCatalogDataPropertiesArgs']]] = None,
                 repository_name: Optional[pulumi.Input[str]] = None,
                 repository_policy_text: Optional[Any] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        """
        The AWS::ECR::PublicRepository resource specifies an Amazon Elastic Container Public Registry (Amazon Public ECR) repository, where users can push and pull Docker images. For more information, see https://docs.aws.amazon.com/AmazonECR

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['RepositoryCatalogDataPropertiesArgs']] repository_catalog_data: The CatalogData property type specifies Catalog data for ECR Public Repository. For information about Catalog Data, see <link>
        :param pulumi.Input[str] repository_name: The name to use for the repository. The repository name may be specified on its own (such as nginx-web-app) or it can be prepended with a namespace to group the repository into a category (such as project-a/nginx-web-app). If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the repository name. For more information, see https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html.
        :param Any repository_policy_text: The JSON repository policy text to apply to the repository. For more information, see https://docs.aws.amazon.com/AmazonECR/latest/userguide/RepositoryPolicyExamples.html in the Amazon Elastic Container Registry User Guide. 
               
               Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::ECR::PublicRepository` for more information about the expected schema for this property.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]] tags: An array of key-value pairs to apply to this resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[PublicRepositoryArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The AWS::ECR::PublicRepository resource specifies an Amazon Elastic Container Public Registry (Amazon Public ECR) repository, where users can push and pull Docker images. For more information, see https://docs.aws.amazon.com/AmazonECR

        :param str resource_name: The name of the resource.
        :param PublicRepositoryArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PublicRepositoryArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 repository_catalog_data: Optional[pulumi.Input[pulumi.InputType['RepositoryCatalogDataPropertiesArgs']]] = None,
                 repository_name: Optional[pulumi.Input[str]] = None,
                 repository_policy_text: Optional[Any] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        pulumi.log.warn("""PublicRepository is deprecated: PublicRepository is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PublicRepositoryArgs.__new__(PublicRepositoryArgs)

            __props__.__dict__["repository_catalog_data"] = repository_catalog_data
            __props__.__dict__["repository_name"] = repository_name
            __props__.__dict__["repository_policy_text"] = repository_policy_text
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["repository_name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(PublicRepository, __self__).__init__(
            'aws-native:ecr:PublicRepository',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PublicRepository':
        """
        Get an existing PublicRepository resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PublicRepositoryArgs.__new__(PublicRepositoryArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["repository_catalog_data"] = None
        __props__.__dict__["repository_name"] = None
        __props__.__dict__["repository_policy_text"] = None
        __props__.__dict__["tags"] = None
        return PublicRepository(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="repositoryCatalogData")
    def repository_catalog_data(self) -> pulumi.Output[Optional['outputs.RepositoryCatalogDataProperties']]:
        """
        The CatalogData property type specifies Catalog data for ECR Public Repository. For information about Catalog Data, see <link>
        """
        return pulumi.get(self, "repository_catalog_data")

    @property
    @pulumi.getter(name="repositoryName")
    def repository_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name to use for the repository. The repository name may be specified on its own (such as nginx-web-app) or it can be prepended with a namespace to group the repository into a category (such as project-a/nginx-web-app). If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the repository name. For more information, see https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html.
        """
        return pulumi.get(self, "repository_name")

    @property
    @pulumi.getter(name="repositoryPolicyText")
    def repository_policy_text(self) -> pulumi.Output[Optional[Any]]:
        """
        The JSON repository policy text to apply to the repository. For more information, see https://docs.aws.amazon.com/AmazonECR/latest/userguide/RepositoryPolicyExamples.html in the Amazon Elastic Container Registry User Guide. 

        Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::ECR::PublicRepository` for more information about the expected schema for this property.
        """
        return pulumi.get(self, "repository_policy_text")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

