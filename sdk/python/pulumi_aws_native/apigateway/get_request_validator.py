# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetRequestValidatorResult',
    'AwaitableGetRequestValidatorResult',
    'get_request_validator',
    'get_request_validator_output',
]

@pulumi.output_type
class GetRequestValidatorResult:
    def __init__(__self__, request_validator_id=None, validate_request_body=None, validate_request_parameters=None):
        if request_validator_id and not isinstance(request_validator_id, str):
            raise TypeError("Expected argument 'request_validator_id' to be a str")
        pulumi.set(__self__, "request_validator_id", request_validator_id)
        if validate_request_body and not isinstance(validate_request_body, bool):
            raise TypeError("Expected argument 'validate_request_body' to be a bool")
        pulumi.set(__self__, "validate_request_body", validate_request_body)
        if validate_request_parameters and not isinstance(validate_request_parameters, bool):
            raise TypeError("Expected argument 'validate_request_parameters' to be a bool")
        pulumi.set(__self__, "validate_request_parameters", validate_request_parameters)

    @property
    @pulumi.getter(name="requestValidatorId")
    def request_validator_id(self) -> Optional[str]:
        """
        ID of the request validator.
        """
        return pulumi.get(self, "request_validator_id")

    @property
    @pulumi.getter(name="validateRequestBody")
    def validate_request_body(self) -> Optional[bool]:
        """
        Indicates whether to validate the request body according to the configured schema for the targeted API and method. 
        """
        return pulumi.get(self, "validate_request_body")

    @property
    @pulumi.getter(name="validateRequestParameters")
    def validate_request_parameters(self) -> Optional[bool]:
        """
        Indicates whether to validate request parameters.
        """
        return pulumi.get(self, "validate_request_parameters")


class AwaitableGetRequestValidatorResult(GetRequestValidatorResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRequestValidatorResult(
            request_validator_id=self.request_validator_id,
            validate_request_body=self.validate_request_body,
            validate_request_parameters=self.validate_request_parameters)


def get_request_validator(request_validator_id: Optional[str] = None,
                          rest_api_id: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRequestValidatorResult:
    """
    Resource Type definition for AWS::ApiGateway::RequestValidator


    :param str request_validator_id: ID of the request validator.
    :param str rest_api_id: The identifier of the targeted API entity.
    """
    __args__ = dict()
    __args__['requestValidatorId'] = request_validator_id
    __args__['restApiId'] = rest_api_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:apigateway:getRequestValidator', __args__, opts=opts, typ=GetRequestValidatorResult).value

    return AwaitableGetRequestValidatorResult(
        request_validator_id=pulumi.get(__ret__, 'request_validator_id'),
        validate_request_body=pulumi.get(__ret__, 'validate_request_body'),
        validate_request_parameters=pulumi.get(__ret__, 'validate_request_parameters'))


@_utilities.lift_output_func(get_request_validator)
def get_request_validator_output(request_validator_id: Optional[pulumi.Input[str]] = None,
                                 rest_api_id: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRequestValidatorResult]:
    """
    Resource Type definition for AWS::ApiGateway::RequestValidator


    :param str request_validator_id: ID of the request validator.
    :param str rest_api_id: The identifier of the targeted API entity.
    """
    ...
