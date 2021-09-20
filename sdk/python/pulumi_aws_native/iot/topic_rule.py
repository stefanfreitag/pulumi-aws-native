# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['TopicRuleArgs', 'TopicRule']

@pulumi.input_type
class TopicRuleArgs:
    def __init__(__self__, *,
                 topic_rule_payload: pulumi.Input['TopicRuleTopicRulePayloadArgs'],
                 rule_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['TopicRuleTagArgs']]]] = None):
        """
        The set of arguments for constructing a TopicRule resource.
        """
        pulumi.set(__self__, "topic_rule_payload", topic_rule_payload)
        if rule_name is not None:
            pulumi.set(__self__, "rule_name", rule_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="topicRulePayload")
    def topic_rule_payload(self) -> pulumi.Input['TopicRuleTopicRulePayloadArgs']:
        return pulumi.get(self, "topic_rule_payload")

    @topic_rule_payload.setter
    def topic_rule_payload(self, value: pulumi.Input['TopicRuleTopicRulePayloadArgs']):
        pulumi.set(self, "topic_rule_payload", value)

    @property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "rule_name")

    @rule_name.setter
    def rule_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rule_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TopicRuleTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TopicRuleTagArgs']]]]):
        pulumi.set(self, "tags", value)


class TopicRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 rule_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TopicRuleTagArgs']]]]] = None,
                 topic_rule_payload: Optional[pulumi.Input[pulumi.InputType['TopicRuleTopicRulePayloadArgs']]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::IoT::TopicRule

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TopicRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::IoT::TopicRule

        :param str resource_name: The name of the resource.
        :param TopicRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TopicRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 rule_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TopicRuleTagArgs']]]]] = None,
                 topic_rule_payload: Optional[pulumi.Input[pulumi.InputType['TopicRuleTopicRulePayloadArgs']]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TopicRuleArgs.__new__(TopicRuleArgs)

            __props__.__dict__["rule_name"] = rule_name
            __props__.__dict__["tags"] = tags
            if topic_rule_payload is None and not opts.urn:
                raise TypeError("Missing required property 'topic_rule_payload'")
            __props__.__dict__["topic_rule_payload"] = topic_rule_payload
            __props__.__dict__["arn"] = None
        super(TopicRule, __self__).__init__(
            'aws-native:iot:TopicRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'TopicRule':
        """
        Get an existing TopicRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = TopicRuleArgs.__new__(TopicRuleArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["rule_name"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["topic_rule_payload"] = None
        return TopicRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "rule_name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.TopicRuleTag']]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="topicRulePayload")
    def topic_rule_payload(self) -> pulumi.Output['outputs.TopicRuleTopicRulePayload']:
        return pulumi.get(self, "topic_rule_payload")

