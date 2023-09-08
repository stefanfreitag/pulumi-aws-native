// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package proton

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

var _ = internal.GetEnvOrDefault

// <p>A description of a resource tag.</p>
type EnvironmentAccountConnectionTag struct {
	// <p>The key of the resource tag.</p>
	Key string `pulumi:"key"`
	// <p>The value of the resource tag.</p>
	Value string `pulumi:"value"`
}

// EnvironmentAccountConnectionTagInput is an input type that accepts EnvironmentAccountConnectionTagArgs and EnvironmentAccountConnectionTagOutput values.
// You can construct a concrete instance of `EnvironmentAccountConnectionTagInput` via:
//
//	EnvironmentAccountConnectionTagArgs{...}
type EnvironmentAccountConnectionTagInput interface {
	pulumi.Input

	ToEnvironmentAccountConnectionTagOutput() EnvironmentAccountConnectionTagOutput
	ToEnvironmentAccountConnectionTagOutputWithContext(context.Context) EnvironmentAccountConnectionTagOutput
}

// <p>A description of a resource tag.</p>
type EnvironmentAccountConnectionTagArgs struct {
	// <p>The key of the resource tag.</p>
	Key pulumi.StringInput `pulumi:"key"`
	// <p>The value of the resource tag.</p>
	Value pulumi.StringInput `pulumi:"value"`
}

func (EnvironmentAccountConnectionTagArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*EnvironmentAccountConnectionTag)(nil)).Elem()
}

func (i EnvironmentAccountConnectionTagArgs) ToEnvironmentAccountConnectionTagOutput() EnvironmentAccountConnectionTagOutput {
	return i.ToEnvironmentAccountConnectionTagOutputWithContext(context.Background())
}

func (i EnvironmentAccountConnectionTagArgs) ToEnvironmentAccountConnectionTagOutputWithContext(ctx context.Context) EnvironmentAccountConnectionTagOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EnvironmentAccountConnectionTagOutput)
}

func (i EnvironmentAccountConnectionTagArgs) ToOutput(ctx context.Context) pulumix.Output[EnvironmentAccountConnectionTag] {
	return pulumix.Output[EnvironmentAccountConnectionTag]{
		OutputState: i.ToEnvironmentAccountConnectionTagOutputWithContext(ctx).OutputState,
	}
}

// EnvironmentAccountConnectionTagArrayInput is an input type that accepts EnvironmentAccountConnectionTagArray and EnvironmentAccountConnectionTagArrayOutput values.
// You can construct a concrete instance of `EnvironmentAccountConnectionTagArrayInput` via:
//
//	EnvironmentAccountConnectionTagArray{ EnvironmentAccountConnectionTagArgs{...} }
type EnvironmentAccountConnectionTagArrayInput interface {
	pulumi.Input

	ToEnvironmentAccountConnectionTagArrayOutput() EnvironmentAccountConnectionTagArrayOutput
	ToEnvironmentAccountConnectionTagArrayOutputWithContext(context.Context) EnvironmentAccountConnectionTagArrayOutput
}

type EnvironmentAccountConnectionTagArray []EnvironmentAccountConnectionTagInput

func (EnvironmentAccountConnectionTagArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]EnvironmentAccountConnectionTag)(nil)).Elem()
}

func (i EnvironmentAccountConnectionTagArray) ToEnvironmentAccountConnectionTagArrayOutput() EnvironmentAccountConnectionTagArrayOutput {
	return i.ToEnvironmentAccountConnectionTagArrayOutputWithContext(context.Background())
}

func (i EnvironmentAccountConnectionTagArray) ToEnvironmentAccountConnectionTagArrayOutputWithContext(ctx context.Context) EnvironmentAccountConnectionTagArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EnvironmentAccountConnectionTagArrayOutput)
}

func (i EnvironmentAccountConnectionTagArray) ToOutput(ctx context.Context) pulumix.Output[[]EnvironmentAccountConnectionTag] {
	return pulumix.Output[[]EnvironmentAccountConnectionTag]{
		OutputState: i.ToEnvironmentAccountConnectionTagArrayOutputWithContext(ctx).OutputState,
	}
}

// <p>A description of a resource tag.</p>
type EnvironmentAccountConnectionTagOutput struct{ *pulumi.OutputState }

func (EnvironmentAccountConnectionTagOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*EnvironmentAccountConnectionTag)(nil)).Elem()
}

func (o EnvironmentAccountConnectionTagOutput) ToEnvironmentAccountConnectionTagOutput() EnvironmentAccountConnectionTagOutput {
	return o
}

func (o EnvironmentAccountConnectionTagOutput) ToEnvironmentAccountConnectionTagOutputWithContext(ctx context.Context) EnvironmentAccountConnectionTagOutput {
	return o
}

func (o EnvironmentAccountConnectionTagOutput) ToOutput(ctx context.Context) pulumix.Output[EnvironmentAccountConnectionTag] {
	return pulumix.Output[EnvironmentAccountConnectionTag]{
		OutputState: o.OutputState,
	}
}

// <p>The key of the resource tag.</p>
func (o EnvironmentAccountConnectionTagOutput) Key() pulumi.StringOutput {
	return o.ApplyT(func(v EnvironmentAccountConnectionTag) string { return v.Key }).(pulumi.StringOutput)
}

// <p>The value of the resource tag.</p>
func (o EnvironmentAccountConnectionTagOutput) Value() pulumi.StringOutput {
	return o.ApplyT(func(v EnvironmentAccountConnectionTag) string { return v.Value }).(pulumi.StringOutput)
}

type EnvironmentAccountConnectionTagArrayOutput struct{ *pulumi.OutputState }

func (EnvironmentAccountConnectionTagArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]EnvironmentAccountConnectionTag)(nil)).Elem()
}

func (o EnvironmentAccountConnectionTagArrayOutput) ToEnvironmentAccountConnectionTagArrayOutput() EnvironmentAccountConnectionTagArrayOutput {
	return o
}

func (o EnvironmentAccountConnectionTagArrayOutput) ToEnvironmentAccountConnectionTagArrayOutputWithContext(ctx context.Context) EnvironmentAccountConnectionTagArrayOutput {
	return o
}

func (o EnvironmentAccountConnectionTagArrayOutput) ToOutput(ctx context.Context) pulumix.Output[[]EnvironmentAccountConnectionTag] {
	return pulumix.Output[[]EnvironmentAccountConnectionTag]{
		OutputState: o.OutputState,
	}
}

func (o EnvironmentAccountConnectionTagArrayOutput) Index(i pulumi.IntInput) EnvironmentAccountConnectionTagOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) EnvironmentAccountConnectionTag {
		return vs[0].([]EnvironmentAccountConnectionTag)[vs[1].(int)]
	}).(EnvironmentAccountConnectionTagOutput)
}

// <p>A description of a resource tag.</p>
type EnvironmentTemplateTag struct {
	// <p>The key of the resource tag.</p>
	Key string `pulumi:"key"`
	// <p>The value of the resource tag.</p>
	Value string `pulumi:"value"`
}

// EnvironmentTemplateTagInput is an input type that accepts EnvironmentTemplateTagArgs and EnvironmentTemplateTagOutput values.
// You can construct a concrete instance of `EnvironmentTemplateTagInput` via:
//
//	EnvironmentTemplateTagArgs{...}
type EnvironmentTemplateTagInput interface {
	pulumi.Input

	ToEnvironmentTemplateTagOutput() EnvironmentTemplateTagOutput
	ToEnvironmentTemplateTagOutputWithContext(context.Context) EnvironmentTemplateTagOutput
}

// <p>A description of a resource tag.</p>
type EnvironmentTemplateTagArgs struct {
	// <p>The key of the resource tag.</p>
	Key pulumi.StringInput `pulumi:"key"`
	// <p>The value of the resource tag.</p>
	Value pulumi.StringInput `pulumi:"value"`
}

func (EnvironmentTemplateTagArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*EnvironmentTemplateTag)(nil)).Elem()
}

func (i EnvironmentTemplateTagArgs) ToEnvironmentTemplateTagOutput() EnvironmentTemplateTagOutput {
	return i.ToEnvironmentTemplateTagOutputWithContext(context.Background())
}

func (i EnvironmentTemplateTagArgs) ToEnvironmentTemplateTagOutputWithContext(ctx context.Context) EnvironmentTemplateTagOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EnvironmentTemplateTagOutput)
}

func (i EnvironmentTemplateTagArgs) ToOutput(ctx context.Context) pulumix.Output[EnvironmentTemplateTag] {
	return pulumix.Output[EnvironmentTemplateTag]{
		OutputState: i.ToEnvironmentTemplateTagOutputWithContext(ctx).OutputState,
	}
}

// EnvironmentTemplateTagArrayInput is an input type that accepts EnvironmentTemplateTagArray and EnvironmentTemplateTagArrayOutput values.
// You can construct a concrete instance of `EnvironmentTemplateTagArrayInput` via:
//
//	EnvironmentTemplateTagArray{ EnvironmentTemplateTagArgs{...} }
type EnvironmentTemplateTagArrayInput interface {
	pulumi.Input

	ToEnvironmentTemplateTagArrayOutput() EnvironmentTemplateTagArrayOutput
	ToEnvironmentTemplateTagArrayOutputWithContext(context.Context) EnvironmentTemplateTagArrayOutput
}

type EnvironmentTemplateTagArray []EnvironmentTemplateTagInput

func (EnvironmentTemplateTagArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]EnvironmentTemplateTag)(nil)).Elem()
}

func (i EnvironmentTemplateTagArray) ToEnvironmentTemplateTagArrayOutput() EnvironmentTemplateTagArrayOutput {
	return i.ToEnvironmentTemplateTagArrayOutputWithContext(context.Background())
}

func (i EnvironmentTemplateTagArray) ToEnvironmentTemplateTagArrayOutputWithContext(ctx context.Context) EnvironmentTemplateTagArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EnvironmentTemplateTagArrayOutput)
}

func (i EnvironmentTemplateTagArray) ToOutput(ctx context.Context) pulumix.Output[[]EnvironmentTemplateTag] {
	return pulumix.Output[[]EnvironmentTemplateTag]{
		OutputState: i.ToEnvironmentTemplateTagArrayOutputWithContext(ctx).OutputState,
	}
}

// <p>A description of a resource tag.</p>
type EnvironmentTemplateTagOutput struct{ *pulumi.OutputState }

func (EnvironmentTemplateTagOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*EnvironmentTemplateTag)(nil)).Elem()
}

func (o EnvironmentTemplateTagOutput) ToEnvironmentTemplateTagOutput() EnvironmentTemplateTagOutput {
	return o
}

func (o EnvironmentTemplateTagOutput) ToEnvironmentTemplateTagOutputWithContext(ctx context.Context) EnvironmentTemplateTagOutput {
	return o
}

func (o EnvironmentTemplateTagOutput) ToOutput(ctx context.Context) pulumix.Output[EnvironmentTemplateTag] {
	return pulumix.Output[EnvironmentTemplateTag]{
		OutputState: o.OutputState,
	}
}

// <p>The key of the resource tag.</p>
func (o EnvironmentTemplateTagOutput) Key() pulumi.StringOutput {
	return o.ApplyT(func(v EnvironmentTemplateTag) string { return v.Key }).(pulumi.StringOutput)
}

// <p>The value of the resource tag.</p>
func (o EnvironmentTemplateTagOutput) Value() pulumi.StringOutput {
	return o.ApplyT(func(v EnvironmentTemplateTag) string { return v.Value }).(pulumi.StringOutput)
}

type EnvironmentTemplateTagArrayOutput struct{ *pulumi.OutputState }

func (EnvironmentTemplateTagArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]EnvironmentTemplateTag)(nil)).Elem()
}

func (o EnvironmentTemplateTagArrayOutput) ToEnvironmentTemplateTagArrayOutput() EnvironmentTemplateTagArrayOutput {
	return o
}

func (o EnvironmentTemplateTagArrayOutput) ToEnvironmentTemplateTagArrayOutputWithContext(ctx context.Context) EnvironmentTemplateTagArrayOutput {
	return o
}

func (o EnvironmentTemplateTagArrayOutput) ToOutput(ctx context.Context) pulumix.Output[[]EnvironmentTemplateTag] {
	return pulumix.Output[[]EnvironmentTemplateTag]{
		OutputState: o.OutputState,
	}
}

func (o EnvironmentTemplateTagArrayOutput) Index(i pulumi.IntInput) EnvironmentTemplateTagOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) EnvironmentTemplateTag {
		return vs[0].([]EnvironmentTemplateTag)[vs[1].(int)]
	}).(EnvironmentTemplateTagOutput)
}

// <p>A description of a resource tag.</p>
type ServiceTemplateTag struct {
	// <p>The key of the resource tag.</p>
	Key string `pulumi:"key"`
	// <p>The value of the resource tag.</p>
	Value string `pulumi:"value"`
}

// ServiceTemplateTagInput is an input type that accepts ServiceTemplateTagArgs and ServiceTemplateTagOutput values.
// You can construct a concrete instance of `ServiceTemplateTagInput` via:
//
//	ServiceTemplateTagArgs{...}
type ServiceTemplateTagInput interface {
	pulumi.Input

	ToServiceTemplateTagOutput() ServiceTemplateTagOutput
	ToServiceTemplateTagOutputWithContext(context.Context) ServiceTemplateTagOutput
}

// <p>A description of a resource tag.</p>
type ServiceTemplateTagArgs struct {
	// <p>The key of the resource tag.</p>
	Key pulumi.StringInput `pulumi:"key"`
	// <p>The value of the resource tag.</p>
	Value pulumi.StringInput `pulumi:"value"`
}

func (ServiceTemplateTagArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ServiceTemplateTag)(nil)).Elem()
}

func (i ServiceTemplateTagArgs) ToServiceTemplateTagOutput() ServiceTemplateTagOutput {
	return i.ToServiceTemplateTagOutputWithContext(context.Background())
}

func (i ServiceTemplateTagArgs) ToServiceTemplateTagOutputWithContext(ctx context.Context) ServiceTemplateTagOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ServiceTemplateTagOutput)
}

func (i ServiceTemplateTagArgs) ToOutput(ctx context.Context) pulumix.Output[ServiceTemplateTag] {
	return pulumix.Output[ServiceTemplateTag]{
		OutputState: i.ToServiceTemplateTagOutputWithContext(ctx).OutputState,
	}
}

// ServiceTemplateTagArrayInput is an input type that accepts ServiceTemplateTagArray and ServiceTemplateTagArrayOutput values.
// You can construct a concrete instance of `ServiceTemplateTagArrayInput` via:
//
//	ServiceTemplateTagArray{ ServiceTemplateTagArgs{...} }
type ServiceTemplateTagArrayInput interface {
	pulumi.Input

	ToServiceTemplateTagArrayOutput() ServiceTemplateTagArrayOutput
	ToServiceTemplateTagArrayOutputWithContext(context.Context) ServiceTemplateTagArrayOutput
}

type ServiceTemplateTagArray []ServiceTemplateTagInput

func (ServiceTemplateTagArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]ServiceTemplateTag)(nil)).Elem()
}

func (i ServiceTemplateTagArray) ToServiceTemplateTagArrayOutput() ServiceTemplateTagArrayOutput {
	return i.ToServiceTemplateTagArrayOutputWithContext(context.Background())
}

func (i ServiceTemplateTagArray) ToServiceTemplateTagArrayOutputWithContext(ctx context.Context) ServiceTemplateTagArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ServiceTemplateTagArrayOutput)
}

func (i ServiceTemplateTagArray) ToOutput(ctx context.Context) pulumix.Output[[]ServiceTemplateTag] {
	return pulumix.Output[[]ServiceTemplateTag]{
		OutputState: i.ToServiceTemplateTagArrayOutputWithContext(ctx).OutputState,
	}
}

// <p>A description of a resource tag.</p>
type ServiceTemplateTagOutput struct{ *pulumi.OutputState }

func (ServiceTemplateTagOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ServiceTemplateTag)(nil)).Elem()
}

func (o ServiceTemplateTagOutput) ToServiceTemplateTagOutput() ServiceTemplateTagOutput {
	return o
}

func (o ServiceTemplateTagOutput) ToServiceTemplateTagOutputWithContext(ctx context.Context) ServiceTemplateTagOutput {
	return o
}

func (o ServiceTemplateTagOutput) ToOutput(ctx context.Context) pulumix.Output[ServiceTemplateTag] {
	return pulumix.Output[ServiceTemplateTag]{
		OutputState: o.OutputState,
	}
}

// <p>The key of the resource tag.</p>
func (o ServiceTemplateTagOutput) Key() pulumi.StringOutput {
	return o.ApplyT(func(v ServiceTemplateTag) string { return v.Key }).(pulumi.StringOutput)
}

// <p>The value of the resource tag.</p>
func (o ServiceTemplateTagOutput) Value() pulumi.StringOutput {
	return o.ApplyT(func(v ServiceTemplateTag) string { return v.Value }).(pulumi.StringOutput)
}

type ServiceTemplateTagArrayOutput struct{ *pulumi.OutputState }

func (ServiceTemplateTagArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]ServiceTemplateTag)(nil)).Elem()
}

func (o ServiceTemplateTagArrayOutput) ToServiceTemplateTagArrayOutput() ServiceTemplateTagArrayOutput {
	return o
}

func (o ServiceTemplateTagArrayOutput) ToServiceTemplateTagArrayOutputWithContext(ctx context.Context) ServiceTemplateTagArrayOutput {
	return o
}

func (o ServiceTemplateTagArrayOutput) ToOutput(ctx context.Context) pulumix.Output[[]ServiceTemplateTag] {
	return pulumix.Output[[]ServiceTemplateTag]{
		OutputState: o.OutputState,
	}
}

func (o ServiceTemplateTagArrayOutput) Index(i pulumi.IntInput) ServiceTemplateTagOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) ServiceTemplateTag {
		return vs[0].([]ServiceTemplateTag)[vs[1].(int)]
	}).(ServiceTemplateTagOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*EnvironmentAccountConnectionTagInput)(nil)).Elem(), EnvironmentAccountConnectionTagArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*EnvironmentAccountConnectionTagArrayInput)(nil)).Elem(), EnvironmentAccountConnectionTagArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*EnvironmentTemplateTagInput)(nil)).Elem(), EnvironmentTemplateTagArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*EnvironmentTemplateTagArrayInput)(nil)).Elem(), EnvironmentTemplateTagArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*ServiceTemplateTagInput)(nil)).Elem(), ServiceTemplateTagArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*ServiceTemplateTagArrayInput)(nil)).Elem(), ServiceTemplateTagArray{})
	pulumi.RegisterOutputType(EnvironmentAccountConnectionTagOutput{})
	pulumi.RegisterOutputType(EnvironmentAccountConnectionTagArrayOutput{})
	pulumi.RegisterOutputType(EnvironmentTemplateTagOutput{})
	pulumi.RegisterOutputType(EnvironmentTemplateTagArrayOutput{})
	pulumi.RegisterOutputType(ServiceTemplateTagOutput{})
	pulumi.RegisterOutputType(ServiceTemplateTagArrayOutput{})
}
