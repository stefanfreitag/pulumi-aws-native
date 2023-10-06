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
from ._inputs import *

__all__ = ['EventSubscriptionArgs', 'EventSubscription']

@pulumi.input_type
class EventSubscriptionArgs:
    def __init__(__self__, *,
                 subscription_name: pulumi.Input[str],
                 enabled: Optional[pulumi.Input[bool]] = None,
                 event_categories: Optional[pulumi.Input[Sequence[pulumi.Input['EventSubscriptionEventCategoriesItem']]]] = None,
                 severity: Optional[pulumi.Input['EventSubscriptionSeverity']] = None,
                 sns_topic_arn: Optional[pulumi.Input[str]] = None,
                 source_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 source_type: Optional[pulumi.Input['EventSubscriptionSourceType']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['EventSubscriptionTagArgs']]]] = None):
        """
        The set of arguments for constructing a EventSubscription resource.
        :param pulumi.Input[str] subscription_name: The name of the Amazon Redshift event notification subscription
        :param pulumi.Input[bool] enabled: A boolean value; set to true to activate the subscription, and set to false to create the subscription but not activate it.
        :param pulumi.Input[Sequence[pulumi.Input['EventSubscriptionEventCategoriesItem']]] event_categories: Specifies the Amazon Redshift event categories to be published by the event notification subscription.
        :param pulumi.Input['EventSubscriptionSeverity'] severity: Specifies the Amazon Redshift event severity to be published by the event notification subscription.
        :param pulumi.Input[str] sns_topic_arn: The Amazon Resource Name (ARN) of the Amazon SNS topic used to transmit the event notifications.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] source_ids: A list of one or more identifiers of Amazon Redshift source objects.
        :param pulumi.Input['EventSubscriptionSourceType'] source_type: The type of source that will be generating the events.
        :param pulumi.Input[Sequence[pulumi.Input['EventSubscriptionTagArgs']]] tags: An array of key-value pairs to apply to this resource.
        """
        EventSubscriptionArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            subscription_name=subscription_name,
            enabled=enabled,
            event_categories=event_categories,
            severity=severity,
            sns_topic_arn=sns_topic_arn,
            source_ids=source_ids,
            source_type=source_type,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             subscription_name: pulumi.Input[str],
             enabled: Optional[pulumi.Input[bool]] = None,
             event_categories: Optional[pulumi.Input[Sequence[pulumi.Input['EventSubscriptionEventCategoriesItem']]]] = None,
             severity: Optional[pulumi.Input['EventSubscriptionSeverity']] = None,
             sns_topic_arn: Optional[pulumi.Input[str]] = None,
             source_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             source_type: Optional[pulumi.Input['EventSubscriptionSourceType']] = None,
             tags: Optional[pulumi.Input[Sequence[pulumi.Input['EventSubscriptionTagArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("subscription_name", subscription_name)
        if enabled is not None:
            _setter("enabled", enabled)
        if event_categories is not None:
            _setter("event_categories", event_categories)
        if severity is not None:
            _setter("severity", severity)
        if sns_topic_arn is not None:
            _setter("sns_topic_arn", sns_topic_arn)
        if source_ids is not None:
            _setter("source_ids", source_ids)
        if source_type is not None:
            _setter("source_type", source_type)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter(name="subscriptionName")
    def subscription_name(self) -> pulumi.Input[str]:
        """
        The name of the Amazon Redshift event notification subscription
        """
        return pulumi.get(self, "subscription_name")

    @subscription_name.setter
    def subscription_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "subscription_name", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        A boolean value; set to true to activate the subscription, and set to false to create the subscription but not activate it.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="eventCategories")
    def event_categories(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['EventSubscriptionEventCategoriesItem']]]]:
        """
        Specifies the Amazon Redshift event categories to be published by the event notification subscription.
        """
        return pulumi.get(self, "event_categories")

    @event_categories.setter
    def event_categories(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['EventSubscriptionEventCategoriesItem']]]]):
        pulumi.set(self, "event_categories", value)

    @property
    @pulumi.getter
    def severity(self) -> Optional[pulumi.Input['EventSubscriptionSeverity']]:
        """
        Specifies the Amazon Redshift event severity to be published by the event notification subscription.
        """
        return pulumi.get(self, "severity")

    @severity.setter
    def severity(self, value: Optional[pulumi.Input['EventSubscriptionSeverity']]):
        pulumi.set(self, "severity", value)

    @property
    @pulumi.getter(name="snsTopicArn")
    def sns_topic_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The Amazon Resource Name (ARN) of the Amazon SNS topic used to transmit the event notifications.
        """
        return pulumi.get(self, "sns_topic_arn")

    @sns_topic_arn.setter
    def sns_topic_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sns_topic_arn", value)

    @property
    @pulumi.getter(name="sourceIds")
    def source_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of one or more identifiers of Amazon Redshift source objects.
        """
        return pulumi.get(self, "source_ids")

    @source_ids.setter
    def source_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "source_ids", value)

    @property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> Optional[pulumi.Input['EventSubscriptionSourceType']]:
        """
        The type of source that will be generating the events.
        """
        return pulumi.get(self, "source_type")

    @source_type.setter
    def source_type(self, value: Optional[pulumi.Input['EventSubscriptionSourceType']]):
        pulumi.set(self, "source_type", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['EventSubscriptionTagArgs']]]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['EventSubscriptionTagArgs']]]]):
        pulumi.set(self, "tags", value)


class EventSubscription(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 event_categories: Optional[pulumi.Input[Sequence[pulumi.Input['EventSubscriptionEventCategoriesItem']]]] = None,
                 severity: Optional[pulumi.Input['EventSubscriptionSeverity']] = None,
                 sns_topic_arn: Optional[pulumi.Input[str]] = None,
                 source_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 source_type: Optional[pulumi.Input['EventSubscriptionSourceType']] = None,
                 subscription_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EventSubscriptionTagArgs']]]]] = None,
                 __props__=None):
        """
        The `AWS::Redshift::EventSubscription` resource creates an Amazon Redshift Event Subscription.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enabled: A boolean value; set to true to activate the subscription, and set to false to create the subscription but not activate it.
        :param pulumi.Input[Sequence[pulumi.Input['EventSubscriptionEventCategoriesItem']]] event_categories: Specifies the Amazon Redshift event categories to be published by the event notification subscription.
        :param pulumi.Input['EventSubscriptionSeverity'] severity: Specifies the Amazon Redshift event severity to be published by the event notification subscription.
        :param pulumi.Input[str] sns_topic_arn: The Amazon Resource Name (ARN) of the Amazon SNS topic used to transmit the event notifications.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] source_ids: A list of one or more identifiers of Amazon Redshift source objects.
        :param pulumi.Input['EventSubscriptionSourceType'] source_type: The type of source that will be generating the events.
        :param pulumi.Input[str] subscription_name: The name of the Amazon Redshift event notification subscription
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EventSubscriptionTagArgs']]]] tags: An array of key-value pairs to apply to this resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EventSubscriptionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The `AWS::Redshift::EventSubscription` resource creates an Amazon Redshift Event Subscription.

        :param str resource_name: The name of the resource.
        :param EventSubscriptionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EventSubscriptionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            EventSubscriptionArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 event_categories: Optional[pulumi.Input[Sequence[pulumi.Input['EventSubscriptionEventCategoriesItem']]]] = None,
                 severity: Optional[pulumi.Input['EventSubscriptionSeverity']] = None,
                 sns_topic_arn: Optional[pulumi.Input[str]] = None,
                 source_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 source_type: Optional[pulumi.Input['EventSubscriptionSourceType']] = None,
                 subscription_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EventSubscriptionTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EventSubscriptionArgs.__new__(EventSubscriptionArgs)

            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["event_categories"] = event_categories
            __props__.__dict__["severity"] = severity
            __props__.__dict__["sns_topic_arn"] = sns_topic_arn
            __props__.__dict__["source_ids"] = source_ids
            __props__.__dict__["source_type"] = source_type
            if subscription_name is None and not opts.urn:
                raise TypeError("Missing required property 'subscription_name'")
            __props__.__dict__["subscription_name"] = subscription_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["cust_subscription_id"] = None
            __props__.__dict__["customer_aws_id"] = None
            __props__.__dict__["event_categories_list"] = None
            __props__.__dict__["source_ids_list"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["subscription_creation_time"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["subscription_name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(EventSubscription, __self__).__init__(
            'aws-native:redshift:EventSubscription',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'EventSubscription':
        """
        Get an existing EventSubscription resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = EventSubscriptionArgs.__new__(EventSubscriptionArgs)

        __props__.__dict__["cust_subscription_id"] = None
        __props__.__dict__["customer_aws_id"] = None
        __props__.__dict__["enabled"] = None
        __props__.__dict__["event_categories"] = None
        __props__.__dict__["event_categories_list"] = None
        __props__.__dict__["severity"] = None
        __props__.__dict__["sns_topic_arn"] = None
        __props__.__dict__["source_ids"] = None
        __props__.__dict__["source_ids_list"] = None
        __props__.__dict__["source_type"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["subscription_creation_time"] = None
        __props__.__dict__["subscription_name"] = None
        __props__.__dict__["tags"] = None
        return EventSubscription(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="custSubscriptionId")
    def cust_subscription_id(self) -> pulumi.Output[str]:
        """
        The name of the Amazon Redshift event notification subscription.
        """
        return pulumi.get(self, "cust_subscription_id")

    @property
    @pulumi.getter(name="customerAwsId")
    def customer_aws_id(self) -> pulumi.Output[str]:
        """
        The AWS account associated with the Amazon Redshift event notification subscription.
        """
        return pulumi.get(self, "customer_aws_id")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        A boolean value; set to true to activate the subscription, and set to false to create the subscription but not activate it.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="eventCategories")
    def event_categories(self) -> pulumi.Output[Optional[Sequence['EventSubscriptionEventCategoriesItem']]]:
        """
        Specifies the Amazon Redshift event categories to be published by the event notification subscription.
        """
        return pulumi.get(self, "event_categories")

    @property
    @pulumi.getter(name="eventCategoriesList")
    def event_categories_list(self) -> pulumi.Output[Sequence[str]]:
        """
        The list of Amazon Redshift event categories specified in the event notification subscription.
        """
        return pulumi.get(self, "event_categories_list")

    @property
    @pulumi.getter
    def severity(self) -> pulumi.Output[Optional['EventSubscriptionSeverity']]:
        """
        Specifies the Amazon Redshift event severity to be published by the event notification subscription.
        """
        return pulumi.get(self, "severity")

    @property
    @pulumi.getter(name="snsTopicArn")
    def sns_topic_arn(self) -> pulumi.Output[Optional[str]]:
        """
        The Amazon Resource Name (ARN) of the Amazon SNS topic used to transmit the event notifications.
        """
        return pulumi.get(self, "sns_topic_arn")

    @property
    @pulumi.getter(name="sourceIds")
    def source_ids(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of one or more identifiers of Amazon Redshift source objects.
        """
        return pulumi.get(self, "source_ids")

    @property
    @pulumi.getter(name="sourceIdsList")
    def source_ids_list(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of the sources that publish events to the Amazon Redshift event notification subscription.
        """
        return pulumi.get(self, "source_ids_list")

    @property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> pulumi.Output[Optional['EventSubscriptionSourceType']]:
        """
        The type of source that will be generating the events.
        """
        return pulumi.get(self, "source_type")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output['EventSubscriptionStatus']:
        """
        The status of the Amazon Redshift event notification subscription.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="subscriptionCreationTime")
    def subscription_creation_time(self) -> pulumi.Output[str]:
        """
        The date and time the Amazon Redshift event notification subscription was created.
        """
        return pulumi.get(self, "subscription_creation_time")

    @property
    @pulumi.getter(name="subscriptionName")
    def subscription_name(self) -> pulumi.Output[str]:
        """
        The name of the Amazon Redshift event notification subscription
        """
        return pulumi.get(self, "subscription_name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.EventSubscriptionTag']]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

