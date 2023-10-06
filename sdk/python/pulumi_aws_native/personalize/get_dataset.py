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

__all__ = [
    'GetDatasetResult',
    'AwaitableGetDatasetResult',
    'get_dataset',
    'get_dataset_output',
]

@pulumi.output_type
class GetDatasetResult:
    def __init__(__self__, dataset_arn=None, dataset_import_job=None):
        if dataset_arn and not isinstance(dataset_arn, str):
            raise TypeError("Expected argument 'dataset_arn' to be a str")
        pulumi.set(__self__, "dataset_arn", dataset_arn)
        if dataset_import_job and not isinstance(dataset_import_job, dict):
            raise TypeError("Expected argument 'dataset_import_job' to be a dict")
        pulumi.set(__self__, "dataset_import_job", dataset_import_job)

    @property
    @pulumi.getter(name="datasetArn")
    def dataset_arn(self) -> Optional[str]:
        """
        The ARN of the dataset
        """
        return pulumi.get(self, "dataset_arn")

    @property
    @pulumi.getter(name="datasetImportJob")
    def dataset_import_job(self) -> Optional['outputs.DatasetImportJob']:
        return pulumi.get(self, "dataset_import_job")


class AwaitableGetDatasetResult(GetDatasetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDatasetResult(
            dataset_arn=self.dataset_arn,
            dataset_import_job=self.dataset_import_job)


def get_dataset(dataset_arn: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDatasetResult:
    """
    Resource schema for AWS::Personalize::Dataset.


    :param str dataset_arn: The ARN of the dataset
    """
    __args__ = dict()
    __args__['datasetArn'] = dataset_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:personalize:getDataset', __args__, opts=opts, typ=GetDatasetResult).value

    return AwaitableGetDatasetResult(
        dataset_arn=pulumi.get(__ret__, 'dataset_arn'),
        dataset_import_job=pulumi.get(__ret__, 'dataset_import_job'))


@_utilities.lift_output_func(get_dataset)
def get_dataset_output(dataset_arn: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDatasetResult]:
    """
    Resource schema for AWS::Personalize::Dataset.


    :param str dataset_arn: The ARN of the dataset
    """
    ...
