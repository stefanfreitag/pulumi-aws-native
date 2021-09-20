// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package codestarconnections

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// A key-value pair to associate with a resource.
type ConnectionTag struct {
	// The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
	Key string `pulumi:"key"`
	// The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
	Value string `pulumi:"value"`
}

// ConnectionTagInput is an input type that accepts ConnectionTagArgs and ConnectionTagOutput values.
// You can construct a concrete instance of `ConnectionTagInput` via:
//
//          ConnectionTagArgs{...}
type ConnectionTagInput interface {
	pulumi.Input

	ToConnectionTagOutput() ConnectionTagOutput
	ToConnectionTagOutputWithContext(context.Context) ConnectionTagOutput
}

// A key-value pair to associate with a resource.
type ConnectionTagArgs struct {
	// The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
	Key pulumi.StringInput `pulumi:"key"`
	// The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
	Value pulumi.StringInput `pulumi:"value"`
}

func (ConnectionTagArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ConnectionTag)(nil)).Elem()
}

func (i ConnectionTagArgs) ToConnectionTagOutput() ConnectionTagOutput {
	return i.ToConnectionTagOutputWithContext(context.Background())
}

func (i ConnectionTagArgs) ToConnectionTagOutputWithContext(ctx context.Context) ConnectionTagOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ConnectionTagOutput)
}

// ConnectionTagArrayInput is an input type that accepts ConnectionTagArray and ConnectionTagArrayOutput values.
// You can construct a concrete instance of `ConnectionTagArrayInput` via:
//
//          ConnectionTagArray{ ConnectionTagArgs{...} }
type ConnectionTagArrayInput interface {
	pulumi.Input

	ToConnectionTagArrayOutput() ConnectionTagArrayOutput
	ToConnectionTagArrayOutputWithContext(context.Context) ConnectionTagArrayOutput
}

type ConnectionTagArray []ConnectionTagInput

func (ConnectionTagArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]ConnectionTag)(nil)).Elem()
}

func (i ConnectionTagArray) ToConnectionTagArrayOutput() ConnectionTagArrayOutput {
	return i.ToConnectionTagArrayOutputWithContext(context.Background())
}

func (i ConnectionTagArray) ToConnectionTagArrayOutputWithContext(ctx context.Context) ConnectionTagArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ConnectionTagArrayOutput)
}

// A key-value pair to associate with a resource.
type ConnectionTagOutput struct{ *pulumi.OutputState }

func (ConnectionTagOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ConnectionTag)(nil)).Elem()
}

func (o ConnectionTagOutput) ToConnectionTagOutput() ConnectionTagOutput {
	return o
}

func (o ConnectionTagOutput) ToConnectionTagOutputWithContext(ctx context.Context) ConnectionTagOutput {
	return o
}

// The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
func (o ConnectionTagOutput) Key() pulumi.StringOutput {
	return o.ApplyT(func(v ConnectionTag) string { return v.Key }).(pulumi.StringOutput)
}

// The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
func (o ConnectionTagOutput) Value() pulumi.StringOutput {
	return o.ApplyT(func(v ConnectionTag) string { return v.Value }).(pulumi.StringOutput)
}

type ConnectionTagArrayOutput struct{ *pulumi.OutputState }

func (ConnectionTagArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]ConnectionTag)(nil)).Elem()
}

func (o ConnectionTagArrayOutput) ToConnectionTagArrayOutput() ConnectionTagArrayOutput {
	return o
}

func (o ConnectionTagArrayOutput) ToConnectionTagArrayOutputWithContext(ctx context.Context) ConnectionTagArrayOutput {
	return o
}

func (o ConnectionTagArrayOutput) Index(i pulumi.IntInput) ConnectionTagOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) ConnectionTag {
		return vs[0].([]ConnectionTag)[vs[1].(int)]
	}).(ConnectionTagOutput)
}

func init() {
	pulumi.RegisterOutputType(ConnectionTagOutput{})
	pulumi.RegisterOutputType(ConnectionTagArrayOutput{})
}
