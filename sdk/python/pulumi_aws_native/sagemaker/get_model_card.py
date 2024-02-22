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
from .. import outputs as _root_outputs
from ._enums import *

__all__ = [
    'GetModelCardResult',
    'AwaitableGetModelCardResult',
    'get_model_card',
    'get_model_card_output',
]

@pulumi.output_type
class GetModelCardResult:
    def __init__(__self__, content=None, created_by=None, creation_time=None, last_modified_by=None, last_modified_time=None, model_card_arn=None, model_card_processing_status=None, model_card_status=None, model_card_version=None, tags=None):
        if content and not isinstance(content, dict):
            raise TypeError("Expected argument 'content' to be a dict")
        pulumi.set(__self__, "content", content)
        if created_by and not isinstance(created_by, dict):
            raise TypeError("Expected argument 'created_by' to be a dict")
        pulumi.set(__self__, "created_by", created_by)
        if creation_time and not isinstance(creation_time, str):
            raise TypeError("Expected argument 'creation_time' to be a str")
        pulumi.set(__self__, "creation_time", creation_time)
        if last_modified_by and not isinstance(last_modified_by, dict):
            raise TypeError("Expected argument 'last_modified_by' to be a dict")
        pulumi.set(__self__, "last_modified_by", last_modified_by)
        if last_modified_time and not isinstance(last_modified_time, str):
            raise TypeError("Expected argument 'last_modified_time' to be a str")
        pulumi.set(__self__, "last_modified_time", last_modified_time)
        if model_card_arn and not isinstance(model_card_arn, str):
            raise TypeError("Expected argument 'model_card_arn' to be a str")
        pulumi.set(__self__, "model_card_arn", model_card_arn)
        if model_card_processing_status and not isinstance(model_card_processing_status, str):
            raise TypeError("Expected argument 'model_card_processing_status' to be a str")
        pulumi.set(__self__, "model_card_processing_status", model_card_processing_status)
        if model_card_status and not isinstance(model_card_status, str):
            raise TypeError("Expected argument 'model_card_status' to be a str")
        pulumi.set(__self__, "model_card_status", model_card_status)
        if model_card_version and not isinstance(model_card_version, int):
            raise TypeError("Expected argument 'model_card_version' to be a int")
        pulumi.set(__self__, "model_card_version", model_card_version)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def content(self) -> Optional['outputs.ModelCardContent']:
        return pulumi.get(self, "content")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional['outputs.ModelCardUserContext']:
        """
        Information about the user who created or modified an experiment, trial, trial component, lineage group, project, or model card.
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[str]:
        """
        The date and time the model card was created.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional['outputs.ModelCardUserContext']:
        """
        Information about the user who created or modified an experiment, trial, trial component, lineage group, project, or model card.
        """
        return pulumi.get(self, "last_modified_by")

    @property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> Optional[str]:
        """
        The date and time the model card was last modified.
        """
        return pulumi.get(self, "last_modified_time")

    @property
    @pulumi.getter(name="modelCardArn")
    def model_card_arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the successfully created model card.
        """
        return pulumi.get(self, "model_card_arn")

    @property
    @pulumi.getter(name="modelCardProcessingStatus")
    def model_card_processing_status(self) -> Optional['ModelCardProcessingStatus']:
        """
        The processing status of model card deletion. The ModelCardProcessingStatus updates throughout the different deletion steps.
        """
        return pulumi.get(self, "model_card_processing_status")

    @property
    @pulumi.getter(name="modelCardStatus")
    def model_card_status(self) -> Optional['ModelCardStatus']:
        """
        The approval status of the model card within your organization. Different organizations might have different criteria for model card review and approval.
        """
        return pulumi.get(self, "model_card_status")

    @property
    @pulumi.getter(name="modelCardVersion")
    def model_card_version(self) -> Optional[int]:
        """
        A version of the model card.
        """
        return pulumi.get(self, "model_card_version")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        Key-value pairs used to manage metadata for model cards.
        """
        return pulumi.get(self, "tags")


class AwaitableGetModelCardResult(GetModelCardResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetModelCardResult(
            content=self.content,
            created_by=self.created_by,
            creation_time=self.creation_time,
            last_modified_by=self.last_modified_by,
            last_modified_time=self.last_modified_time,
            model_card_arn=self.model_card_arn,
            model_card_processing_status=self.model_card_processing_status,
            model_card_status=self.model_card_status,
            model_card_version=self.model_card_version,
            tags=self.tags)


def get_model_card(model_card_name: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetModelCardResult:
    """
    Resource Type definition for AWS::SageMaker::ModelCard.


    :param str model_card_name: The unique name of the model card.
    """
    __args__ = dict()
    __args__['modelCardName'] = model_card_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:sagemaker:getModelCard', __args__, opts=opts, typ=GetModelCardResult).value

    return AwaitableGetModelCardResult(
        content=pulumi.get(__ret__, 'content'),
        created_by=pulumi.get(__ret__, 'created_by'),
        creation_time=pulumi.get(__ret__, 'creation_time'),
        last_modified_by=pulumi.get(__ret__, 'last_modified_by'),
        last_modified_time=pulumi.get(__ret__, 'last_modified_time'),
        model_card_arn=pulumi.get(__ret__, 'model_card_arn'),
        model_card_processing_status=pulumi.get(__ret__, 'model_card_processing_status'),
        model_card_status=pulumi.get(__ret__, 'model_card_status'),
        model_card_version=pulumi.get(__ret__, 'model_card_version'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_model_card)
def get_model_card_output(model_card_name: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetModelCardResult]:
    """
    Resource Type definition for AWS::SageMaker::ModelCard.


    :param str model_card_name: The unique name of the model card.
    """
    ...
