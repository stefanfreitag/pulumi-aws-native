// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package iot

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::IoT::TopicRuleDestination
type TopicRuleDestination struct {
	pulumi.CustomResourceState

	// Amazon Resource Name (ARN).
	Arn pulumi.StringOutput `pulumi:"arn"`
	// HTTP URL destination properties.
	HttpUrlProperties TopicRuleDestinationHttpUrlDestinationSummaryPtrOutput `pulumi:"httpUrlProperties"`
	// The status of the TopicRuleDestination.
	Status TopicRuleDestinationTopicRuleDestinationStatusPtrOutput `pulumi:"status"`
	// The reasoning for the current status of the TopicRuleDestination.
	StatusReason pulumi.StringOutput `pulumi:"statusReason"`
	// VPC destination properties.
	VpcProperties TopicRuleDestinationVpcDestinationPropertiesPtrOutput `pulumi:"vpcProperties"`
}

// NewTopicRuleDestination registers a new resource with the given unique name, arguments, and options.
func NewTopicRuleDestination(ctx *pulumi.Context,
	name string, args *TopicRuleDestinationArgs, opts ...pulumi.ResourceOption) (*TopicRuleDestination, error) {
	if args == nil {
		args = &TopicRuleDestinationArgs{}
	}

	var resource TopicRuleDestination
	err := ctx.RegisterResource("aws-native:iot:TopicRuleDestination", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetTopicRuleDestination gets an existing TopicRuleDestination resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetTopicRuleDestination(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *TopicRuleDestinationState, opts ...pulumi.ResourceOption) (*TopicRuleDestination, error) {
	var resource TopicRuleDestination
	err := ctx.ReadResource("aws-native:iot:TopicRuleDestination", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering TopicRuleDestination resources.
type topicRuleDestinationState struct {
}

type TopicRuleDestinationState struct {
}

func (TopicRuleDestinationState) ElementType() reflect.Type {
	return reflect.TypeOf((*topicRuleDestinationState)(nil)).Elem()
}

type topicRuleDestinationArgs struct {
	// HTTP URL destination properties.
	HttpUrlProperties *TopicRuleDestinationHttpUrlDestinationSummary `pulumi:"httpUrlProperties"`
	// The status of the TopicRuleDestination.
	Status *TopicRuleDestinationTopicRuleDestinationStatus `pulumi:"status"`
	// VPC destination properties.
	VpcProperties *TopicRuleDestinationVpcDestinationProperties `pulumi:"vpcProperties"`
}

// The set of arguments for constructing a TopicRuleDestination resource.
type TopicRuleDestinationArgs struct {
	// HTTP URL destination properties.
	HttpUrlProperties TopicRuleDestinationHttpUrlDestinationSummaryPtrInput
	// The status of the TopicRuleDestination.
	Status TopicRuleDestinationTopicRuleDestinationStatusPtrInput
	// VPC destination properties.
	VpcProperties TopicRuleDestinationVpcDestinationPropertiesPtrInput
}

func (TopicRuleDestinationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*topicRuleDestinationArgs)(nil)).Elem()
}

type TopicRuleDestinationInput interface {
	pulumi.Input

	ToTopicRuleDestinationOutput() TopicRuleDestinationOutput
	ToTopicRuleDestinationOutputWithContext(ctx context.Context) TopicRuleDestinationOutput
}

func (*TopicRuleDestination) ElementType() reflect.Type {
	return reflect.TypeOf((*TopicRuleDestination)(nil))
}

func (i *TopicRuleDestination) ToTopicRuleDestinationOutput() TopicRuleDestinationOutput {
	return i.ToTopicRuleDestinationOutputWithContext(context.Background())
}

func (i *TopicRuleDestination) ToTopicRuleDestinationOutputWithContext(ctx context.Context) TopicRuleDestinationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TopicRuleDestinationOutput)
}

type TopicRuleDestinationOutput struct{ *pulumi.OutputState }

func (TopicRuleDestinationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*TopicRuleDestination)(nil))
}

func (o TopicRuleDestinationOutput) ToTopicRuleDestinationOutput() TopicRuleDestinationOutput {
	return o
}

func (o TopicRuleDestinationOutput) ToTopicRuleDestinationOutputWithContext(ctx context.Context) TopicRuleDestinationOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(TopicRuleDestinationOutput{})
}
