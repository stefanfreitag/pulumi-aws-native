// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package kinesis

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The encryption type to use. The only valid value is KMS.
type StreamStreamEncryptionEncryptionType string

const (
	StreamStreamEncryptionEncryptionTypeKms = StreamStreamEncryptionEncryptionType("KMS")
)

func (StreamStreamEncryptionEncryptionType) ElementType() reflect.Type {
	return reflect.TypeOf((*StreamStreamEncryptionEncryptionType)(nil)).Elem()
}

func (e StreamStreamEncryptionEncryptionType) ToStreamStreamEncryptionEncryptionTypeOutput() StreamStreamEncryptionEncryptionTypeOutput {
	return pulumi.ToOutput(e).(StreamStreamEncryptionEncryptionTypeOutput)
}

func (e StreamStreamEncryptionEncryptionType) ToStreamStreamEncryptionEncryptionTypeOutputWithContext(ctx context.Context) StreamStreamEncryptionEncryptionTypeOutput {
	return pulumi.ToOutputWithContext(ctx, e).(StreamStreamEncryptionEncryptionTypeOutput)
}

func (e StreamStreamEncryptionEncryptionType) ToStreamStreamEncryptionEncryptionTypePtrOutput() StreamStreamEncryptionEncryptionTypePtrOutput {
	return e.ToStreamStreamEncryptionEncryptionTypePtrOutputWithContext(context.Background())
}

func (e StreamStreamEncryptionEncryptionType) ToStreamStreamEncryptionEncryptionTypePtrOutputWithContext(ctx context.Context) StreamStreamEncryptionEncryptionTypePtrOutput {
	return StreamStreamEncryptionEncryptionType(e).ToStreamStreamEncryptionEncryptionTypeOutputWithContext(ctx).ToStreamStreamEncryptionEncryptionTypePtrOutputWithContext(ctx)
}

func (e StreamStreamEncryptionEncryptionType) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e StreamStreamEncryptionEncryptionType) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e StreamStreamEncryptionEncryptionType) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e StreamStreamEncryptionEncryptionType) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type StreamStreamEncryptionEncryptionTypeOutput struct{ *pulumi.OutputState }

func (StreamStreamEncryptionEncryptionTypeOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*StreamStreamEncryptionEncryptionType)(nil)).Elem()
}

func (o StreamStreamEncryptionEncryptionTypeOutput) ToStreamStreamEncryptionEncryptionTypeOutput() StreamStreamEncryptionEncryptionTypeOutput {
	return o
}

func (o StreamStreamEncryptionEncryptionTypeOutput) ToStreamStreamEncryptionEncryptionTypeOutputWithContext(ctx context.Context) StreamStreamEncryptionEncryptionTypeOutput {
	return o
}

func (o StreamStreamEncryptionEncryptionTypeOutput) ToStreamStreamEncryptionEncryptionTypePtrOutput() StreamStreamEncryptionEncryptionTypePtrOutput {
	return o.ToStreamStreamEncryptionEncryptionTypePtrOutputWithContext(context.Background())
}

func (o StreamStreamEncryptionEncryptionTypeOutput) ToStreamStreamEncryptionEncryptionTypePtrOutputWithContext(ctx context.Context) StreamStreamEncryptionEncryptionTypePtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v StreamStreamEncryptionEncryptionType) *StreamStreamEncryptionEncryptionType {
		return &v
	}).(StreamStreamEncryptionEncryptionTypePtrOutput)
}

func (o StreamStreamEncryptionEncryptionTypeOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o StreamStreamEncryptionEncryptionTypeOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e StreamStreamEncryptionEncryptionType) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o StreamStreamEncryptionEncryptionTypeOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o StreamStreamEncryptionEncryptionTypeOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e StreamStreamEncryptionEncryptionType) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type StreamStreamEncryptionEncryptionTypePtrOutput struct{ *pulumi.OutputState }

func (StreamStreamEncryptionEncryptionTypePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**StreamStreamEncryptionEncryptionType)(nil)).Elem()
}

func (o StreamStreamEncryptionEncryptionTypePtrOutput) ToStreamStreamEncryptionEncryptionTypePtrOutput() StreamStreamEncryptionEncryptionTypePtrOutput {
	return o
}

func (o StreamStreamEncryptionEncryptionTypePtrOutput) ToStreamStreamEncryptionEncryptionTypePtrOutputWithContext(ctx context.Context) StreamStreamEncryptionEncryptionTypePtrOutput {
	return o
}

func (o StreamStreamEncryptionEncryptionTypePtrOutput) Elem() StreamStreamEncryptionEncryptionTypeOutput {
	return o.ApplyT(func(v *StreamStreamEncryptionEncryptionType) StreamStreamEncryptionEncryptionType {
		if v != nil {
			return *v
		}
		var ret StreamStreamEncryptionEncryptionType
		return ret
	}).(StreamStreamEncryptionEncryptionTypeOutput)
}

func (o StreamStreamEncryptionEncryptionTypePtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o StreamStreamEncryptionEncryptionTypePtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *StreamStreamEncryptionEncryptionType) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// StreamStreamEncryptionEncryptionTypeInput is an input type that accepts StreamStreamEncryptionEncryptionTypeArgs and StreamStreamEncryptionEncryptionTypeOutput values.
// You can construct a concrete instance of `StreamStreamEncryptionEncryptionTypeInput` via:
//
//          StreamStreamEncryptionEncryptionTypeArgs{...}
type StreamStreamEncryptionEncryptionTypeInput interface {
	pulumi.Input

	ToStreamStreamEncryptionEncryptionTypeOutput() StreamStreamEncryptionEncryptionTypeOutput
	ToStreamStreamEncryptionEncryptionTypeOutputWithContext(context.Context) StreamStreamEncryptionEncryptionTypeOutput
}

var streamStreamEncryptionEncryptionTypePtrType = reflect.TypeOf((**StreamStreamEncryptionEncryptionType)(nil)).Elem()

type StreamStreamEncryptionEncryptionTypePtrInput interface {
	pulumi.Input

	ToStreamStreamEncryptionEncryptionTypePtrOutput() StreamStreamEncryptionEncryptionTypePtrOutput
	ToStreamStreamEncryptionEncryptionTypePtrOutputWithContext(context.Context) StreamStreamEncryptionEncryptionTypePtrOutput
}

type streamStreamEncryptionEncryptionTypePtr string

func StreamStreamEncryptionEncryptionTypePtr(v string) StreamStreamEncryptionEncryptionTypePtrInput {
	return (*streamStreamEncryptionEncryptionTypePtr)(&v)
}

func (*streamStreamEncryptionEncryptionTypePtr) ElementType() reflect.Type {
	return streamStreamEncryptionEncryptionTypePtrType
}

func (in *streamStreamEncryptionEncryptionTypePtr) ToStreamStreamEncryptionEncryptionTypePtrOutput() StreamStreamEncryptionEncryptionTypePtrOutput {
	return pulumi.ToOutput(in).(StreamStreamEncryptionEncryptionTypePtrOutput)
}

func (in *streamStreamEncryptionEncryptionTypePtr) ToStreamStreamEncryptionEncryptionTypePtrOutputWithContext(ctx context.Context) StreamStreamEncryptionEncryptionTypePtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(StreamStreamEncryptionEncryptionTypePtrOutput)
}

func init() {
	pulumi.RegisterOutputType(StreamStreamEncryptionEncryptionTypeOutput{})
	pulumi.RegisterOutputType(StreamStreamEncryptionEncryptionTypePtrOutput{})
}
