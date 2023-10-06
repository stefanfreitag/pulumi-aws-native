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
    'DataIntegrationFileConfigurationArgs',
    'DataIntegrationObjectConfigurationArgs',
    'DataIntegrationScheduleConfigArgs',
    'DataIntegrationTagArgs',
    'EventIntegrationEventFilterArgs',
    'EventIntegrationTagArgs',
]

@pulumi.input_type
class DataIntegrationFileConfigurationArgs:
    def __init__(__self__, *,
                 folders: pulumi.Input[Sequence[pulumi.Input[str]]],
                 filters: Optional[Any] = None):
        """
        The configuration for what files should be pulled from the source.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] folders: Identifiers for the source folders to pull all files from recursively.
        :param Any filters: Restrictions for what files should be pulled from the source.
        """
        DataIntegrationFileConfigurationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            folders=folders,
            filters=filters,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             folders: pulumi.Input[Sequence[pulumi.Input[str]]],
             filters: Optional[Any] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("folders", folders)
        if filters is not None:
            _setter("filters", filters)

    @property
    @pulumi.getter
    def folders(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        Identifiers for the source folders to pull all files from recursively.
        """
        return pulumi.get(self, "folders")

    @folders.setter
    def folders(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "folders", value)

    @property
    @pulumi.getter
    def filters(self) -> Optional[Any]:
        """
        Restrictions for what files should be pulled from the source.
        """
        return pulumi.get(self, "filters")

    @filters.setter
    def filters(self, value: Optional[Any]):
        pulumi.set(self, "filters", value)


@pulumi.input_type
class DataIntegrationObjectConfigurationArgs:
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


@pulumi.input_type
class DataIntegrationScheduleConfigArgs:
    def __init__(__self__, *,
                 schedule_expression: pulumi.Input[str],
                 first_execution_from: Optional[pulumi.Input[str]] = None,
                 object: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] schedule_expression: How often the data should be pulled from data source.
        :param pulumi.Input[str] first_execution_from: The start date for objects to import in the first flow run. Epoch or ISO timestamp format is supported.
        :param pulumi.Input[str] object: The name of the object to pull from the data source.
        """
        DataIntegrationScheduleConfigArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            schedule_expression=schedule_expression,
            first_execution_from=first_execution_from,
            object=object,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             schedule_expression: pulumi.Input[str],
             first_execution_from: Optional[pulumi.Input[str]] = None,
             object: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("schedule_expression", schedule_expression)
        if first_execution_from is not None:
            _setter("first_execution_from", first_execution_from)
        if object is not None:
            _setter("object", object)

    @property
    @pulumi.getter(name="scheduleExpression")
    def schedule_expression(self) -> pulumi.Input[str]:
        """
        How often the data should be pulled from data source.
        """
        return pulumi.get(self, "schedule_expression")

    @schedule_expression.setter
    def schedule_expression(self, value: pulumi.Input[str]):
        pulumi.set(self, "schedule_expression", value)

    @property
    @pulumi.getter(name="firstExecutionFrom")
    def first_execution_from(self) -> Optional[pulumi.Input[str]]:
        """
        The start date for objects to import in the first flow run. Epoch or ISO timestamp format is supported.
        """
        return pulumi.get(self, "first_execution_from")

    @first_execution_from.setter
    def first_execution_from(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "first_execution_from", value)

    @property
    @pulumi.getter
    def object(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the object to pull from the data source.
        """
        return pulumi.get(self, "object")

    @object.setter
    def object(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "object", value)


@pulumi.input_type
class DataIntegrationTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        A label for tagging DataIntegration resources
        :param pulumi.Input[str] key: A key to identify the tag.
        :param pulumi.Input[str] value: Corresponding tag value for the key.
        """
        DataIntegrationTagArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            key=key,
            value=value,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             key: pulumi.Input[str],
             value: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("key", key)
        _setter("value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        A key to identify the tag.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        Corresponding tag value for the key.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class EventIntegrationEventFilterArgs:
    def __init__(__self__, *,
                 source: pulumi.Input[str]):
        """
        :param pulumi.Input[str] source: The source of the events.
        """
        EventIntegrationEventFilterArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            source=source,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             source: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("source", source)

    @property
    @pulumi.getter
    def source(self) -> pulumi.Input[str]:
        """
        The source of the events.
        """
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: pulumi.Input[str]):
        pulumi.set(self, "source", value)


@pulumi.input_type
class EventIntegrationTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        :param pulumi.Input[str] key: A key to identify the tag.
        :param pulumi.Input[str] value: Corresponding tag value for the key.
        """
        EventIntegrationTagArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            key=key,
            value=value,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             key: pulumi.Input[str],
             value: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("key", key)
        _setter("value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        A key to identify the tag.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        Corresponding tag value for the key.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


