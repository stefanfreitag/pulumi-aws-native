# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = [
    'IndexTagMap',
    'ViewFilters',
    'ViewIncludedProperty',
    'ViewTagMap',
]

@pulumi.output_type
class IndexTagMap(dict):
    def __init__(__self__):
        pass
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             opts: Optional[pulumi.ResourceOptions]=None):
        pass


@pulumi.output_type
class ViewFilters(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "filterString":
            suggest = "filter_string"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ViewFilters. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ViewFilters.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ViewFilters.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 filter_string: str):
        ViewFilters._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            filter_string=filter_string,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             filter_string: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("filter_string", filter_string)

    @property
    @pulumi.getter(name="filterString")
    def filter_string(self) -> str:
        return pulumi.get(self, "filter_string")


@pulumi.output_type
class ViewIncludedProperty(dict):
    def __init__(__self__, *,
                 name: str):
        ViewIncludedProperty._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            name=name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             name: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("name", name)

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")


@pulumi.output_type
class ViewTagMap(dict):
    def __init__(__self__):
        pass
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             opts: Optional[pulumi.ResourceOptions]=None):
        pass


