// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package iotfleethub

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

var _ = internal.GetEnvOrDefault

// To add or update tag, provide both key and value. To delete tag, provide only tag key to be deleted.
type ApplicationTag struct {
	// The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
	Key string `pulumi:"key"`
	// The value for the tag. You can specify a value that is 1 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
	Value string `pulumi:"value"`
}

// ApplicationTagInput is an input type that accepts ApplicationTagArgs and ApplicationTagOutput values.
// You can construct a concrete instance of `ApplicationTagInput` via:
//
//	ApplicationTagArgs{...}
type ApplicationTagInput interface {
	pulumi.Input

	ToApplicationTagOutput() ApplicationTagOutput
	ToApplicationTagOutputWithContext(context.Context) ApplicationTagOutput
}

// To add or update tag, provide both key and value. To delete tag, provide only tag key to be deleted.
type ApplicationTagArgs struct {
	// The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
	Key pulumi.StringInput `pulumi:"key"`
	// The value for the tag. You can specify a value that is 1 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
	Value pulumi.StringInput `pulumi:"value"`
}

func (ApplicationTagArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ApplicationTag)(nil)).Elem()
}

func (i ApplicationTagArgs) ToApplicationTagOutput() ApplicationTagOutput {
	return i.ToApplicationTagOutputWithContext(context.Background())
}

func (i ApplicationTagArgs) ToApplicationTagOutputWithContext(ctx context.Context) ApplicationTagOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ApplicationTagOutput)
}

func (i ApplicationTagArgs) ToOutput(ctx context.Context) pulumix.Output[ApplicationTag] {
	return pulumix.Output[ApplicationTag]{
		OutputState: i.ToApplicationTagOutputWithContext(ctx).OutputState,
	}
}

// ApplicationTagArrayInput is an input type that accepts ApplicationTagArray and ApplicationTagArrayOutput values.
// You can construct a concrete instance of `ApplicationTagArrayInput` via:
//
//	ApplicationTagArray{ ApplicationTagArgs{...} }
type ApplicationTagArrayInput interface {
	pulumi.Input

	ToApplicationTagArrayOutput() ApplicationTagArrayOutput
	ToApplicationTagArrayOutputWithContext(context.Context) ApplicationTagArrayOutput
}

type ApplicationTagArray []ApplicationTagInput

func (ApplicationTagArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]ApplicationTag)(nil)).Elem()
}

func (i ApplicationTagArray) ToApplicationTagArrayOutput() ApplicationTagArrayOutput {
	return i.ToApplicationTagArrayOutputWithContext(context.Background())
}

func (i ApplicationTagArray) ToApplicationTagArrayOutputWithContext(ctx context.Context) ApplicationTagArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ApplicationTagArrayOutput)
}

func (i ApplicationTagArray) ToOutput(ctx context.Context) pulumix.Output[[]ApplicationTag] {
	return pulumix.Output[[]ApplicationTag]{
		OutputState: i.ToApplicationTagArrayOutputWithContext(ctx).OutputState,
	}
}

// To add or update tag, provide both key and value. To delete tag, provide only tag key to be deleted.
type ApplicationTagOutput struct{ *pulumi.OutputState }

func (ApplicationTagOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ApplicationTag)(nil)).Elem()
}

func (o ApplicationTagOutput) ToApplicationTagOutput() ApplicationTagOutput {
	return o
}

func (o ApplicationTagOutput) ToApplicationTagOutputWithContext(ctx context.Context) ApplicationTagOutput {
	return o
}

func (o ApplicationTagOutput) ToOutput(ctx context.Context) pulumix.Output[ApplicationTag] {
	return pulumix.Output[ApplicationTag]{
		OutputState: o.OutputState,
	}
}

// The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
func (o ApplicationTagOutput) Key() pulumi.StringOutput {
	return o.ApplyT(func(v ApplicationTag) string { return v.Key }).(pulumi.StringOutput)
}

// The value for the tag. You can specify a value that is 1 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
func (o ApplicationTagOutput) Value() pulumi.StringOutput {
	return o.ApplyT(func(v ApplicationTag) string { return v.Value }).(pulumi.StringOutput)
}

type ApplicationTagArrayOutput struct{ *pulumi.OutputState }

func (ApplicationTagArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]ApplicationTag)(nil)).Elem()
}

func (o ApplicationTagArrayOutput) ToApplicationTagArrayOutput() ApplicationTagArrayOutput {
	return o
}

func (o ApplicationTagArrayOutput) ToApplicationTagArrayOutputWithContext(ctx context.Context) ApplicationTagArrayOutput {
	return o
}

func (o ApplicationTagArrayOutput) ToOutput(ctx context.Context) pulumix.Output[[]ApplicationTag] {
	return pulumix.Output[[]ApplicationTag]{
		OutputState: o.OutputState,
	}
}

func (o ApplicationTagArrayOutput) Index(i pulumi.IntInput) ApplicationTagOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) ApplicationTag {
		return vs[0].([]ApplicationTag)[vs[1].(int)]
	}).(ApplicationTagOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ApplicationTagInput)(nil)).Elem(), ApplicationTagArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*ApplicationTagArrayInput)(nil)).Elem(), ApplicationTagArray{})
	pulumi.RegisterOutputType(ApplicationTagOutput{})
	pulumi.RegisterOutputType(ApplicationTagArrayOutput{})
}
