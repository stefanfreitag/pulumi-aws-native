// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package mediaconvert

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::MediaConvert::Queue
//
// Deprecated: Queue is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type Queue struct {
	pulumi.CustomResourceState

	Arn         pulumi.StringOutput    `pulumi:"arn"`
	Description pulumi.StringPtrOutput `pulumi:"description"`
	Name        pulumi.StringPtrOutput `pulumi:"name"`
	PricingPlan pulumi.StringPtrOutput `pulumi:"pricingPlan"`
	Status      pulumi.StringPtrOutput `pulumi:"status"`
	Tags        pulumi.AnyOutput       `pulumi:"tags"`
}

// NewQueue registers a new resource with the given unique name, arguments, and options.
func NewQueue(ctx *pulumi.Context,
	name string, args *QueueArgs, opts ...pulumi.ResourceOption) (*Queue, error) {
	if args == nil {
		args = &QueueArgs{}
	}

	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"name",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Queue
	err := ctx.RegisterResource("aws-native:mediaconvert:Queue", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetQueue gets an existing Queue resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetQueue(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *QueueState, opts ...pulumi.ResourceOption) (*Queue, error) {
	var resource Queue
	err := ctx.ReadResource("aws-native:mediaconvert:Queue", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Queue resources.
type queueState struct {
}

type QueueState struct {
}

func (QueueState) ElementType() reflect.Type {
	return reflect.TypeOf((*queueState)(nil)).Elem()
}

type queueArgs struct {
	Description *string     `pulumi:"description"`
	Name        *string     `pulumi:"name"`
	PricingPlan *string     `pulumi:"pricingPlan"`
	Status      *string     `pulumi:"status"`
	Tags        interface{} `pulumi:"tags"`
}

// The set of arguments for constructing a Queue resource.
type QueueArgs struct {
	Description pulumi.StringPtrInput
	Name        pulumi.StringPtrInput
	PricingPlan pulumi.StringPtrInput
	Status      pulumi.StringPtrInput
	Tags        pulumi.Input
}

func (QueueArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*queueArgs)(nil)).Elem()
}

type QueueInput interface {
	pulumi.Input

	ToQueueOutput() QueueOutput
	ToQueueOutputWithContext(ctx context.Context) QueueOutput
}

func (*Queue) ElementType() reflect.Type {
	return reflect.TypeOf((**Queue)(nil)).Elem()
}

func (i *Queue) ToQueueOutput() QueueOutput {
	return i.ToQueueOutputWithContext(context.Background())
}

func (i *Queue) ToQueueOutputWithContext(ctx context.Context) QueueOutput {
	return pulumi.ToOutputWithContext(ctx, i).(QueueOutput)
}

func (i *Queue) ToOutput(ctx context.Context) pulumix.Output[*Queue] {
	return pulumix.Output[*Queue]{
		OutputState: i.ToQueueOutputWithContext(ctx).OutputState,
	}
}

type QueueOutput struct{ *pulumi.OutputState }

func (QueueOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Queue)(nil)).Elem()
}

func (o QueueOutput) ToQueueOutput() QueueOutput {
	return o
}

func (o QueueOutput) ToQueueOutputWithContext(ctx context.Context) QueueOutput {
	return o
}

func (o QueueOutput) ToOutput(ctx context.Context) pulumix.Output[*Queue] {
	return pulumix.Output[*Queue]{
		OutputState: o.OutputState,
	}
}

func (o QueueOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *Queue) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

func (o QueueOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Queue) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

func (o QueueOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Queue) pulumi.StringPtrOutput { return v.Name }).(pulumi.StringPtrOutput)
}

func (o QueueOutput) PricingPlan() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Queue) pulumi.StringPtrOutput { return v.PricingPlan }).(pulumi.StringPtrOutput)
}

func (o QueueOutput) Status() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Queue) pulumi.StringPtrOutput { return v.Status }).(pulumi.StringPtrOutput)
}

func (o QueueOutput) Tags() pulumi.AnyOutput {
	return o.ApplyT(func(v *Queue) pulumi.AnyOutput { return v.Tags }).(pulumi.AnyOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*QueueInput)(nil)).Elem(), &Queue{})
	pulumi.RegisterOutputType(QueueOutput{})
}
