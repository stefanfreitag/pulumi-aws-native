// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package qldb

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type StreamKinesisConfiguration struct {
	AggregationEnabled *bool   `pulumi:"aggregationEnabled"`
	StreamArn          *string `pulumi:"streamArn"`
}

// StreamKinesisConfigurationInput is an input type that accepts StreamKinesisConfigurationArgs and StreamKinesisConfigurationOutput values.
// You can construct a concrete instance of `StreamKinesisConfigurationInput` via:
//
//          StreamKinesisConfigurationArgs{...}
type StreamKinesisConfigurationInput interface {
	pulumi.Input

	ToStreamKinesisConfigurationOutput() StreamKinesisConfigurationOutput
	ToStreamKinesisConfigurationOutputWithContext(context.Context) StreamKinesisConfigurationOutput
}

type StreamKinesisConfigurationArgs struct {
	AggregationEnabled pulumi.BoolPtrInput   `pulumi:"aggregationEnabled"`
	StreamArn          pulumi.StringPtrInput `pulumi:"streamArn"`
}

func (StreamKinesisConfigurationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*StreamKinesisConfiguration)(nil)).Elem()
}

func (i StreamKinesisConfigurationArgs) ToStreamKinesisConfigurationOutput() StreamKinesisConfigurationOutput {
	return i.ToStreamKinesisConfigurationOutputWithContext(context.Background())
}

func (i StreamKinesisConfigurationArgs) ToStreamKinesisConfigurationOutputWithContext(ctx context.Context) StreamKinesisConfigurationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(StreamKinesisConfigurationOutput)
}

func (i StreamKinesisConfigurationArgs) ToStreamKinesisConfigurationPtrOutput() StreamKinesisConfigurationPtrOutput {
	return i.ToStreamKinesisConfigurationPtrOutputWithContext(context.Background())
}

func (i StreamKinesisConfigurationArgs) ToStreamKinesisConfigurationPtrOutputWithContext(ctx context.Context) StreamKinesisConfigurationPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(StreamKinesisConfigurationOutput).ToStreamKinesisConfigurationPtrOutputWithContext(ctx)
}

// StreamKinesisConfigurationPtrInput is an input type that accepts StreamKinesisConfigurationArgs, StreamKinesisConfigurationPtr and StreamKinesisConfigurationPtrOutput values.
// You can construct a concrete instance of `StreamKinesisConfigurationPtrInput` via:
//
//          StreamKinesisConfigurationArgs{...}
//
//  or:
//
//          nil
type StreamKinesisConfigurationPtrInput interface {
	pulumi.Input

	ToStreamKinesisConfigurationPtrOutput() StreamKinesisConfigurationPtrOutput
	ToStreamKinesisConfigurationPtrOutputWithContext(context.Context) StreamKinesisConfigurationPtrOutput
}

type streamKinesisConfigurationPtrType StreamKinesisConfigurationArgs

func StreamKinesisConfigurationPtr(v *StreamKinesisConfigurationArgs) StreamKinesisConfigurationPtrInput {
	return (*streamKinesisConfigurationPtrType)(v)
}

func (*streamKinesisConfigurationPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**StreamKinesisConfiguration)(nil)).Elem()
}

func (i *streamKinesisConfigurationPtrType) ToStreamKinesisConfigurationPtrOutput() StreamKinesisConfigurationPtrOutput {
	return i.ToStreamKinesisConfigurationPtrOutputWithContext(context.Background())
}

func (i *streamKinesisConfigurationPtrType) ToStreamKinesisConfigurationPtrOutputWithContext(ctx context.Context) StreamKinesisConfigurationPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(StreamKinesisConfigurationPtrOutput)
}

type StreamKinesisConfigurationOutput struct{ *pulumi.OutputState }

func (StreamKinesisConfigurationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*StreamKinesisConfiguration)(nil)).Elem()
}

func (o StreamKinesisConfigurationOutput) ToStreamKinesisConfigurationOutput() StreamKinesisConfigurationOutput {
	return o
}

func (o StreamKinesisConfigurationOutput) ToStreamKinesisConfigurationOutputWithContext(ctx context.Context) StreamKinesisConfigurationOutput {
	return o
}

func (o StreamKinesisConfigurationOutput) ToStreamKinesisConfigurationPtrOutput() StreamKinesisConfigurationPtrOutput {
	return o.ToStreamKinesisConfigurationPtrOutputWithContext(context.Background())
}

func (o StreamKinesisConfigurationOutput) ToStreamKinesisConfigurationPtrOutputWithContext(ctx context.Context) StreamKinesisConfigurationPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v StreamKinesisConfiguration) *StreamKinesisConfiguration {
		return &v
	}).(StreamKinesisConfigurationPtrOutput)
}

func (o StreamKinesisConfigurationOutput) AggregationEnabled() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v StreamKinesisConfiguration) *bool { return v.AggregationEnabled }).(pulumi.BoolPtrOutput)
}

func (o StreamKinesisConfigurationOutput) StreamArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v StreamKinesisConfiguration) *string { return v.StreamArn }).(pulumi.StringPtrOutput)
}

type StreamKinesisConfigurationPtrOutput struct{ *pulumi.OutputState }

func (StreamKinesisConfigurationPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**StreamKinesisConfiguration)(nil)).Elem()
}

func (o StreamKinesisConfigurationPtrOutput) ToStreamKinesisConfigurationPtrOutput() StreamKinesisConfigurationPtrOutput {
	return o
}

func (o StreamKinesisConfigurationPtrOutput) ToStreamKinesisConfigurationPtrOutputWithContext(ctx context.Context) StreamKinesisConfigurationPtrOutput {
	return o
}

func (o StreamKinesisConfigurationPtrOutput) Elem() StreamKinesisConfigurationOutput {
	return o.ApplyT(func(v *StreamKinesisConfiguration) StreamKinesisConfiguration {
		if v != nil {
			return *v
		}
		var ret StreamKinesisConfiguration
		return ret
	}).(StreamKinesisConfigurationOutput)
}

func (o StreamKinesisConfigurationPtrOutput) AggregationEnabled() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *StreamKinesisConfiguration) *bool {
		if v == nil {
			return nil
		}
		return v.AggregationEnabled
	}).(pulumi.BoolPtrOutput)
}

func (o StreamKinesisConfigurationPtrOutput) StreamArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *StreamKinesisConfiguration) *string {
		if v == nil {
			return nil
		}
		return v.StreamArn
	}).(pulumi.StringPtrOutput)
}

// A key-value pair to associate with a resource.
type StreamTag struct {
	// The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
	Key string `pulumi:"key"`
	// The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
	Value string `pulumi:"value"`
}

// StreamTagInput is an input type that accepts StreamTagArgs and StreamTagOutput values.
// You can construct a concrete instance of `StreamTagInput` via:
//
//          StreamTagArgs{...}
type StreamTagInput interface {
	pulumi.Input

	ToStreamTagOutput() StreamTagOutput
	ToStreamTagOutputWithContext(context.Context) StreamTagOutput
}

// A key-value pair to associate with a resource.
type StreamTagArgs struct {
	// The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
	Key pulumi.StringInput `pulumi:"key"`
	// The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
	Value pulumi.StringInput `pulumi:"value"`
}

func (StreamTagArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*StreamTag)(nil)).Elem()
}

func (i StreamTagArgs) ToStreamTagOutput() StreamTagOutput {
	return i.ToStreamTagOutputWithContext(context.Background())
}

func (i StreamTagArgs) ToStreamTagOutputWithContext(ctx context.Context) StreamTagOutput {
	return pulumi.ToOutputWithContext(ctx, i).(StreamTagOutput)
}

// StreamTagArrayInput is an input type that accepts StreamTagArray and StreamTagArrayOutput values.
// You can construct a concrete instance of `StreamTagArrayInput` via:
//
//          StreamTagArray{ StreamTagArgs{...} }
type StreamTagArrayInput interface {
	pulumi.Input

	ToStreamTagArrayOutput() StreamTagArrayOutput
	ToStreamTagArrayOutputWithContext(context.Context) StreamTagArrayOutput
}

type StreamTagArray []StreamTagInput

func (StreamTagArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]StreamTag)(nil)).Elem()
}

func (i StreamTagArray) ToStreamTagArrayOutput() StreamTagArrayOutput {
	return i.ToStreamTagArrayOutputWithContext(context.Background())
}

func (i StreamTagArray) ToStreamTagArrayOutputWithContext(ctx context.Context) StreamTagArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(StreamTagArrayOutput)
}

// A key-value pair to associate with a resource.
type StreamTagOutput struct{ *pulumi.OutputState }

func (StreamTagOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*StreamTag)(nil)).Elem()
}

func (o StreamTagOutput) ToStreamTagOutput() StreamTagOutput {
	return o
}

func (o StreamTagOutput) ToStreamTagOutputWithContext(ctx context.Context) StreamTagOutput {
	return o
}

// The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
func (o StreamTagOutput) Key() pulumi.StringOutput {
	return o.ApplyT(func(v StreamTag) string { return v.Key }).(pulumi.StringOutput)
}

// The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
func (o StreamTagOutput) Value() pulumi.StringOutput {
	return o.ApplyT(func(v StreamTag) string { return v.Value }).(pulumi.StringOutput)
}

type StreamTagArrayOutput struct{ *pulumi.OutputState }

func (StreamTagArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]StreamTag)(nil)).Elem()
}

func (o StreamTagArrayOutput) ToStreamTagArrayOutput() StreamTagArrayOutput {
	return o
}

func (o StreamTagArrayOutput) ToStreamTagArrayOutputWithContext(ctx context.Context) StreamTagArrayOutput {
	return o
}

func (o StreamTagArrayOutput) Index(i pulumi.IntInput) StreamTagOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) StreamTag {
		return vs[0].([]StreamTag)[vs[1].(int)]
	}).(StreamTagOutput)
}

func init() {
	pulumi.RegisterOutputType(StreamKinesisConfigurationOutput{})
	pulumi.RegisterOutputType(StreamKinesisConfigurationPtrOutput{})
	pulumi.RegisterOutputType(StreamTagOutput{})
	pulumi.RegisterOutputType(StreamTagArrayOutput{})
}
