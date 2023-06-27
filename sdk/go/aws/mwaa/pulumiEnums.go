// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package mwaa

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type EnvironmentLoggingLevel string

const (
	EnvironmentLoggingLevelCritical = EnvironmentLoggingLevel("CRITICAL")
	EnvironmentLoggingLevelError    = EnvironmentLoggingLevel("ERROR")
	EnvironmentLoggingLevelWarning  = EnvironmentLoggingLevel("WARNING")
	EnvironmentLoggingLevelInfo     = EnvironmentLoggingLevel("INFO")
	EnvironmentLoggingLevelDebug    = EnvironmentLoggingLevel("DEBUG")
)

func (EnvironmentLoggingLevel) ElementType() reflect.Type {
	return reflect.TypeOf((*EnvironmentLoggingLevel)(nil)).Elem()
}

func (e EnvironmentLoggingLevel) ToEnvironmentLoggingLevelOutput() EnvironmentLoggingLevelOutput {
	return pulumi.ToOutput(e).(EnvironmentLoggingLevelOutput)
}

func (e EnvironmentLoggingLevel) ToEnvironmentLoggingLevelOutputWithContext(ctx context.Context) EnvironmentLoggingLevelOutput {
	return pulumi.ToOutputWithContext(ctx, e).(EnvironmentLoggingLevelOutput)
}

func (e EnvironmentLoggingLevel) ToEnvironmentLoggingLevelPtrOutput() EnvironmentLoggingLevelPtrOutput {
	return e.ToEnvironmentLoggingLevelPtrOutputWithContext(context.Background())
}

func (e EnvironmentLoggingLevel) ToEnvironmentLoggingLevelPtrOutputWithContext(ctx context.Context) EnvironmentLoggingLevelPtrOutput {
	return EnvironmentLoggingLevel(e).ToEnvironmentLoggingLevelOutputWithContext(ctx).ToEnvironmentLoggingLevelPtrOutputWithContext(ctx)
}

func (e EnvironmentLoggingLevel) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e EnvironmentLoggingLevel) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e EnvironmentLoggingLevel) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e EnvironmentLoggingLevel) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type EnvironmentLoggingLevelOutput struct{ *pulumi.OutputState }

func (EnvironmentLoggingLevelOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*EnvironmentLoggingLevel)(nil)).Elem()
}

func (o EnvironmentLoggingLevelOutput) ToEnvironmentLoggingLevelOutput() EnvironmentLoggingLevelOutput {
	return o
}

func (o EnvironmentLoggingLevelOutput) ToEnvironmentLoggingLevelOutputWithContext(ctx context.Context) EnvironmentLoggingLevelOutput {
	return o
}

func (o EnvironmentLoggingLevelOutput) ToEnvironmentLoggingLevelPtrOutput() EnvironmentLoggingLevelPtrOutput {
	return o.ToEnvironmentLoggingLevelPtrOutputWithContext(context.Background())
}

func (o EnvironmentLoggingLevelOutput) ToEnvironmentLoggingLevelPtrOutputWithContext(ctx context.Context) EnvironmentLoggingLevelPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v EnvironmentLoggingLevel) *EnvironmentLoggingLevel {
		return &v
	}).(EnvironmentLoggingLevelPtrOutput)
}

func (o EnvironmentLoggingLevelOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o EnvironmentLoggingLevelOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e EnvironmentLoggingLevel) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o EnvironmentLoggingLevelOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o EnvironmentLoggingLevelOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e EnvironmentLoggingLevel) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type EnvironmentLoggingLevelPtrOutput struct{ *pulumi.OutputState }

func (EnvironmentLoggingLevelPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**EnvironmentLoggingLevel)(nil)).Elem()
}

func (o EnvironmentLoggingLevelPtrOutput) ToEnvironmentLoggingLevelPtrOutput() EnvironmentLoggingLevelPtrOutput {
	return o
}

func (o EnvironmentLoggingLevelPtrOutput) ToEnvironmentLoggingLevelPtrOutputWithContext(ctx context.Context) EnvironmentLoggingLevelPtrOutput {
	return o
}

func (o EnvironmentLoggingLevelPtrOutput) Elem() EnvironmentLoggingLevelOutput {
	return o.ApplyT(func(v *EnvironmentLoggingLevel) EnvironmentLoggingLevel {
		if v != nil {
			return *v
		}
		var ret EnvironmentLoggingLevel
		return ret
	}).(EnvironmentLoggingLevelOutput)
}

func (o EnvironmentLoggingLevelPtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o EnvironmentLoggingLevelPtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *EnvironmentLoggingLevel) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// EnvironmentLoggingLevelInput is an input type that accepts EnvironmentLoggingLevelArgs and EnvironmentLoggingLevelOutput values.
// You can construct a concrete instance of `EnvironmentLoggingLevelInput` via:
//
//	EnvironmentLoggingLevelArgs{...}
type EnvironmentLoggingLevelInput interface {
	pulumi.Input

	ToEnvironmentLoggingLevelOutput() EnvironmentLoggingLevelOutput
	ToEnvironmentLoggingLevelOutputWithContext(context.Context) EnvironmentLoggingLevelOutput
}

var environmentLoggingLevelPtrType = reflect.TypeOf((**EnvironmentLoggingLevel)(nil)).Elem()

type EnvironmentLoggingLevelPtrInput interface {
	pulumi.Input

	ToEnvironmentLoggingLevelPtrOutput() EnvironmentLoggingLevelPtrOutput
	ToEnvironmentLoggingLevelPtrOutputWithContext(context.Context) EnvironmentLoggingLevelPtrOutput
}

type environmentLoggingLevelPtr string

func EnvironmentLoggingLevelPtr(v string) EnvironmentLoggingLevelPtrInput {
	return (*environmentLoggingLevelPtr)(&v)
}

func (*environmentLoggingLevelPtr) ElementType() reflect.Type {
	return environmentLoggingLevelPtrType
}

func (in *environmentLoggingLevelPtr) ToEnvironmentLoggingLevelPtrOutput() EnvironmentLoggingLevelPtrOutput {
	return pulumi.ToOutput(in).(EnvironmentLoggingLevelPtrOutput)
}

func (in *environmentLoggingLevelPtr) ToEnvironmentLoggingLevelPtrOutputWithContext(ctx context.Context) EnvironmentLoggingLevelPtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(EnvironmentLoggingLevelPtrOutput)
}

// Choice for mode of webserver access including over public internet or via private VPC endpoint.
type EnvironmentWebserverAccessMode string

const (
	EnvironmentWebserverAccessModePrivateOnly = EnvironmentWebserverAccessMode("PRIVATE_ONLY")
	EnvironmentWebserverAccessModePublicOnly  = EnvironmentWebserverAccessMode("PUBLIC_ONLY")
)

func (EnvironmentWebserverAccessMode) ElementType() reflect.Type {
	return reflect.TypeOf((*EnvironmentWebserverAccessMode)(nil)).Elem()
}

func (e EnvironmentWebserverAccessMode) ToEnvironmentWebserverAccessModeOutput() EnvironmentWebserverAccessModeOutput {
	return pulumi.ToOutput(e).(EnvironmentWebserverAccessModeOutput)
}

func (e EnvironmentWebserverAccessMode) ToEnvironmentWebserverAccessModeOutputWithContext(ctx context.Context) EnvironmentWebserverAccessModeOutput {
	return pulumi.ToOutputWithContext(ctx, e).(EnvironmentWebserverAccessModeOutput)
}

func (e EnvironmentWebserverAccessMode) ToEnvironmentWebserverAccessModePtrOutput() EnvironmentWebserverAccessModePtrOutput {
	return e.ToEnvironmentWebserverAccessModePtrOutputWithContext(context.Background())
}

func (e EnvironmentWebserverAccessMode) ToEnvironmentWebserverAccessModePtrOutputWithContext(ctx context.Context) EnvironmentWebserverAccessModePtrOutput {
	return EnvironmentWebserverAccessMode(e).ToEnvironmentWebserverAccessModeOutputWithContext(ctx).ToEnvironmentWebserverAccessModePtrOutputWithContext(ctx)
}

func (e EnvironmentWebserverAccessMode) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e EnvironmentWebserverAccessMode) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e EnvironmentWebserverAccessMode) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e EnvironmentWebserverAccessMode) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type EnvironmentWebserverAccessModeOutput struct{ *pulumi.OutputState }

func (EnvironmentWebserverAccessModeOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*EnvironmentWebserverAccessMode)(nil)).Elem()
}

func (o EnvironmentWebserverAccessModeOutput) ToEnvironmentWebserverAccessModeOutput() EnvironmentWebserverAccessModeOutput {
	return o
}

func (o EnvironmentWebserverAccessModeOutput) ToEnvironmentWebserverAccessModeOutputWithContext(ctx context.Context) EnvironmentWebserverAccessModeOutput {
	return o
}

func (o EnvironmentWebserverAccessModeOutput) ToEnvironmentWebserverAccessModePtrOutput() EnvironmentWebserverAccessModePtrOutput {
	return o.ToEnvironmentWebserverAccessModePtrOutputWithContext(context.Background())
}

func (o EnvironmentWebserverAccessModeOutput) ToEnvironmentWebserverAccessModePtrOutputWithContext(ctx context.Context) EnvironmentWebserverAccessModePtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v EnvironmentWebserverAccessMode) *EnvironmentWebserverAccessMode {
		return &v
	}).(EnvironmentWebserverAccessModePtrOutput)
}

func (o EnvironmentWebserverAccessModeOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o EnvironmentWebserverAccessModeOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e EnvironmentWebserverAccessMode) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o EnvironmentWebserverAccessModeOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o EnvironmentWebserverAccessModeOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e EnvironmentWebserverAccessMode) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type EnvironmentWebserverAccessModePtrOutput struct{ *pulumi.OutputState }

func (EnvironmentWebserverAccessModePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**EnvironmentWebserverAccessMode)(nil)).Elem()
}

func (o EnvironmentWebserverAccessModePtrOutput) ToEnvironmentWebserverAccessModePtrOutput() EnvironmentWebserverAccessModePtrOutput {
	return o
}

func (o EnvironmentWebserverAccessModePtrOutput) ToEnvironmentWebserverAccessModePtrOutputWithContext(ctx context.Context) EnvironmentWebserverAccessModePtrOutput {
	return o
}

func (o EnvironmentWebserverAccessModePtrOutput) Elem() EnvironmentWebserverAccessModeOutput {
	return o.ApplyT(func(v *EnvironmentWebserverAccessMode) EnvironmentWebserverAccessMode {
		if v != nil {
			return *v
		}
		var ret EnvironmentWebserverAccessMode
		return ret
	}).(EnvironmentWebserverAccessModeOutput)
}

func (o EnvironmentWebserverAccessModePtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o EnvironmentWebserverAccessModePtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *EnvironmentWebserverAccessMode) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// EnvironmentWebserverAccessModeInput is an input type that accepts EnvironmentWebserverAccessModeArgs and EnvironmentWebserverAccessModeOutput values.
// You can construct a concrete instance of `EnvironmentWebserverAccessModeInput` via:
//
//	EnvironmentWebserverAccessModeArgs{...}
type EnvironmentWebserverAccessModeInput interface {
	pulumi.Input

	ToEnvironmentWebserverAccessModeOutput() EnvironmentWebserverAccessModeOutput
	ToEnvironmentWebserverAccessModeOutputWithContext(context.Context) EnvironmentWebserverAccessModeOutput
}

var environmentWebserverAccessModePtrType = reflect.TypeOf((**EnvironmentWebserverAccessMode)(nil)).Elem()

type EnvironmentWebserverAccessModePtrInput interface {
	pulumi.Input

	ToEnvironmentWebserverAccessModePtrOutput() EnvironmentWebserverAccessModePtrOutput
	ToEnvironmentWebserverAccessModePtrOutputWithContext(context.Context) EnvironmentWebserverAccessModePtrOutput
}

type environmentWebserverAccessModePtr string

func EnvironmentWebserverAccessModePtr(v string) EnvironmentWebserverAccessModePtrInput {
	return (*environmentWebserverAccessModePtr)(&v)
}

func (*environmentWebserverAccessModePtr) ElementType() reflect.Type {
	return environmentWebserverAccessModePtrType
}

func (in *environmentWebserverAccessModePtr) ToEnvironmentWebserverAccessModePtrOutput() EnvironmentWebserverAccessModePtrOutput {
	return pulumi.ToOutput(in).(EnvironmentWebserverAccessModePtrOutput)
}

func (in *environmentWebserverAccessModePtr) ToEnvironmentWebserverAccessModePtrOutputWithContext(ctx context.Context) EnvironmentWebserverAccessModePtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(EnvironmentWebserverAccessModePtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*EnvironmentLoggingLevelInput)(nil)).Elem(), EnvironmentLoggingLevel("CRITICAL"))
	pulumi.RegisterInputType(reflect.TypeOf((*EnvironmentLoggingLevelPtrInput)(nil)).Elem(), EnvironmentLoggingLevel("CRITICAL"))
	pulumi.RegisterInputType(reflect.TypeOf((*EnvironmentWebserverAccessModeInput)(nil)).Elem(), EnvironmentWebserverAccessMode("PRIVATE_ONLY"))
	pulumi.RegisterInputType(reflect.TypeOf((*EnvironmentWebserverAccessModePtrInput)(nil)).Elem(), EnvironmentWebserverAccessMode("PRIVATE_ONLY"))
	pulumi.RegisterOutputType(EnvironmentLoggingLevelOutput{})
	pulumi.RegisterOutputType(EnvironmentLoggingLevelPtrOutput{})
	pulumi.RegisterOutputType(EnvironmentWebserverAccessModeOutput{})
	pulumi.RegisterOutputType(EnvironmentWebserverAccessModePtrOutput{})
}
