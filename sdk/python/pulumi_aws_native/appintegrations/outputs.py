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
    'DataIntegrationFileConfiguration',
    'DataIntegrationObjectConfiguration',
    'DataIntegrationScheduleConfig',
    'DataIntegrationTag',
    'EventIntegrationEventFilter',
    'EventIntegrationTag',
]

@pulumi.output_type
class DataIntegrationFileConfiguration(dict):
    """
    The configuration for what files should be pulled from the source.
    """
    def __init__(__self__, *,
                 folders: Sequence[str],
                 filters: Optional[Any] = None):
        """
        The configuration for what files should be pulled from the source.
        :param Sequence[str] folders: Identifiers for the source folders to pull all files from recursively.
        :param Any filters: Restrictions for what files should be pulled from the source.
        """
        DataIntegrationFileConfiguration._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            folders=folders,
            filters=filters,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             folders: Sequence[str],
             filters: Optional[Any] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("folders", folders)
        if filters is not None:
            _setter("filters", filters)

    @property
    @pulumi.getter
    def folders(self) -> Sequence[str]:
        """
        Identifiers for the source folders to pull all files from recursively.
        """
        return pulumi.get(self, "folders")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Any]:
        """
        Restrictions for what files should be pulled from the source.
        """
        return pulumi.get(self, "filters")


@pulumi.output_type
class DataIntegrationObjectConfiguration(dict):
    """
    The configuration for what data should be pulled from the source.
    """
    def __init__(__self__):
        """
        The configuration for what data should be pulled from the source.
        """
        pass
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             opts: Optional[pulumi.ResourceOptions]=None):
        pass


@pulumi.output_type
class DataIntegrationScheduleConfig(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "scheduleExpression":
            suggest = "schedule_expression"
        elif key == "firstExecutionFrom":
            suggest = "first_execution_from"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in DataIntegrationScheduleConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        DataIntegrationScheduleConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        DataIntegrationScheduleConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 schedule_expression: str,
                 first_execution_from: Optional[str] = None,
                 object: Optional[str] = None):
        """
        :param str schedule_expression: How often the data should be pulled from data source.
        :param str first_execution_from: The start date for objects to import in the first flow run. Epoch or ISO timestamp format is supported.
        :param str object: The name of the object to pull from the data source.
        """
        DataIntegrationScheduleConfig._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            schedule_expression=schedule_expression,
            first_execution_from=first_execution_from,
            object=object,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             schedule_expression: str,
             first_execution_from: Optional[str] = None,
             object: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("schedule_expression", schedule_expression)
        if first_execution_from is not None:
            _setter("first_execution_from", first_execution_from)
        if object is not None:
            _setter("object", object)

    @property
    @pulumi.getter(name="scheduleExpression")
    def schedule_expression(self) -> str:
        """
        How often the data should be pulled from data source.
        """
        return pulumi.get(self, "schedule_expression")

    @property
    @pulumi.getter(name="firstExecutionFrom")
    def first_execution_from(self) -> Optional[str]:
        """
        The start date for objects to import in the first flow run. Epoch or ISO timestamp format is supported.
        """
        return pulumi.get(self, "first_execution_from")

    @property
    @pulumi.getter
    def object(self) -> Optional[str]:
        """
        The name of the object to pull from the data source.
        """
        return pulumi.get(self, "object")


@pulumi.output_type
class DataIntegrationTag(dict):
    """
    A label for tagging DataIntegration resources
    """
    def __init__(__self__, *,
                 key: str,
                 value: str):
        """
        A label for tagging DataIntegration resources
        :param str key: A key to identify the tag.
        :param str value: Corresponding tag value for the key.
        """
        DataIntegrationTag._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            key=key,
            value=value,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             key: str,
             value: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("key", key)
        _setter("value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        A key to identify the tag.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        Corresponding tag value for the key.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class EventIntegrationEventFilter(dict):
    def __init__(__self__, *,
                 source: str):
        """
        :param str source: The source of the events.
        """
        EventIntegrationEventFilter._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            source=source,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             source: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("source", source)

    @property
    @pulumi.getter
    def source(self) -> str:
        """
        The source of the events.
        """
        return pulumi.get(self, "source")


@pulumi.output_type
class EventIntegrationTag(dict):
    def __init__(__self__, *,
                 key: str,
                 value: str):
        """
        :param str key: A key to identify the tag.
        :param str value: Corresponding tag value for the key.
        """
        EventIntegrationTag._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            key=key,
            value=value,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             key: str,
             value: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("key", key)
        _setter("value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        A key to identify the tag.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        Corresponding tag value for the key.
        """
        return pulumi.get(self, "value")


