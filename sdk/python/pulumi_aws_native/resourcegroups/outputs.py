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
    'GroupConfigurationItem',
    'GroupConfigurationParameter',
    'GroupQuery',
    'GroupResourceQuery',
    'GroupTag',
    'GroupTagFilter',
]

@pulumi.output_type
class GroupConfigurationItem(dict):
    def __init__(__self__, *,
                 parameters: Optional[Sequence['outputs.GroupConfigurationParameter']] = None,
                 type: Optional[str] = None):
        GroupConfigurationItem._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            parameters=parameters,
            type=type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             parameters: Optional[Sequence['outputs.GroupConfigurationParameter']] = None,
             type: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if parameters is not None:
            _setter("parameters", parameters)
        if type is not None:
            _setter("type", type)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[Sequence['outputs.GroupConfigurationParameter']]:
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        return pulumi.get(self, "type")


@pulumi.output_type
class GroupConfigurationParameter(dict):
    def __init__(__self__, *,
                 name: Optional[str] = None,
                 values: Optional[Sequence[str]] = None):
        GroupConfigurationParameter._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            name=name,
            values=values,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             name: Optional[str] = None,
             values: Optional[Sequence[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if name is not None:
            _setter("name", name)
        if values is not None:
            _setter("values", values)

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def values(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "values")


@pulumi.output_type
class GroupQuery(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "resourceTypeFilters":
            suggest = "resource_type_filters"
        elif key == "stackIdentifier":
            suggest = "stack_identifier"
        elif key == "tagFilters":
            suggest = "tag_filters"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in GroupQuery. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        GroupQuery.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        GroupQuery.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 resource_type_filters: Optional[Sequence[str]] = None,
                 stack_identifier: Optional[str] = None,
                 tag_filters: Optional[Sequence['outputs.GroupTagFilter']] = None):
        GroupQuery._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            resource_type_filters=resource_type_filters,
            stack_identifier=stack_identifier,
            tag_filters=tag_filters,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             resource_type_filters: Optional[Sequence[str]] = None,
             stack_identifier: Optional[str] = None,
             tag_filters: Optional[Sequence['outputs.GroupTagFilter']] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if resource_type_filters is not None:
            _setter("resource_type_filters", resource_type_filters)
        if stack_identifier is not None:
            _setter("stack_identifier", stack_identifier)
        if tag_filters is not None:
            _setter("tag_filters", tag_filters)

    @property
    @pulumi.getter(name="resourceTypeFilters")
    def resource_type_filters(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "resource_type_filters")

    @property
    @pulumi.getter(name="stackIdentifier")
    def stack_identifier(self) -> Optional[str]:
        return pulumi.get(self, "stack_identifier")

    @property
    @pulumi.getter(name="tagFilters")
    def tag_filters(self) -> Optional[Sequence['outputs.GroupTagFilter']]:
        return pulumi.get(self, "tag_filters")


@pulumi.output_type
class GroupResourceQuery(dict):
    def __init__(__self__, *,
                 query: Optional['outputs.GroupQuery'] = None,
                 type: Optional['GroupResourceQueryType'] = None):
        GroupResourceQuery._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            query=query,
            type=type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             query: Optional['outputs.GroupQuery'] = None,
             type: Optional['GroupResourceQueryType'] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if query is not None:
            _setter("query", query)
        if type is not None:
            _setter("type", type)

    @property
    @pulumi.getter
    def query(self) -> Optional['outputs.GroupQuery']:
        return pulumi.get(self, "query")

    @property
    @pulumi.getter
    def type(self) -> Optional['GroupResourceQueryType']:
        return pulumi.get(self, "type")


@pulumi.output_type
class GroupTag(dict):
    def __init__(__self__, *,
                 key: Optional[str] = None,
                 value: Optional[str] = None):
        GroupTag._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            key=key,
            value=value,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             key: Optional[str] = None,
             value: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if key is not None:
            _setter("key", key)
        if value is not None:
            _setter("value", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[str]:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        return pulumi.get(self, "value")


@pulumi.output_type
class GroupTagFilter(dict):
    def __init__(__self__, *,
                 key: Optional[str] = None,
                 values: Optional[Sequence[str]] = None):
        GroupTagFilter._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            key=key,
            values=values,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             key: Optional[str] = None,
             values: Optional[Sequence[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if key is not None:
            _setter("key", key)
        if values is not None:
            _setter("values", values)

    @property
    @pulumi.getter
    def key(self) -> Optional[str]:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def values(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "values")


