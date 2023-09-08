// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package rolesanywhere

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

type TrustAnchorType string

const (
	TrustAnchorTypeAwsAcmPca            = TrustAnchorType("AWS_ACM_PCA")
	TrustAnchorTypeCertificateBundle    = TrustAnchorType("CERTIFICATE_BUNDLE")
	TrustAnchorTypeSelfSignedRepository = TrustAnchorType("SELF_SIGNED_REPOSITORY")
)

func (TrustAnchorType) ElementType() reflect.Type {
	return reflect.TypeOf((*TrustAnchorType)(nil)).Elem()
}

func (e TrustAnchorType) ToTrustAnchorTypeOutput() TrustAnchorTypeOutput {
	return pulumi.ToOutput(e).(TrustAnchorTypeOutput)
}

func (e TrustAnchorType) ToTrustAnchorTypeOutputWithContext(ctx context.Context) TrustAnchorTypeOutput {
	return pulumi.ToOutputWithContext(ctx, e).(TrustAnchorTypeOutput)
}

func (e TrustAnchorType) ToTrustAnchorTypePtrOutput() TrustAnchorTypePtrOutput {
	return e.ToTrustAnchorTypePtrOutputWithContext(context.Background())
}

func (e TrustAnchorType) ToTrustAnchorTypePtrOutputWithContext(ctx context.Context) TrustAnchorTypePtrOutput {
	return TrustAnchorType(e).ToTrustAnchorTypeOutputWithContext(ctx).ToTrustAnchorTypePtrOutputWithContext(ctx)
}

func (e TrustAnchorType) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e TrustAnchorType) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e TrustAnchorType) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e TrustAnchorType) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type TrustAnchorTypeOutput struct{ *pulumi.OutputState }

func (TrustAnchorTypeOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*TrustAnchorType)(nil)).Elem()
}

func (o TrustAnchorTypeOutput) ToTrustAnchorTypeOutput() TrustAnchorTypeOutput {
	return o
}

func (o TrustAnchorTypeOutput) ToTrustAnchorTypeOutputWithContext(ctx context.Context) TrustAnchorTypeOutput {
	return o
}

func (o TrustAnchorTypeOutput) ToTrustAnchorTypePtrOutput() TrustAnchorTypePtrOutput {
	return o.ToTrustAnchorTypePtrOutputWithContext(context.Background())
}

func (o TrustAnchorTypeOutput) ToTrustAnchorTypePtrOutputWithContext(ctx context.Context) TrustAnchorTypePtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v TrustAnchorType) *TrustAnchorType {
		return &v
	}).(TrustAnchorTypePtrOutput)
}

func (o TrustAnchorTypeOutput) ToOutput(ctx context.Context) pulumix.Output[TrustAnchorType] {
	return pulumix.Output[TrustAnchorType]{
		OutputState: o.OutputState,
	}
}

func (o TrustAnchorTypeOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o TrustAnchorTypeOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e TrustAnchorType) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o TrustAnchorTypeOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o TrustAnchorTypeOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e TrustAnchorType) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type TrustAnchorTypePtrOutput struct{ *pulumi.OutputState }

func (TrustAnchorTypePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**TrustAnchorType)(nil)).Elem()
}

func (o TrustAnchorTypePtrOutput) ToTrustAnchorTypePtrOutput() TrustAnchorTypePtrOutput {
	return o
}

func (o TrustAnchorTypePtrOutput) ToTrustAnchorTypePtrOutputWithContext(ctx context.Context) TrustAnchorTypePtrOutput {
	return o
}

func (o TrustAnchorTypePtrOutput) ToOutput(ctx context.Context) pulumix.Output[*TrustAnchorType] {
	return pulumix.Output[*TrustAnchorType]{
		OutputState: o.OutputState,
	}
}

func (o TrustAnchorTypePtrOutput) Elem() TrustAnchorTypeOutput {
	return o.ApplyT(func(v *TrustAnchorType) TrustAnchorType {
		if v != nil {
			return *v
		}
		var ret TrustAnchorType
		return ret
	}).(TrustAnchorTypeOutput)
}

func (o TrustAnchorTypePtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o TrustAnchorTypePtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *TrustAnchorType) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// TrustAnchorTypeInput is an input type that accepts TrustAnchorTypeArgs and TrustAnchorTypeOutput values.
// You can construct a concrete instance of `TrustAnchorTypeInput` via:
//
//	TrustAnchorTypeArgs{...}
type TrustAnchorTypeInput interface {
	pulumi.Input

	ToTrustAnchorTypeOutput() TrustAnchorTypeOutput
	ToTrustAnchorTypeOutputWithContext(context.Context) TrustAnchorTypeOutput
}

var trustAnchorTypePtrType = reflect.TypeOf((**TrustAnchorType)(nil)).Elem()

type TrustAnchorTypePtrInput interface {
	pulumi.Input

	ToTrustAnchorTypePtrOutput() TrustAnchorTypePtrOutput
	ToTrustAnchorTypePtrOutputWithContext(context.Context) TrustAnchorTypePtrOutput
}

type trustAnchorTypePtr string

func TrustAnchorTypePtr(v string) TrustAnchorTypePtrInput {
	return (*trustAnchorTypePtr)(&v)
}

func (*trustAnchorTypePtr) ElementType() reflect.Type {
	return trustAnchorTypePtrType
}

func (in *trustAnchorTypePtr) ToTrustAnchorTypePtrOutput() TrustAnchorTypePtrOutput {
	return pulumi.ToOutput(in).(TrustAnchorTypePtrOutput)
}

func (in *trustAnchorTypePtr) ToTrustAnchorTypePtrOutputWithContext(ctx context.Context) TrustAnchorTypePtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(TrustAnchorTypePtrOutput)
}

func (in *trustAnchorTypePtr) ToOutput(ctx context.Context) pulumix.Output[*TrustAnchorType] {
	return pulumix.Output[*TrustAnchorType]{
		OutputState: in.ToTrustAnchorTypePtrOutputWithContext(ctx).OutputState,
	}
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*TrustAnchorTypeInput)(nil)).Elem(), TrustAnchorType("AWS_ACM_PCA"))
	pulumi.RegisterInputType(reflect.TypeOf((*TrustAnchorTypePtrInput)(nil)).Elem(), TrustAnchorType("AWS_ACM_PCA"))
	pulumi.RegisterOutputType(TrustAnchorTypeOutput{})
	pulumi.RegisterOutputType(TrustAnchorTypePtrOutput{})
}
