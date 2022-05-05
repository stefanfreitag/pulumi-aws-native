// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package kinesisvideo

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type Definition for AWS::KinesisVideo::SignalingChannel
type SignalingChannel struct {
	pulumi.CustomResourceState

	// The Amazon Resource Name (ARN) of the Kinesis Video Signaling Channel.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// The period of time a signaling channel retains undelivered messages before they are discarded.
	MessageTtlSeconds pulumi.IntPtrOutput `pulumi:"messageTtlSeconds"`
	// The name of the Kinesis Video Signaling Channel.
	Name pulumi.StringPtrOutput `pulumi:"name"`
	// An array of key-value pairs to apply to this resource.
	Tags SignalingChannelTagArrayOutput `pulumi:"tags"`
	// The type of the Kinesis Video Signaling Channel to create. Currently, SINGLE_MASTER is the only supported channel type.
	Type SignalingChannelTypePtrOutput `pulumi:"type"`
}

// NewSignalingChannel registers a new resource with the given unique name, arguments, and options.
func NewSignalingChannel(ctx *pulumi.Context,
	name string, args *SignalingChannelArgs, opts ...pulumi.ResourceOption) (*SignalingChannel, error) {
	if args == nil {
		args = &SignalingChannelArgs{}
	}

	var resource SignalingChannel
	err := ctx.RegisterResource("aws-native:kinesisvideo:SignalingChannel", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSignalingChannel gets an existing SignalingChannel resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSignalingChannel(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SignalingChannelState, opts ...pulumi.ResourceOption) (*SignalingChannel, error) {
	var resource SignalingChannel
	err := ctx.ReadResource("aws-native:kinesisvideo:SignalingChannel", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering SignalingChannel resources.
type signalingChannelState struct {
}

type SignalingChannelState struct {
}

func (SignalingChannelState) ElementType() reflect.Type {
	return reflect.TypeOf((*signalingChannelState)(nil)).Elem()
}

type signalingChannelArgs struct {
	// The period of time a signaling channel retains undelivered messages before they are discarded.
	MessageTtlSeconds *int `pulumi:"messageTtlSeconds"`
	// The name of the Kinesis Video Signaling Channel.
	Name *string `pulumi:"name"`
	// An array of key-value pairs to apply to this resource.
	Tags []SignalingChannelTag `pulumi:"tags"`
	// The type of the Kinesis Video Signaling Channel to create. Currently, SINGLE_MASTER is the only supported channel type.
	Type *SignalingChannelType `pulumi:"type"`
}

// The set of arguments for constructing a SignalingChannel resource.
type SignalingChannelArgs struct {
	// The period of time a signaling channel retains undelivered messages before they are discarded.
	MessageTtlSeconds pulumi.IntPtrInput
	// The name of the Kinesis Video Signaling Channel.
	Name pulumi.StringPtrInput
	// An array of key-value pairs to apply to this resource.
	Tags SignalingChannelTagArrayInput
	// The type of the Kinesis Video Signaling Channel to create. Currently, SINGLE_MASTER is the only supported channel type.
	Type SignalingChannelTypePtrInput
}

func (SignalingChannelArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*signalingChannelArgs)(nil)).Elem()
}

type SignalingChannelInput interface {
	pulumi.Input

	ToSignalingChannelOutput() SignalingChannelOutput
	ToSignalingChannelOutputWithContext(ctx context.Context) SignalingChannelOutput
}

func (*SignalingChannel) ElementType() reflect.Type {
	return reflect.TypeOf((**SignalingChannel)(nil)).Elem()
}

func (i *SignalingChannel) ToSignalingChannelOutput() SignalingChannelOutput {
	return i.ToSignalingChannelOutputWithContext(context.Background())
}

func (i *SignalingChannel) ToSignalingChannelOutputWithContext(ctx context.Context) SignalingChannelOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SignalingChannelOutput)
}

type SignalingChannelOutput struct{ *pulumi.OutputState }

func (SignalingChannelOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**SignalingChannel)(nil)).Elem()
}

func (o SignalingChannelOutput) ToSignalingChannelOutput() SignalingChannelOutput {
	return o
}

func (o SignalingChannelOutput) ToSignalingChannelOutputWithContext(ctx context.Context) SignalingChannelOutput {
	return o
}

// The Amazon Resource Name (ARN) of the Kinesis Video Signaling Channel.
func (o SignalingChannelOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *SignalingChannel) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

// The period of time a signaling channel retains undelivered messages before they are discarded.
func (o SignalingChannelOutput) MessageTtlSeconds() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *SignalingChannel) pulumi.IntPtrOutput { return v.MessageTtlSeconds }).(pulumi.IntPtrOutput)
}

// The name of the Kinesis Video Signaling Channel.
func (o SignalingChannelOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *SignalingChannel) pulumi.StringPtrOutput { return v.Name }).(pulumi.StringPtrOutput)
}

// An array of key-value pairs to apply to this resource.
func (o SignalingChannelOutput) Tags() SignalingChannelTagArrayOutput {
	return o.ApplyT(func(v *SignalingChannel) SignalingChannelTagArrayOutput { return v.Tags }).(SignalingChannelTagArrayOutput)
}

// The type of the Kinesis Video Signaling Channel to create. Currently, SINGLE_MASTER is the only supported channel type.
func (o SignalingChannelOutput) Type() SignalingChannelTypePtrOutput {
	return o.ApplyT(func(v *SignalingChannel) SignalingChannelTypePtrOutput { return v.Type }).(SignalingChannelTypePtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*SignalingChannelInput)(nil)).Elem(), &SignalingChannel{})
	pulumi.RegisterOutputType(SignalingChannelOutput{})
}
