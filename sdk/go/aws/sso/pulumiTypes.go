// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sso

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type InstanceAccessControlAttributeConfigurationAccessControlAttribute struct {
	Key   string                                                                 `pulumi:"key"`
	Value InstanceAccessControlAttributeConfigurationAccessControlAttributeValue `pulumi:"value"`
}

// InstanceAccessControlAttributeConfigurationAccessControlAttributeInput is an input type that accepts InstanceAccessControlAttributeConfigurationAccessControlAttributeArgs and InstanceAccessControlAttributeConfigurationAccessControlAttributeOutput values.
// You can construct a concrete instance of `InstanceAccessControlAttributeConfigurationAccessControlAttributeInput` via:
//
//          InstanceAccessControlAttributeConfigurationAccessControlAttributeArgs{...}
type InstanceAccessControlAttributeConfigurationAccessControlAttributeInput interface {
	pulumi.Input

	ToInstanceAccessControlAttributeConfigurationAccessControlAttributeOutput() InstanceAccessControlAttributeConfigurationAccessControlAttributeOutput
	ToInstanceAccessControlAttributeConfigurationAccessControlAttributeOutputWithContext(context.Context) InstanceAccessControlAttributeConfigurationAccessControlAttributeOutput
}

type InstanceAccessControlAttributeConfigurationAccessControlAttributeArgs struct {
	Key   pulumi.StringInput                                                          `pulumi:"key"`
	Value InstanceAccessControlAttributeConfigurationAccessControlAttributeValueInput `pulumi:"value"`
}

func (InstanceAccessControlAttributeConfigurationAccessControlAttributeArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*InstanceAccessControlAttributeConfigurationAccessControlAttribute)(nil)).Elem()
}

func (i InstanceAccessControlAttributeConfigurationAccessControlAttributeArgs) ToInstanceAccessControlAttributeConfigurationAccessControlAttributeOutput() InstanceAccessControlAttributeConfigurationAccessControlAttributeOutput {
	return i.ToInstanceAccessControlAttributeConfigurationAccessControlAttributeOutputWithContext(context.Background())
}

func (i InstanceAccessControlAttributeConfigurationAccessControlAttributeArgs) ToInstanceAccessControlAttributeConfigurationAccessControlAttributeOutputWithContext(ctx context.Context) InstanceAccessControlAttributeConfigurationAccessControlAttributeOutput {
	return pulumi.ToOutputWithContext(ctx, i).(InstanceAccessControlAttributeConfigurationAccessControlAttributeOutput)
}

// InstanceAccessControlAttributeConfigurationAccessControlAttributeArrayInput is an input type that accepts InstanceAccessControlAttributeConfigurationAccessControlAttributeArray and InstanceAccessControlAttributeConfigurationAccessControlAttributeArrayOutput values.
// You can construct a concrete instance of `InstanceAccessControlAttributeConfigurationAccessControlAttributeArrayInput` via:
//
//          InstanceAccessControlAttributeConfigurationAccessControlAttributeArray{ InstanceAccessControlAttributeConfigurationAccessControlAttributeArgs{...} }
type InstanceAccessControlAttributeConfigurationAccessControlAttributeArrayInput interface {
	pulumi.Input

	ToInstanceAccessControlAttributeConfigurationAccessControlAttributeArrayOutput() InstanceAccessControlAttributeConfigurationAccessControlAttributeArrayOutput
	ToInstanceAccessControlAttributeConfigurationAccessControlAttributeArrayOutputWithContext(context.Context) InstanceAccessControlAttributeConfigurationAccessControlAttributeArrayOutput
}

type InstanceAccessControlAttributeConfigurationAccessControlAttributeArray []InstanceAccessControlAttributeConfigurationAccessControlAttributeInput

func (InstanceAccessControlAttributeConfigurationAccessControlAttributeArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]InstanceAccessControlAttributeConfigurationAccessControlAttribute)(nil)).Elem()
}

func (i InstanceAccessControlAttributeConfigurationAccessControlAttributeArray) ToInstanceAccessControlAttributeConfigurationAccessControlAttributeArrayOutput() InstanceAccessControlAttributeConfigurationAccessControlAttributeArrayOutput {
	return i.ToInstanceAccessControlAttributeConfigurationAccessControlAttributeArrayOutputWithContext(context.Background())
}

func (i InstanceAccessControlAttributeConfigurationAccessControlAttributeArray) ToInstanceAccessControlAttributeConfigurationAccessControlAttributeArrayOutputWithContext(ctx context.Context) InstanceAccessControlAttributeConfigurationAccessControlAttributeArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(InstanceAccessControlAttributeConfigurationAccessControlAttributeArrayOutput)
}

type InstanceAccessControlAttributeConfigurationAccessControlAttributeOutput struct{ *pulumi.OutputState }

func (InstanceAccessControlAttributeConfigurationAccessControlAttributeOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*InstanceAccessControlAttributeConfigurationAccessControlAttribute)(nil)).Elem()
}

func (o InstanceAccessControlAttributeConfigurationAccessControlAttributeOutput) ToInstanceAccessControlAttributeConfigurationAccessControlAttributeOutput() InstanceAccessControlAttributeConfigurationAccessControlAttributeOutput {
	return o
}

func (o InstanceAccessControlAttributeConfigurationAccessControlAttributeOutput) ToInstanceAccessControlAttributeConfigurationAccessControlAttributeOutputWithContext(ctx context.Context) InstanceAccessControlAttributeConfigurationAccessControlAttributeOutput {
	return o
}

func (o InstanceAccessControlAttributeConfigurationAccessControlAttributeOutput) Key() pulumi.StringOutput {
	return o.ApplyT(func(v InstanceAccessControlAttributeConfigurationAccessControlAttribute) string { return v.Key }).(pulumi.StringOutput)
}

func (o InstanceAccessControlAttributeConfigurationAccessControlAttributeOutput) Value() InstanceAccessControlAttributeConfigurationAccessControlAttributeValueOutput {
	return o.ApplyT(func(v InstanceAccessControlAttributeConfigurationAccessControlAttribute) InstanceAccessControlAttributeConfigurationAccessControlAttributeValue {
		return v.Value
	}).(InstanceAccessControlAttributeConfigurationAccessControlAttributeValueOutput)
}

type InstanceAccessControlAttributeConfigurationAccessControlAttributeArrayOutput struct{ *pulumi.OutputState }

func (InstanceAccessControlAttributeConfigurationAccessControlAttributeArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]InstanceAccessControlAttributeConfigurationAccessControlAttribute)(nil)).Elem()
}

func (o InstanceAccessControlAttributeConfigurationAccessControlAttributeArrayOutput) ToInstanceAccessControlAttributeConfigurationAccessControlAttributeArrayOutput() InstanceAccessControlAttributeConfigurationAccessControlAttributeArrayOutput {
	return o
}

func (o InstanceAccessControlAttributeConfigurationAccessControlAttributeArrayOutput) ToInstanceAccessControlAttributeConfigurationAccessControlAttributeArrayOutputWithContext(ctx context.Context) InstanceAccessControlAttributeConfigurationAccessControlAttributeArrayOutput {
	return o
}

func (o InstanceAccessControlAttributeConfigurationAccessControlAttributeArrayOutput) Index(i pulumi.IntInput) InstanceAccessControlAttributeConfigurationAccessControlAttributeOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) InstanceAccessControlAttributeConfigurationAccessControlAttribute {
		return vs[0].([]InstanceAccessControlAttributeConfigurationAccessControlAttribute)[vs[1].(int)]
	}).(InstanceAccessControlAttributeConfigurationAccessControlAttributeOutput)
}

type InstanceAccessControlAttributeConfigurationAccessControlAttributeValue struct {
	Source []string `pulumi:"source"`
}

// InstanceAccessControlAttributeConfigurationAccessControlAttributeValueInput is an input type that accepts InstanceAccessControlAttributeConfigurationAccessControlAttributeValueArgs and InstanceAccessControlAttributeConfigurationAccessControlAttributeValueOutput values.
// You can construct a concrete instance of `InstanceAccessControlAttributeConfigurationAccessControlAttributeValueInput` via:
//
//          InstanceAccessControlAttributeConfigurationAccessControlAttributeValueArgs{...}
type InstanceAccessControlAttributeConfigurationAccessControlAttributeValueInput interface {
	pulumi.Input

	ToInstanceAccessControlAttributeConfigurationAccessControlAttributeValueOutput() InstanceAccessControlAttributeConfigurationAccessControlAttributeValueOutput
	ToInstanceAccessControlAttributeConfigurationAccessControlAttributeValueOutputWithContext(context.Context) InstanceAccessControlAttributeConfigurationAccessControlAttributeValueOutput
}

type InstanceAccessControlAttributeConfigurationAccessControlAttributeValueArgs struct {
	Source pulumi.StringArrayInput `pulumi:"source"`
}

func (InstanceAccessControlAttributeConfigurationAccessControlAttributeValueArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*InstanceAccessControlAttributeConfigurationAccessControlAttributeValue)(nil)).Elem()
}

func (i InstanceAccessControlAttributeConfigurationAccessControlAttributeValueArgs) ToInstanceAccessControlAttributeConfigurationAccessControlAttributeValueOutput() InstanceAccessControlAttributeConfigurationAccessControlAttributeValueOutput {
	return i.ToInstanceAccessControlAttributeConfigurationAccessControlAttributeValueOutputWithContext(context.Background())
}

func (i InstanceAccessControlAttributeConfigurationAccessControlAttributeValueArgs) ToInstanceAccessControlAttributeConfigurationAccessControlAttributeValueOutputWithContext(ctx context.Context) InstanceAccessControlAttributeConfigurationAccessControlAttributeValueOutput {
	return pulumi.ToOutputWithContext(ctx, i).(InstanceAccessControlAttributeConfigurationAccessControlAttributeValueOutput)
}

type InstanceAccessControlAttributeConfigurationAccessControlAttributeValueOutput struct{ *pulumi.OutputState }

func (InstanceAccessControlAttributeConfigurationAccessControlAttributeValueOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*InstanceAccessControlAttributeConfigurationAccessControlAttributeValue)(nil)).Elem()
}

func (o InstanceAccessControlAttributeConfigurationAccessControlAttributeValueOutput) ToInstanceAccessControlAttributeConfigurationAccessControlAttributeValueOutput() InstanceAccessControlAttributeConfigurationAccessControlAttributeValueOutput {
	return o
}

func (o InstanceAccessControlAttributeConfigurationAccessControlAttributeValueOutput) ToInstanceAccessControlAttributeConfigurationAccessControlAttributeValueOutputWithContext(ctx context.Context) InstanceAccessControlAttributeConfigurationAccessControlAttributeValueOutput {
	return o
}

func (o InstanceAccessControlAttributeConfigurationAccessControlAttributeValueOutput) Source() pulumi.StringArrayOutput {
	return o.ApplyT(func(v InstanceAccessControlAttributeConfigurationAccessControlAttributeValue) []string {
		return v.Source
	}).(pulumi.StringArrayOutput)
}

// The InstanceAccessControlAttributeConfiguration property has been deprecated but is still supported for backwards compatibility purposes. We recomend that you use  AccessControlAttributes property instead.
type InstanceAccessControlAttributeConfigurationProperties struct {
	AccessControlAttributes []InstanceAccessControlAttributeConfigurationAccessControlAttribute `pulumi:"accessControlAttributes"`
}

// InstanceAccessControlAttributeConfigurationPropertiesInput is an input type that accepts InstanceAccessControlAttributeConfigurationPropertiesArgs and InstanceAccessControlAttributeConfigurationPropertiesOutput values.
// You can construct a concrete instance of `InstanceAccessControlAttributeConfigurationPropertiesInput` via:
//
//          InstanceAccessControlAttributeConfigurationPropertiesArgs{...}
type InstanceAccessControlAttributeConfigurationPropertiesInput interface {
	pulumi.Input

	ToInstanceAccessControlAttributeConfigurationPropertiesOutput() InstanceAccessControlAttributeConfigurationPropertiesOutput
	ToInstanceAccessControlAttributeConfigurationPropertiesOutputWithContext(context.Context) InstanceAccessControlAttributeConfigurationPropertiesOutput
}

// The InstanceAccessControlAttributeConfiguration property has been deprecated but is still supported for backwards compatibility purposes. We recomend that you use  AccessControlAttributes property instead.
type InstanceAccessControlAttributeConfigurationPropertiesArgs struct {
	AccessControlAttributes InstanceAccessControlAttributeConfigurationAccessControlAttributeArrayInput `pulumi:"accessControlAttributes"`
}

func (InstanceAccessControlAttributeConfigurationPropertiesArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*InstanceAccessControlAttributeConfigurationProperties)(nil)).Elem()
}

func (i InstanceAccessControlAttributeConfigurationPropertiesArgs) ToInstanceAccessControlAttributeConfigurationPropertiesOutput() InstanceAccessControlAttributeConfigurationPropertiesOutput {
	return i.ToInstanceAccessControlAttributeConfigurationPropertiesOutputWithContext(context.Background())
}

func (i InstanceAccessControlAttributeConfigurationPropertiesArgs) ToInstanceAccessControlAttributeConfigurationPropertiesOutputWithContext(ctx context.Context) InstanceAccessControlAttributeConfigurationPropertiesOutput {
	return pulumi.ToOutputWithContext(ctx, i).(InstanceAccessControlAttributeConfigurationPropertiesOutput)
}

func (i InstanceAccessControlAttributeConfigurationPropertiesArgs) ToInstanceAccessControlAttributeConfigurationPropertiesPtrOutput() InstanceAccessControlAttributeConfigurationPropertiesPtrOutput {
	return i.ToInstanceAccessControlAttributeConfigurationPropertiesPtrOutputWithContext(context.Background())
}

func (i InstanceAccessControlAttributeConfigurationPropertiesArgs) ToInstanceAccessControlAttributeConfigurationPropertiesPtrOutputWithContext(ctx context.Context) InstanceAccessControlAttributeConfigurationPropertiesPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(InstanceAccessControlAttributeConfigurationPropertiesOutput).ToInstanceAccessControlAttributeConfigurationPropertiesPtrOutputWithContext(ctx)
}

// InstanceAccessControlAttributeConfigurationPropertiesPtrInput is an input type that accepts InstanceAccessControlAttributeConfigurationPropertiesArgs, InstanceAccessControlAttributeConfigurationPropertiesPtr and InstanceAccessControlAttributeConfigurationPropertiesPtrOutput values.
// You can construct a concrete instance of `InstanceAccessControlAttributeConfigurationPropertiesPtrInput` via:
//
//          InstanceAccessControlAttributeConfigurationPropertiesArgs{...}
//
//  or:
//
//          nil
type InstanceAccessControlAttributeConfigurationPropertiesPtrInput interface {
	pulumi.Input

	ToInstanceAccessControlAttributeConfigurationPropertiesPtrOutput() InstanceAccessControlAttributeConfigurationPropertiesPtrOutput
	ToInstanceAccessControlAttributeConfigurationPropertiesPtrOutputWithContext(context.Context) InstanceAccessControlAttributeConfigurationPropertiesPtrOutput
}

type instanceAccessControlAttributeConfigurationPropertiesPtrType InstanceAccessControlAttributeConfigurationPropertiesArgs

func InstanceAccessControlAttributeConfigurationPropertiesPtr(v *InstanceAccessControlAttributeConfigurationPropertiesArgs) InstanceAccessControlAttributeConfigurationPropertiesPtrInput {
	return (*instanceAccessControlAttributeConfigurationPropertiesPtrType)(v)
}

func (*instanceAccessControlAttributeConfigurationPropertiesPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**InstanceAccessControlAttributeConfigurationProperties)(nil)).Elem()
}

func (i *instanceAccessControlAttributeConfigurationPropertiesPtrType) ToInstanceAccessControlAttributeConfigurationPropertiesPtrOutput() InstanceAccessControlAttributeConfigurationPropertiesPtrOutput {
	return i.ToInstanceAccessControlAttributeConfigurationPropertiesPtrOutputWithContext(context.Background())
}

func (i *instanceAccessControlAttributeConfigurationPropertiesPtrType) ToInstanceAccessControlAttributeConfigurationPropertiesPtrOutputWithContext(ctx context.Context) InstanceAccessControlAttributeConfigurationPropertiesPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(InstanceAccessControlAttributeConfigurationPropertiesPtrOutput)
}

// The InstanceAccessControlAttributeConfiguration property has been deprecated but is still supported for backwards compatibility purposes. We recomend that you use  AccessControlAttributes property instead.
type InstanceAccessControlAttributeConfigurationPropertiesOutput struct{ *pulumi.OutputState }

func (InstanceAccessControlAttributeConfigurationPropertiesOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*InstanceAccessControlAttributeConfigurationProperties)(nil)).Elem()
}

func (o InstanceAccessControlAttributeConfigurationPropertiesOutput) ToInstanceAccessControlAttributeConfigurationPropertiesOutput() InstanceAccessControlAttributeConfigurationPropertiesOutput {
	return o
}

func (o InstanceAccessControlAttributeConfigurationPropertiesOutput) ToInstanceAccessControlAttributeConfigurationPropertiesOutputWithContext(ctx context.Context) InstanceAccessControlAttributeConfigurationPropertiesOutput {
	return o
}

func (o InstanceAccessControlAttributeConfigurationPropertiesOutput) ToInstanceAccessControlAttributeConfigurationPropertiesPtrOutput() InstanceAccessControlAttributeConfigurationPropertiesPtrOutput {
	return o.ToInstanceAccessControlAttributeConfigurationPropertiesPtrOutputWithContext(context.Background())
}

func (o InstanceAccessControlAttributeConfigurationPropertiesOutput) ToInstanceAccessControlAttributeConfigurationPropertiesPtrOutputWithContext(ctx context.Context) InstanceAccessControlAttributeConfigurationPropertiesPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v InstanceAccessControlAttributeConfigurationProperties) *InstanceAccessControlAttributeConfigurationProperties {
		return &v
	}).(InstanceAccessControlAttributeConfigurationPropertiesPtrOutput)
}

func (o InstanceAccessControlAttributeConfigurationPropertiesOutput) AccessControlAttributes() InstanceAccessControlAttributeConfigurationAccessControlAttributeArrayOutput {
	return o.ApplyT(func(v InstanceAccessControlAttributeConfigurationProperties) []InstanceAccessControlAttributeConfigurationAccessControlAttribute {
		return v.AccessControlAttributes
	}).(InstanceAccessControlAttributeConfigurationAccessControlAttributeArrayOutput)
}

type InstanceAccessControlAttributeConfigurationPropertiesPtrOutput struct{ *pulumi.OutputState }

func (InstanceAccessControlAttributeConfigurationPropertiesPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**InstanceAccessControlAttributeConfigurationProperties)(nil)).Elem()
}

func (o InstanceAccessControlAttributeConfigurationPropertiesPtrOutput) ToInstanceAccessControlAttributeConfigurationPropertiesPtrOutput() InstanceAccessControlAttributeConfigurationPropertiesPtrOutput {
	return o
}

func (o InstanceAccessControlAttributeConfigurationPropertiesPtrOutput) ToInstanceAccessControlAttributeConfigurationPropertiesPtrOutputWithContext(ctx context.Context) InstanceAccessControlAttributeConfigurationPropertiesPtrOutput {
	return o
}

func (o InstanceAccessControlAttributeConfigurationPropertiesPtrOutput) Elem() InstanceAccessControlAttributeConfigurationPropertiesOutput {
	return o.ApplyT(func(v *InstanceAccessControlAttributeConfigurationProperties) InstanceAccessControlAttributeConfigurationProperties {
		if v != nil {
			return *v
		}
		var ret InstanceAccessControlAttributeConfigurationProperties
		return ret
	}).(InstanceAccessControlAttributeConfigurationPropertiesOutput)
}

func (o InstanceAccessControlAttributeConfigurationPropertiesPtrOutput) AccessControlAttributes() InstanceAccessControlAttributeConfigurationAccessControlAttributeArrayOutput {
	return o.ApplyT(func(v *InstanceAccessControlAttributeConfigurationProperties) []InstanceAccessControlAttributeConfigurationAccessControlAttribute {
		if v == nil {
			return nil
		}
		return v.AccessControlAttributes
	}).(InstanceAccessControlAttributeConfigurationAccessControlAttributeArrayOutput)
}

// The metadata that you apply to the permission set to help you categorize and organize them.
type PermissionSetTag struct {
	Key   string `pulumi:"key"`
	Value string `pulumi:"value"`
}

// PermissionSetTagInput is an input type that accepts PermissionSetTagArgs and PermissionSetTagOutput values.
// You can construct a concrete instance of `PermissionSetTagInput` via:
//
//          PermissionSetTagArgs{...}
type PermissionSetTagInput interface {
	pulumi.Input

	ToPermissionSetTagOutput() PermissionSetTagOutput
	ToPermissionSetTagOutputWithContext(context.Context) PermissionSetTagOutput
}

// The metadata that you apply to the permission set to help you categorize and organize them.
type PermissionSetTagArgs struct {
	Key   pulumi.StringInput `pulumi:"key"`
	Value pulumi.StringInput `pulumi:"value"`
}

func (PermissionSetTagArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*PermissionSetTag)(nil)).Elem()
}

func (i PermissionSetTagArgs) ToPermissionSetTagOutput() PermissionSetTagOutput {
	return i.ToPermissionSetTagOutputWithContext(context.Background())
}

func (i PermissionSetTagArgs) ToPermissionSetTagOutputWithContext(ctx context.Context) PermissionSetTagOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PermissionSetTagOutput)
}

// PermissionSetTagArrayInput is an input type that accepts PermissionSetTagArray and PermissionSetTagArrayOutput values.
// You can construct a concrete instance of `PermissionSetTagArrayInput` via:
//
//          PermissionSetTagArray{ PermissionSetTagArgs{...} }
type PermissionSetTagArrayInput interface {
	pulumi.Input

	ToPermissionSetTagArrayOutput() PermissionSetTagArrayOutput
	ToPermissionSetTagArrayOutputWithContext(context.Context) PermissionSetTagArrayOutput
}

type PermissionSetTagArray []PermissionSetTagInput

func (PermissionSetTagArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]PermissionSetTag)(nil)).Elem()
}

func (i PermissionSetTagArray) ToPermissionSetTagArrayOutput() PermissionSetTagArrayOutput {
	return i.ToPermissionSetTagArrayOutputWithContext(context.Background())
}

func (i PermissionSetTagArray) ToPermissionSetTagArrayOutputWithContext(ctx context.Context) PermissionSetTagArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PermissionSetTagArrayOutput)
}

// The metadata that you apply to the permission set to help you categorize and organize them.
type PermissionSetTagOutput struct{ *pulumi.OutputState }

func (PermissionSetTagOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*PermissionSetTag)(nil)).Elem()
}

func (o PermissionSetTagOutput) ToPermissionSetTagOutput() PermissionSetTagOutput {
	return o
}

func (o PermissionSetTagOutput) ToPermissionSetTagOutputWithContext(ctx context.Context) PermissionSetTagOutput {
	return o
}

func (o PermissionSetTagOutput) Key() pulumi.StringOutput {
	return o.ApplyT(func(v PermissionSetTag) string { return v.Key }).(pulumi.StringOutput)
}

func (o PermissionSetTagOutput) Value() pulumi.StringOutput {
	return o.ApplyT(func(v PermissionSetTag) string { return v.Value }).(pulumi.StringOutput)
}

type PermissionSetTagArrayOutput struct{ *pulumi.OutputState }

func (PermissionSetTagArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]PermissionSetTag)(nil)).Elem()
}

func (o PermissionSetTagArrayOutput) ToPermissionSetTagArrayOutput() PermissionSetTagArrayOutput {
	return o
}

func (o PermissionSetTagArrayOutput) ToPermissionSetTagArrayOutputWithContext(ctx context.Context) PermissionSetTagArrayOutput {
	return o
}

func (o PermissionSetTagArrayOutput) Index(i pulumi.IntInput) PermissionSetTagOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) PermissionSetTag {
		return vs[0].([]PermissionSetTag)[vs[1].(int)]
	}).(PermissionSetTagOutput)
}

func init() {
	pulumi.RegisterOutputType(InstanceAccessControlAttributeConfigurationAccessControlAttributeOutput{})
	pulumi.RegisterOutputType(InstanceAccessControlAttributeConfigurationAccessControlAttributeArrayOutput{})
	pulumi.RegisterOutputType(InstanceAccessControlAttributeConfigurationAccessControlAttributeValueOutput{})
	pulumi.RegisterOutputType(InstanceAccessControlAttributeConfigurationPropertiesOutput{})
	pulumi.RegisterOutputType(InstanceAccessControlAttributeConfigurationPropertiesPtrOutput{})
	pulumi.RegisterOutputType(PermissionSetTagOutput{})
	pulumi.RegisterOutputType(PermissionSetTagArrayOutput{})
}
