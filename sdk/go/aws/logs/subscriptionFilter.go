// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package logs

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Subscription filters allow you to subscribe to a real-time stream of log events and have them delivered to a specific destination.
type SubscriptionFilter struct {
	pulumi.CustomResourceState

	// The Amazon Resource Name (ARN) of the destination.
	DestinationArn pulumi.StringOutput `pulumi:"destinationArn"`
	// The method used to distribute log data to the destination. By default, log data is grouped by log stream, but the grouping can be set to random for a more even distribution. This property is only applicable when the destination is an Amazon Kinesis stream.
	Distribution SubscriptionFilterDistributionPtrOutput `pulumi:"distribution"`
	// The name of the filter generated by resource.
	FilterName pulumi.StringPtrOutput `pulumi:"filterName"`
	// The filtering expressions that restrict what gets delivered to the destination AWS resource.
	FilterPattern pulumi.StringOutput `pulumi:"filterPattern"`
	// Existing log group that you want to associate with this filter.
	LogGroupName pulumi.StringOutput `pulumi:"logGroupName"`
	// The ARN of an IAM role that grants CloudWatch Logs permissions to deliver ingested log events to the destination stream. You don't need to provide the ARN when you are working with a logical destination for cross-account delivery.
	RoleArn pulumi.StringPtrOutput `pulumi:"roleArn"`
}

// NewSubscriptionFilter registers a new resource with the given unique name, arguments, and options.
func NewSubscriptionFilter(ctx *pulumi.Context,
	name string, args *SubscriptionFilterArgs, opts ...pulumi.ResourceOption) (*SubscriptionFilter, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DestinationArn == nil {
		return nil, errors.New("invalid value for required argument 'DestinationArn'")
	}
	if args.FilterPattern == nil {
		return nil, errors.New("invalid value for required argument 'FilterPattern'")
	}
	if args.LogGroupName == nil {
		return nil, errors.New("invalid value for required argument 'LogGroupName'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"filterName",
		"logGroupName",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource SubscriptionFilter
	err := ctx.RegisterResource("aws-native:logs:SubscriptionFilter", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSubscriptionFilter gets an existing SubscriptionFilter resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSubscriptionFilter(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SubscriptionFilterState, opts ...pulumi.ResourceOption) (*SubscriptionFilter, error) {
	var resource SubscriptionFilter
	err := ctx.ReadResource("aws-native:logs:SubscriptionFilter", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering SubscriptionFilter resources.
type subscriptionFilterState struct {
}

type SubscriptionFilterState struct {
}

func (SubscriptionFilterState) ElementType() reflect.Type {
	return reflect.TypeOf((*subscriptionFilterState)(nil)).Elem()
}

type subscriptionFilterArgs struct {
	// The Amazon Resource Name (ARN) of the destination.
	DestinationArn string `pulumi:"destinationArn"`
	// The method used to distribute log data to the destination. By default, log data is grouped by log stream, but the grouping can be set to random for a more even distribution. This property is only applicable when the destination is an Amazon Kinesis stream.
	Distribution *SubscriptionFilterDistribution `pulumi:"distribution"`
	// The name of the filter generated by resource.
	FilterName *string `pulumi:"filterName"`
	// The filtering expressions that restrict what gets delivered to the destination AWS resource.
	FilterPattern string `pulumi:"filterPattern"`
	// Existing log group that you want to associate with this filter.
	LogGroupName string `pulumi:"logGroupName"`
	// The ARN of an IAM role that grants CloudWatch Logs permissions to deliver ingested log events to the destination stream. You don't need to provide the ARN when you are working with a logical destination for cross-account delivery.
	RoleArn *string `pulumi:"roleArn"`
}

// The set of arguments for constructing a SubscriptionFilter resource.
type SubscriptionFilterArgs struct {
	// The Amazon Resource Name (ARN) of the destination.
	DestinationArn pulumi.StringInput
	// The method used to distribute log data to the destination. By default, log data is grouped by log stream, but the grouping can be set to random for a more even distribution. This property is only applicable when the destination is an Amazon Kinesis stream.
	Distribution SubscriptionFilterDistributionPtrInput
	// The name of the filter generated by resource.
	FilterName pulumi.StringPtrInput
	// The filtering expressions that restrict what gets delivered to the destination AWS resource.
	FilterPattern pulumi.StringInput
	// Existing log group that you want to associate with this filter.
	LogGroupName pulumi.StringInput
	// The ARN of an IAM role that grants CloudWatch Logs permissions to deliver ingested log events to the destination stream. You don't need to provide the ARN when you are working with a logical destination for cross-account delivery.
	RoleArn pulumi.StringPtrInput
}

func (SubscriptionFilterArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*subscriptionFilterArgs)(nil)).Elem()
}

type SubscriptionFilterInput interface {
	pulumi.Input

	ToSubscriptionFilterOutput() SubscriptionFilterOutput
	ToSubscriptionFilterOutputWithContext(ctx context.Context) SubscriptionFilterOutput
}

func (*SubscriptionFilter) ElementType() reflect.Type {
	return reflect.TypeOf((**SubscriptionFilter)(nil)).Elem()
}

func (i *SubscriptionFilter) ToSubscriptionFilterOutput() SubscriptionFilterOutput {
	return i.ToSubscriptionFilterOutputWithContext(context.Background())
}

func (i *SubscriptionFilter) ToSubscriptionFilterOutputWithContext(ctx context.Context) SubscriptionFilterOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SubscriptionFilterOutput)
}

func (i *SubscriptionFilter) ToOutput(ctx context.Context) pulumix.Output[*SubscriptionFilter] {
	return pulumix.Output[*SubscriptionFilter]{
		OutputState: i.ToSubscriptionFilterOutputWithContext(ctx).OutputState,
	}
}

type SubscriptionFilterOutput struct{ *pulumi.OutputState }

func (SubscriptionFilterOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**SubscriptionFilter)(nil)).Elem()
}

func (o SubscriptionFilterOutput) ToSubscriptionFilterOutput() SubscriptionFilterOutput {
	return o
}

func (o SubscriptionFilterOutput) ToSubscriptionFilterOutputWithContext(ctx context.Context) SubscriptionFilterOutput {
	return o
}

func (o SubscriptionFilterOutput) ToOutput(ctx context.Context) pulumix.Output[*SubscriptionFilter] {
	return pulumix.Output[*SubscriptionFilter]{
		OutputState: o.OutputState,
	}
}

// The Amazon Resource Name (ARN) of the destination.
func (o SubscriptionFilterOutput) DestinationArn() pulumi.StringOutput {
	return o.ApplyT(func(v *SubscriptionFilter) pulumi.StringOutput { return v.DestinationArn }).(pulumi.StringOutput)
}

// The method used to distribute log data to the destination. By default, log data is grouped by log stream, but the grouping can be set to random for a more even distribution. This property is only applicable when the destination is an Amazon Kinesis stream.
func (o SubscriptionFilterOutput) Distribution() SubscriptionFilterDistributionPtrOutput {
	return o.ApplyT(func(v *SubscriptionFilter) SubscriptionFilterDistributionPtrOutput { return v.Distribution }).(SubscriptionFilterDistributionPtrOutput)
}

// The name of the filter generated by resource.
func (o SubscriptionFilterOutput) FilterName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *SubscriptionFilter) pulumi.StringPtrOutput { return v.FilterName }).(pulumi.StringPtrOutput)
}

// The filtering expressions that restrict what gets delivered to the destination AWS resource.
func (o SubscriptionFilterOutput) FilterPattern() pulumi.StringOutput {
	return o.ApplyT(func(v *SubscriptionFilter) pulumi.StringOutput { return v.FilterPattern }).(pulumi.StringOutput)
}

// Existing log group that you want to associate with this filter.
func (o SubscriptionFilterOutput) LogGroupName() pulumi.StringOutput {
	return o.ApplyT(func(v *SubscriptionFilter) pulumi.StringOutput { return v.LogGroupName }).(pulumi.StringOutput)
}

// The ARN of an IAM role that grants CloudWatch Logs permissions to deliver ingested log events to the destination stream. You don't need to provide the ARN when you are working with a logical destination for cross-account delivery.
func (o SubscriptionFilterOutput) RoleArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *SubscriptionFilter) pulumi.StringPtrOutput { return v.RoleArn }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*SubscriptionFilterInput)(nil)).Elem(), &SubscriptionFilter{})
	pulumi.RegisterOutputType(SubscriptionFilterOutput{})
}
