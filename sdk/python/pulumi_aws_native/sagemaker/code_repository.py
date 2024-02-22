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

__all__ = ['CodeRepositoryArgs', 'CodeRepository']

@pulumi.input_type
class CodeRepositoryArgs:
    def __init__(__self__, *,
                 git_config: pulumi.Input['CodeRepositoryGitConfigArgs'],
                 code_repository_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a CodeRepository resource.
        """
        pulumi.set(__self__, "git_config", git_config)
        if code_repository_name is not None:
            pulumi.set(__self__, "code_repository_name", code_repository_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="gitConfig")
    def git_config(self) -> pulumi.Input['CodeRepositoryGitConfigArgs']:
        return pulumi.get(self, "git_config")

    @git_config.setter
    def git_config(self, value: pulumi.Input['CodeRepositoryGitConfigArgs']):
        pulumi.set(self, "git_config", value)

    @property
    @pulumi.getter(name="codeRepositoryName")
    def code_repository_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "code_repository_name")

    @code_repository_name.setter
    def code_repository_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "code_repository_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)


warnings.warn("""CodeRepository is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class CodeRepository(pulumi.CustomResource):
    warnings.warn("""CodeRepository is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 code_repository_name: Optional[pulumi.Input[str]] = None,
                 git_config: Optional[pulumi.Input[pulumi.InputType['CodeRepositoryGitConfigArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::SageMaker::CodeRepository

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CodeRepositoryArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::SageMaker::CodeRepository

        :param str resource_name: The name of the resource.
        :param CodeRepositoryArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CodeRepositoryArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 code_repository_name: Optional[pulumi.Input[str]] = None,
                 git_config: Optional[pulumi.Input[pulumi.InputType['CodeRepositoryGitConfigArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        pulumi.log.warn("""CodeRepository is deprecated: CodeRepository is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CodeRepositoryArgs.__new__(CodeRepositoryArgs)

            __props__.__dict__["code_repository_name"] = code_repository_name
            if git_config is None and not opts.urn:
                raise TypeError("Missing required property 'git_config'")
            __props__.__dict__["git_config"] = git_config
            __props__.__dict__["tags"] = tags
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["code_repository_name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(CodeRepository, __self__).__init__(
            'aws-native:sagemaker:CodeRepository',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'CodeRepository':
        """
        Get an existing CodeRepository resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CodeRepositoryArgs.__new__(CodeRepositoryArgs)

        __props__.__dict__["code_repository_name"] = None
        __props__.__dict__["git_config"] = None
        __props__.__dict__["tags"] = None
        return CodeRepository(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="codeRepositoryName")
    def code_repository_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "code_repository_name")

    @property
    @pulumi.getter(name="gitConfig")
    def git_config(self) -> pulumi.Output['outputs.CodeRepositoryGitConfig']:
        return pulumi.get(self, "git_config")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        return pulumi.get(self, "tags")

