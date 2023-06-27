// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package oam

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::Oam::Sink
type Sink struct {
	pulumi.CustomResourceState

	// The Amazon resource name (ARN) of the ObservabilityAccessManager Sink
	Arn pulumi.StringOutput `pulumi:"arn"`
	// The name of the ObservabilityAccessManager Sink.
	Name pulumi.StringOutput `pulumi:"name"`
	// The policy of this ObservabilityAccessManager Sink.
	Policy pulumi.AnyOutput `pulumi:"policy"`
	// Tags to apply to the sink
	Tags pulumi.AnyOutput `pulumi:"tags"`
}

// NewSink registers a new resource with the given unique name, arguments, and options.
func NewSink(ctx *pulumi.Context,
	name string, args *SinkArgs, opts ...pulumi.ResourceOption) (*Sink, error) {
	if args == nil {
		args = &SinkArgs{}
	}

	var resource Sink
	err := ctx.RegisterResource("aws-native:oam:Sink", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSink gets an existing Sink resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSink(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SinkState, opts ...pulumi.ResourceOption) (*Sink, error) {
	var resource Sink
	err := ctx.ReadResource("aws-native:oam:Sink", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Sink resources.
type sinkState struct {
}

type SinkState struct {
}

func (SinkState) ElementType() reflect.Type {
	return reflect.TypeOf((*sinkState)(nil)).Elem()
}

type sinkArgs struct {
	// The name of the ObservabilityAccessManager Sink.
	Name *string `pulumi:"name"`
	// The policy of this ObservabilityAccessManager Sink.
	Policy interface{} `pulumi:"policy"`
	// Tags to apply to the sink
	Tags interface{} `pulumi:"tags"`
}

// The set of arguments for constructing a Sink resource.
type SinkArgs struct {
	// The name of the ObservabilityAccessManager Sink.
	Name pulumi.StringPtrInput
	// The policy of this ObservabilityAccessManager Sink.
	Policy pulumi.Input
	// Tags to apply to the sink
	Tags pulumi.Input
}

func (SinkArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*sinkArgs)(nil)).Elem()
}

type SinkInput interface {
	pulumi.Input

	ToSinkOutput() SinkOutput
	ToSinkOutputWithContext(ctx context.Context) SinkOutput
}

func (*Sink) ElementType() reflect.Type {
	return reflect.TypeOf((**Sink)(nil)).Elem()
}

func (i *Sink) ToSinkOutput() SinkOutput {
	return i.ToSinkOutputWithContext(context.Background())
}

func (i *Sink) ToSinkOutputWithContext(ctx context.Context) SinkOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SinkOutput)
}

type SinkOutput struct{ *pulumi.OutputState }

func (SinkOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Sink)(nil)).Elem()
}

func (o SinkOutput) ToSinkOutput() SinkOutput {
	return o
}

func (o SinkOutput) ToSinkOutputWithContext(ctx context.Context) SinkOutput {
	return o
}

// The Amazon resource name (ARN) of the ObservabilityAccessManager Sink
func (o SinkOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *Sink) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

// The name of the ObservabilityAccessManager Sink.
func (o SinkOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Sink) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// The policy of this ObservabilityAccessManager Sink.
func (o SinkOutput) Policy() pulumi.AnyOutput {
	return o.ApplyT(func(v *Sink) pulumi.AnyOutput { return v.Policy }).(pulumi.AnyOutput)
}

// Tags to apply to the sink
func (o SinkOutput) Tags() pulumi.AnyOutput {
	return o.ApplyT(func(v *Sink) pulumi.AnyOutput { return v.Tags }).(pulumi.AnyOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*SinkInput)(nil)).Elem(), &Sink{})
	pulumi.RegisterOutputType(SinkOutput{})
}
