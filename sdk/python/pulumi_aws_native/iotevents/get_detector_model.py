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

__all__ = [
    'GetDetectorModelResult',
    'AwaitableGetDetectorModelResult',
    'get_detector_model',
    'get_detector_model_output',
]

@pulumi.output_type
class GetDetectorModelResult:
    def __init__(__self__, detector_model_definition=None, detector_model_description=None, evaluation_method=None, role_arn=None, tags=None):
        if detector_model_definition and not isinstance(detector_model_definition, dict):
            raise TypeError("Expected argument 'detector_model_definition' to be a dict")
        pulumi.set(__self__, "detector_model_definition", detector_model_definition)
        if detector_model_description and not isinstance(detector_model_description, str):
            raise TypeError("Expected argument 'detector_model_description' to be a str")
        pulumi.set(__self__, "detector_model_description", detector_model_description)
        if evaluation_method and not isinstance(evaluation_method, str):
            raise TypeError("Expected argument 'evaluation_method' to be a str")
        pulumi.set(__self__, "evaluation_method", evaluation_method)
        if role_arn and not isinstance(role_arn, str):
            raise TypeError("Expected argument 'role_arn' to be a str")
        pulumi.set(__self__, "role_arn", role_arn)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="detectorModelDefinition")
    def detector_model_definition(self) -> Optional['outputs.DetectorModelDefinition']:
        return pulumi.get(self, "detector_model_definition")

    @property
    @pulumi.getter(name="detectorModelDescription")
    def detector_model_description(self) -> Optional[str]:
        """
        A brief description of the detector model.
        """
        return pulumi.get(self, "detector_model_description")

    @property
    @pulumi.getter(name="evaluationMethod")
    def evaluation_method(self) -> Optional['DetectorModelEvaluationMethod']:
        """
        Information about the order in which events are evaluated and how actions are executed.
        """
        return pulumi.get(self, "evaluation_method")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[str]:
        """
        The ARN of the role that grants permission to AWS IoT Events to perform its operations.
        """
        return pulumi.get(self, "role_arn")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.DetectorModelTag']]:
        """
        An array of key-value pairs to apply to this resource.

        For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
        """
        return pulumi.get(self, "tags")


class AwaitableGetDetectorModelResult(GetDetectorModelResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDetectorModelResult(
            detector_model_definition=self.detector_model_definition,
            detector_model_description=self.detector_model_description,
            evaluation_method=self.evaluation_method,
            role_arn=self.role_arn,
            tags=self.tags)


def get_detector_model(detector_model_name: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDetectorModelResult:
    """
    The AWS::IoTEvents::DetectorModel resource creates a detector model. You create a *detector model* (a model of your equipment or process) using *states*. For each state, you define conditional (Boolean) logic that evaluates the incoming inputs to detect significant events. When an event is detected, it can change the state or trigger custom-built or predefined actions using other AWS services. You can define additional events that trigger actions when entering or exiting a state and, optionally, when a condition is met. For more information, see [How to Use AWS IoT Events](https://docs.aws.amazon.com/iotevents/latest/developerguide/how-to-use-iotevents.html) in the *AWS IoT Events Developer Guide*.


    :param str detector_model_name: The name of the detector model.
    """
    __args__ = dict()
    __args__['detectorModelName'] = detector_model_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:iotevents:getDetectorModel', __args__, opts=opts, typ=GetDetectorModelResult).value

    return AwaitableGetDetectorModelResult(
        detector_model_definition=pulumi.get(__ret__, 'detector_model_definition'),
        detector_model_description=pulumi.get(__ret__, 'detector_model_description'),
        evaluation_method=pulumi.get(__ret__, 'evaluation_method'),
        role_arn=pulumi.get(__ret__, 'role_arn'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_detector_model)
def get_detector_model_output(detector_model_name: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDetectorModelResult]:
    """
    The AWS::IoTEvents::DetectorModel resource creates a detector model. You create a *detector model* (a model of your equipment or process) using *states*. For each state, you define conditional (Boolean) logic that evaluates the incoming inputs to detect significant events. When an event is detected, it can change the state or trigger custom-built or predefined actions using other AWS services. You can define additional events that trigger actions when entering or exiting a state and, optionally, when a condition is met. For more information, see [How to Use AWS IoT Events](https://docs.aws.amazon.com/iotevents/latest/developerguide/how-to-use-iotevents.html) in the *AWS IoT Events Developer Guide*.


    :param str detector_model_name: The name of the detector model.
    """
    ...
