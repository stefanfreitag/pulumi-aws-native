# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetModelResult',
    'AwaitableGetModelResult',
    'get_model',
    'get_model_output',
]

@pulumi.output_type
class GetModelResult:
    def __init__(__self__, content_type=None, description=None, model_id=None, name=None, schema=None):
        if content_type and not isinstance(content_type, str):
            raise TypeError("Expected argument 'content_type' to be a str")
        pulumi.set(__self__, "content_type", content_type)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if model_id and not isinstance(model_id, str):
            raise TypeError("Expected argument 'model_id' to be a str")
        pulumi.set(__self__, "model_id", model_id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if schema and not isinstance(schema, dict):
            raise TypeError("Expected argument 'schema' to be a dict")
        pulumi.set(__self__, "schema", schema)

    @property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[str]:
        """
        The content-type for the model, for example, "application/json".
        """
        return pulumi.get(self, "content_type")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of the model.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="modelId")
    def model_id(self) -> Optional[str]:
        return pulumi.get(self, "model_id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the model.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def schema(self) -> Optional[Any]:
        """
        The schema for the model. For application/json models, this should be JSON schema draft 4 model.
        """
        return pulumi.get(self, "schema")


class AwaitableGetModelResult(GetModelResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetModelResult(
            content_type=self.content_type,
            description=self.description,
            model_id=self.model_id,
            name=self.name,
            schema=self.schema)


def get_model(api_id: Optional[str] = None,
              model_id: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetModelResult:
    """
    The ``AWS::ApiGatewayV2::Model`` resource updates data model for a WebSocket API. For more information, see [Model Selection Expressions](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-model-selection-expressions) in the *API Gateway Developer Guide*.


    :param str api_id: The API identifier.
    """
    __args__ = dict()
    __args__['apiId'] = api_id
    __args__['modelId'] = model_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:apigatewayv2:getModel', __args__, opts=opts, typ=GetModelResult).value

    return AwaitableGetModelResult(
        content_type=pulumi.get(__ret__, 'content_type'),
        description=pulumi.get(__ret__, 'description'),
        model_id=pulumi.get(__ret__, 'model_id'),
        name=pulumi.get(__ret__, 'name'),
        schema=pulumi.get(__ret__, 'schema'))


@_utilities.lift_output_func(get_model)
def get_model_output(api_id: Optional[pulumi.Input[str]] = None,
                     model_id: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetModelResult]:
    """
    The ``AWS::ApiGatewayV2::Model`` resource updates data model for a WebSocket API. For more information, see [Model Selection Expressions](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-model-selection-expressions) in the *API Gateway Developer Guide*.


    :param str api_id: The API identifier.
    """
    ...
