// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package kinesisvideo

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// The type of the Kinesis Video Signaling Channel to create. Currently, SINGLE_MASTER is the only supported channel type.
type SignalingChannelType string

const (
	SignalingChannelTypeSingleMaster = SignalingChannelType("SINGLE_MASTER")
)

func (SignalingChannelType) ElementType() reflect.Type {
	return reflect.TypeOf((*SignalingChannelType)(nil)).Elem()
}

func (e SignalingChannelType) ToSignalingChannelTypeOutput() SignalingChannelTypeOutput {
	return pulumi.ToOutput(e).(SignalingChannelTypeOutput)
}

func (e SignalingChannelType) ToSignalingChannelTypeOutputWithContext(ctx context.Context) SignalingChannelTypeOutput {
	return pulumi.ToOutputWithContext(ctx, e).(SignalingChannelTypeOutput)
}

func (e SignalingChannelType) ToSignalingChannelTypePtrOutput() SignalingChannelTypePtrOutput {
	return e.ToSignalingChannelTypePtrOutputWithContext(context.Background())
}

func (e SignalingChannelType) ToSignalingChannelTypePtrOutputWithContext(ctx context.Context) SignalingChannelTypePtrOutput {
	return SignalingChannelType(e).ToSignalingChannelTypeOutputWithContext(ctx).ToSignalingChannelTypePtrOutputWithContext(ctx)
}

func (e SignalingChannelType) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e SignalingChannelType) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e SignalingChannelType) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e SignalingChannelType) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type SignalingChannelTypeOutput struct{ *pulumi.OutputState }

func (SignalingChannelTypeOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*SignalingChannelType)(nil)).Elem()
}

func (o SignalingChannelTypeOutput) ToSignalingChannelTypeOutput() SignalingChannelTypeOutput {
	return o
}

func (o SignalingChannelTypeOutput) ToSignalingChannelTypeOutputWithContext(ctx context.Context) SignalingChannelTypeOutput {
	return o
}

func (o SignalingChannelTypeOutput) ToSignalingChannelTypePtrOutput() SignalingChannelTypePtrOutput {
	return o.ToSignalingChannelTypePtrOutputWithContext(context.Background())
}

func (o SignalingChannelTypeOutput) ToSignalingChannelTypePtrOutputWithContext(ctx context.Context) SignalingChannelTypePtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v SignalingChannelType) *SignalingChannelType {
		return &v
	}).(SignalingChannelTypePtrOutput)
}

func (o SignalingChannelTypeOutput) ToOutput(ctx context.Context) pulumix.Output[SignalingChannelType] {
	return pulumix.Output[SignalingChannelType]{
		OutputState: o.OutputState,
	}
}

func (o SignalingChannelTypeOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o SignalingChannelTypeOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e SignalingChannelType) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o SignalingChannelTypeOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o SignalingChannelTypeOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e SignalingChannelType) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type SignalingChannelTypePtrOutput struct{ *pulumi.OutputState }

func (SignalingChannelTypePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**SignalingChannelType)(nil)).Elem()
}

func (o SignalingChannelTypePtrOutput) ToSignalingChannelTypePtrOutput() SignalingChannelTypePtrOutput {
	return o
}

func (o SignalingChannelTypePtrOutput) ToSignalingChannelTypePtrOutputWithContext(ctx context.Context) SignalingChannelTypePtrOutput {
	return o
}

func (o SignalingChannelTypePtrOutput) ToOutput(ctx context.Context) pulumix.Output[*SignalingChannelType] {
	return pulumix.Output[*SignalingChannelType]{
		OutputState: o.OutputState,
	}
}

func (o SignalingChannelTypePtrOutput) Elem() SignalingChannelTypeOutput {
	return o.ApplyT(func(v *SignalingChannelType) SignalingChannelType {
		if v != nil {
			return *v
		}
		var ret SignalingChannelType
		return ret
	}).(SignalingChannelTypeOutput)
}

func (o SignalingChannelTypePtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o SignalingChannelTypePtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *SignalingChannelType) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// SignalingChannelTypeInput is an input type that accepts SignalingChannelTypeArgs and SignalingChannelTypeOutput values.
// You can construct a concrete instance of `SignalingChannelTypeInput` via:
//
//	SignalingChannelTypeArgs{...}
type SignalingChannelTypeInput interface {
	pulumi.Input

	ToSignalingChannelTypeOutput() SignalingChannelTypeOutput
	ToSignalingChannelTypeOutputWithContext(context.Context) SignalingChannelTypeOutput
}

var signalingChannelTypePtrType = reflect.TypeOf((**SignalingChannelType)(nil)).Elem()

type SignalingChannelTypePtrInput interface {
	pulumi.Input

	ToSignalingChannelTypePtrOutput() SignalingChannelTypePtrOutput
	ToSignalingChannelTypePtrOutputWithContext(context.Context) SignalingChannelTypePtrOutput
}

type signalingChannelTypePtr string

func SignalingChannelTypePtr(v string) SignalingChannelTypePtrInput {
	return (*signalingChannelTypePtr)(&v)
}

func (*signalingChannelTypePtr) ElementType() reflect.Type {
	return signalingChannelTypePtrType
}

func (in *signalingChannelTypePtr) ToSignalingChannelTypePtrOutput() SignalingChannelTypePtrOutput {
	return pulumi.ToOutput(in).(SignalingChannelTypePtrOutput)
}

func (in *signalingChannelTypePtr) ToSignalingChannelTypePtrOutputWithContext(ctx context.Context) SignalingChannelTypePtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(SignalingChannelTypePtrOutput)
}

func (in *signalingChannelTypePtr) ToOutput(ctx context.Context) pulumix.Output[*SignalingChannelType] {
	return pulumix.Output[*SignalingChannelType]{
		OutputState: in.ToSignalingChannelTypePtrOutputWithContext(ctx).OutputState,
	}
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*SignalingChannelTypeInput)(nil)).Elem(), SignalingChannelType("SINGLE_MASTER"))
	pulumi.RegisterInputType(reflect.TypeOf((*SignalingChannelTypePtrInput)(nil)).Elem(), SignalingChannelType("SINGLE_MASTER"))
	pulumi.RegisterOutputType(SignalingChannelTypeOutput{})
	pulumi.RegisterOutputType(SignalingChannelTypePtrOutput{})
}
