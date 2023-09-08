// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package systemsmanagersap

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

type ApplicationCredentialCredentialType string

const (
	ApplicationCredentialCredentialTypeAdmin = ApplicationCredentialCredentialType("ADMIN")
)

func (ApplicationCredentialCredentialType) ElementType() reflect.Type {
	return reflect.TypeOf((*ApplicationCredentialCredentialType)(nil)).Elem()
}

func (e ApplicationCredentialCredentialType) ToApplicationCredentialCredentialTypeOutput() ApplicationCredentialCredentialTypeOutput {
	return pulumi.ToOutput(e).(ApplicationCredentialCredentialTypeOutput)
}

func (e ApplicationCredentialCredentialType) ToApplicationCredentialCredentialTypeOutputWithContext(ctx context.Context) ApplicationCredentialCredentialTypeOutput {
	return pulumi.ToOutputWithContext(ctx, e).(ApplicationCredentialCredentialTypeOutput)
}

func (e ApplicationCredentialCredentialType) ToApplicationCredentialCredentialTypePtrOutput() ApplicationCredentialCredentialTypePtrOutput {
	return e.ToApplicationCredentialCredentialTypePtrOutputWithContext(context.Background())
}

func (e ApplicationCredentialCredentialType) ToApplicationCredentialCredentialTypePtrOutputWithContext(ctx context.Context) ApplicationCredentialCredentialTypePtrOutput {
	return ApplicationCredentialCredentialType(e).ToApplicationCredentialCredentialTypeOutputWithContext(ctx).ToApplicationCredentialCredentialTypePtrOutputWithContext(ctx)
}

func (e ApplicationCredentialCredentialType) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e ApplicationCredentialCredentialType) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e ApplicationCredentialCredentialType) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e ApplicationCredentialCredentialType) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type ApplicationCredentialCredentialTypeOutput struct{ *pulumi.OutputState }

func (ApplicationCredentialCredentialTypeOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ApplicationCredentialCredentialType)(nil)).Elem()
}

func (o ApplicationCredentialCredentialTypeOutput) ToApplicationCredentialCredentialTypeOutput() ApplicationCredentialCredentialTypeOutput {
	return o
}

func (o ApplicationCredentialCredentialTypeOutput) ToApplicationCredentialCredentialTypeOutputWithContext(ctx context.Context) ApplicationCredentialCredentialTypeOutput {
	return o
}

func (o ApplicationCredentialCredentialTypeOutput) ToApplicationCredentialCredentialTypePtrOutput() ApplicationCredentialCredentialTypePtrOutput {
	return o.ToApplicationCredentialCredentialTypePtrOutputWithContext(context.Background())
}

func (o ApplicationCredentialCredentialTypeOutput) ToApplicationCredentialCredentialTypePtrOutputWithContext(ctx context.Context) ApplicationCredentialCredentialTypePtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v ApplicationCredentialCredentialType) *ApplicationCredentialCredentialType {
		return &v
	}).(ApplicationCredentialCredentialTypePtrOutput)
}

func (o ApplicationCredentialCredentialTypeOutput) ToOutput(ctx context.Context) pulumix.Output[ApplicationCredentialCredentialType] {
	return pulumix.Output[ApplicationCredentialCredentialType]{
		OutputState: o.OutputState,
	}
}

func (o ApplicationCredentialCredentialTypeOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o ApplicationCredentialCredentialTypeOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e ApplicationCredentialCredentialType) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o ApplicationCredentialCredentialTypeOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o ApplicationCredentialCredentialTypeOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e ApplicationCredentialCredentialType) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type ApplicationCredentialCredentialTypePtrOutput struct{ *pulumi.OutputState }

func (ApplicationCredentialCredentialTypePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ApplicationCredentialCredentialType)(nil)).Elem()
}

func (o ApplicationCredentialCredentialTypePtrOutput) ToApplicationCredentialCredentialTypePtrOutput() ApplicationCredentialCredentialTypePtrOutput {
	return o
}

func (o ApplicationCredentialCredentialTypePtrOutput) ToApplicationCredentialCredentialTypePtrOutputWithContext(ctx context.Context) ApplicationCredentialCredentialTypePtrOutput {
	return o
}

func (o ApplicationCredentialCredentialTypePtrOutput) ToOutput(ctx context.Context) pulumix.Output[*ApplicationCredentialCredentialType] {
	return pulumix.Output[*ApplicationCredentialCredentialType]{
		OutputState: o.OutputState,
	}
}

func (o ApplicationCredentialCredentialTypePtrOutput) Elem() ApplicationCredentialCredentialTypeOutput {
	return o.ApplyT(func(v *ApplicationCredentialCredentialType) ApplicationCredentialCredentialType {
		if v != nil {
			return *v
		}
		var ret ApplicationCredentialCredentialType
		return ret
	}).(ApplicationCredentialCredentialTypeOutput)
}

func (o ApplicationCredentialCredentialTypePtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o ApplicationCredentialCredentialTypePtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *ApplicationCredentialCredentialType) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// ApplicationCredentialCredentialTypeInput is an input type that accepts ApplicationCredentialCredentialTypeArgs and ApplicationCredentialCredentialTypeOutput values.
// You can construct a concrete instance of `ApplicationCredentialCredentialTypeInput` via:
//
//	ApplicationCredentialCredentialTypeArgs{...}
type ApplicationCredentialCredentialTypeInput interface {
	pulumi.Input

	ToApplicationCredentialCredentialTypeOutput() ApplicationCredentialCredentialTypeOutput
	ToApplicationCredentialCredentialTypeOutputWithContext(context.Context) ApplicationCredentialCredentialTypeOutput
}

var applicationCredentialCredentialTypePtrType = reflect.TypeOf((**ApplicationCredentialCredentialType)(nil)).Elem()

type ApplicationCredentialCredentialTypePtrInput interface {
	pulumi.Input

	ToApplicationCredentialCredentialTypePtrOutput() ApplicationCredentialCredentialTypePtrOutput
	ToApplicationCredentialCredentialTypePtrOutputWithContext(context.Context) ApplicationCredentialCredentialTypePtrOutput
}

type applicationCredentialCredentialTypePtr string

func ApplicationCredentialCredentialTypePtr(v string) ApplicationCredentialCredentialTypePtrInput {
	return (*applicationCredentialCredentialTypePtr)(&v)
}

func (*applicationCredentialCredentialTypePtr) ElementType() reflect.Type {
	return applicationCredentialCredentialTypePtrType
}

func (in *applicationCredentialCredentialTypePtr) ToApplicationCredentialCredentialTypePtrOutput() ApplicationCredentialCredentialTypePtrOutput {
	return pulumi.ToOutput(in).(ApplicationCredentialCredentialTypePtrOutput)
}

func (in *applicationCredentialCredentialTypePtr) ToApplicationCredentialCredentialTypePtrOutputWithContext(ctx context.Context) ApplicationCredentialCredentialTypePtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(ApplicationCredentialCredentialTypePtrOutput)
}

func (in *applicationCredentialCredentialTypePtr) ToOutput(ctx context.Context) pulumix.Output[*ApplicationCredentialCredentialType] {
	return pulumix.Output[*ApplicationCredentialCredentialType]{
		OutputState: in.ToApplicationCredentialCredentialTypePtrOutputWithContext(ctx).OutputState,
	}
}

type ApplicationType string

const (
	ApplicationTypeHana = ApplicationType("HANA")
)

func (ApplicationType) ElementType() reflect.Type {
	return reflect.TypeOf((*ApplicationType)(nil)).Elem()
}

func (e ApplicationType) ToApplicationTypeOutput() ApplicationTypeOutput {
	return pulumi.ToOutput(e).(ApplicationTypeOutput)
}

func (e ApplicationType) ToApplicationTypeOutputWithContext(ctx context.Context) ApplicationTypeOutput {
	return pulumi.ToOutputWithContext(ctx, e).(ApplicationTypeOutput)
}

func (e ApplicationType) ToApplicationTypePtrOutput() ApplicationTypePtrOutput {
	return e.ToApplicationTypePtrOutputWithContext(context.Background())
}

func (e ApplicationType) ToApplicationTypePtrOutputWithContext(ctx context.Context) ApplicationTypePtrOutput {
	return ApplicationType(e).ToApplicationTypeOutputWithContext(ctx).ToApplicationTypePtrOutputWithContext(ctx)
}

func (e ApplicationType) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e ApplicationType) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e ApplicationType) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e ApplicationType) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type ApplicationTypeOutput struct{ *pulumi.OutputState }

func (ApplicationTypeOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ApplicationType)(nil)).Elem()
}

func (o ApplicationTypeOutput) ToApplicationTypeOutput() ApplicationTypeOutput {
	return o
}

func (o ApplicationTypeOutput) ToApplicationTypeOutputWithContext(ctx context.Context) ApplicationTypeOutput {
	return o
}

func (o ApplicationTypeOutput) ToApplicationTypePtrOutput() ApplicationTypePtrOutput {
	return o.ToApplicationTypePtrOutputWithContext(context.Background())
}

func (o ApplicationTypeOutput) ToApplicationTypePtrOutputWithContext(ctx context.Context) ApplicationTypePtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v ApplicationType) *ApplicationType {
		return &v
	}).(ApplicationTypePtrOutput)
}

func (o ApplicationTypeOutput) ToOutput(ctx context.Context) pulumix.Output[ApplicationType] {
	return pulumix.Output[ApplicationType]{
		OutputState: o.OutputState,
	}
}

func (o ApplicationTypeOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o ApplicationTypeOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e ApplicationType) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o ApplicationTypeOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o ApplicationTypeOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e ApplicationType) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type ApplicationTypePtrOutput struct{ *pulumi.OutputState }

func (ApplicationTypePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ApplicationType)(nil)).Elem()
}

func (o ApplicationTypePtrOutput) ToApplicationTypePtrOutput() ApplicationTypePtrOutput {
	return o
}

func (o ApplicationTypePtrOutput) ToApplicationTypePtrOutputWithContext(ctx context.Context) ApplicationTypePtrOutput {
	return o
}

func (o ApplicationTypePtrOutput) ToOutput(ctx context.Context) pulumix.Output[*ApplicationType] {
	return pulumix.Output[*ApplicationType]{
		OutputState: o.OutputState,
	}
}

func (o ApplicationTypePtrOutput) Elem() ApplicationTypeOutput {
	return o.ApplyT(func(v *ApplicationType) ApplicationType {
		if v != nil {
			return *v
		}
		var ret ApplicationType
		return ret
	}).(ApplicationTypeOutput)
}

func (o ApplicationTypePtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o ApplicationTypePtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *ApplicationType) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// ApplicationTypeInput is an input type that accepts ApplicationTypeArgs and ApplicationTypeOutput values.
// You can construct a concrete instance of `ApplicationTypeInput` via:
//
//	ApplicationTypeArgs{...}
type ApplicationTypeInput interface {
	pulumi.Input

	ToApplicationTypeOutput() ApplicationTypeOutput
	ToApplicationTypeOutputWithContext(context.Context) ApplicationTypeOutput
}

var applicationTypePtrType = reflect.TypeOf((**ApplicationType)(nil)).Elem()

type ApplicationTypePtrInput interface {
	pulumi.Input

	ToApplicationTypePtrOutput() ApplicationTypePtrOutput
	ToApplicationTypePtrOutputWithContext(context.Context) ApplicationTypePtrOutput
}

type applicationTypePtr string

func ApplicationTypePtr(v string) ApplicationTypePtrInput {
	return (*applicationTypePtr)(&v)
}

func (*applicationTypePtr) ElementType() reflect.Type {
	return applicationTypePtrType
}

func (in *applicationTypePtr) ToApplicationTypePtrOutput() ApplicationTypePtrOutput {
	return pulumi.ToOutput(in).(ApplicationTypePtrOutput)
}

func (in *applicationTypePtr) ToApplicationTypePtrOutputWithContext(ctx context.Context) ApplicationTypePtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(ApplicationTypePtrOutput)
}

func (in *applicationTypePtr) ToOutput(ctx context.Context) pulumix.Output[*ApplicationType] {
	return pulumix.Output[*ApplicationType]{
		OutputState: in.ToApplicationTypePtrOutputWithContext(ctx).OutputState,
	}
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ApplicationCredentialCredentialTypeInput)(nil)).Elem(), ApplicationCredentialCredentialType("ADMIN"))
	pulumi.RegisterInputType(reflect.TypeOf((*ApplicationCredentialCredentialTypePtrInput)(nil)).Elem(), ApplicationCredentialCredentialType("ADMIN"))
	pulumi.RegisterInputType(reflect.TypeOf((*ApplicationTypeInput)(nil)).Elem(), ApplicationType("HANA"))
	pulumi.RegisterInputType(reflect.TypeOf((*ApplicationTypePtrInput)(nil)).Elem(), ApplicationType("HANA"))
	pulumi.RegisterOutputType(ApplicationCredentialCredentialTypeOutput{})
	pulumi.RegisterOutputType(ApplicationCredentialCredentialTypePtrOutput{})
	pulumi.RegisterOutputType(ApplicationTypeOutput{})
	pulumi.RegisterOutputType(ApplicationTypePtrOutput{})
}
