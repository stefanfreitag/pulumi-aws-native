// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package kinesis

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::Kinesis::StreamConsumer
func LookupStreamConsumer(ctx *pulumi.Context, args *LookupStreamConsumerArgs, opts ...pulumi.InvokeOption) (*LookupStreamConsumerResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupStreamConsumerResult
	err := ctx.Invoke("aws-native:kinesis:getStreamConsumer", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupStreamConsumerArgs struct {
	Id string `pulumi:"id"`
}

type LookupStreamConsumerResult struct {
	ConsumerArn               *string `pulumi:"consumerArn"`
	ConsumerCreationTimestamp *string `pulumi:"consumerCreationTimestamp"`
	ConsumerStatus            *string `pulumi:"consumerStatus"`
	Id                        *string `pulumi:"id"`
}

func LookupStreamConsumerOutput(ctx *pulumi.Context, args LookupStreamConsumerOutputArgs, opts ...pulumi.InvokeOption) LookupStreamConsumerResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupStreamConsumerResult, error) {
			args := v.(LookupStreamConsumerArgs)
			r, err := LookupStreamConsumer(ctx, &args, opts...)
			var s LookupStreamConsumerResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupStreamConsumerResultOutput)
}

type LookupStreamConsumerOutputArgs struct {
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupStreamConsumerOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupStreamConsumerArgs)(nil)).Elem()
}

type LookupStreamConsumerResultOutput struct{ *pulumi.OutputState }

func (LookupStreamConsumerResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupStreamConsumerResult)(nil)).Elem()
}

func (o LookupStreamConsumerResultOutput) ToLookupStreamConsumerResultOutput() LookupStreamConsumerResultOutput {
	return o
}

func (o LookupStreamConsumerResultOutput) ToLookupStreamConsumerResultOutputWithContext(ctx context.Context) LookupStreamConsumerResultOutput {
	return o
}

func (o LookupStreamConsumerResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupStreamConsumerResult] {
	return pulumix.Output[LookupStreamConsumerResult]{
		OutputState: o.OutputState,
	}
}

func (o LookupStreamConsumerResultOutput) ConsumerArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupStreamConsumerResult) *string { return v.ConsumerArn }).(pulumi.StringPtrOutput)
}

func (o LookupStreamConsumerResultOutput) ConsumerCreationTimestamp() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupStreamConsumerResult) *string { return v.ConsumerCreationTimestamp }).(pulumi.StringPtrOutput)
}

func (o LookupStreamConsumerResultOutput) ConsumerStatus() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupStreamConsumerResult) *string { return v.ConsumerStatus }).(pulumi.StringPtrOutput)
}

func (o LookupStreamConsumerResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupStreamConsumerResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupStreamConsumerResultOutput{})
}
