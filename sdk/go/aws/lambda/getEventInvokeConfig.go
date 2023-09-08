// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package lambda

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::Lambda::EventInvokeConfig
func LookupEventInvokeConfig(ctx *pulumi.Context, args *LookupEventInvokeConfigArgs, opts ...pulumi.InvokeOption) (*LookupEventInvokeConfigResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupEventInvokeConfigResult
	err := ctx.Invoke("aws-native:lambda:getEventInvokeConfig", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupEventInvokeConfigArgs struct {
	Id string `pulumi:"id"`
}

type LookupEventInvokeConfigResult struct {
	DestinationConfig        *EventInvokeConfigDestinationConfig `pulumi:"destinationConfig"`
	Id                       *string                             `pulumi:"id"`
	MaximumEventAgeInSeconds *int                                `pulumi:"maximumEventAgeInSeconds"`
	MaximumRetryAttempts     *int                                `pulumi:"maximumRetryAttempts"`
}

func LookupEventInvokeConfigOutput(ctx *pulumi.Context, args LookupEventInvokeConfigOutputArgs, opts ...pulumi.InvokeOption) LookupEventInvokeConfigResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupEventInvokeConfigResult, error) {
			args := v.(LookupEventInvokeConfigArgs)
			r, err := LookupEventInvokeConfig(ctx, &args, opts...)
			var s LookupEventInvokeConfigResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupEventInvokeConfigResultOutput)
}

type LookupEventInvokeConfigOutputArgs struct {
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupEventInvokeConfigOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupEventInvokeConfigArgs)(nil)).Elem()
}

type LookupEventInvokeConfigResultOutput struct{ *pulumi.OutputState }

func (LookupEventInvokeConfigResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupEventInvokeConfigResult)(nil)).Elem()
}

func (o LookupEventInvokeConfigResultOutput) ToLookupEventInvokeConfigResultOutput() LookupEventInvokeConfigResultOutput {
	return o
}

func (o LookupEventInvokeConfigResultOutput) ToLookupEventInvokeConfigResultOutputWithContext(ctx context.Context) LookupEventInvokeConfigResultOutput {
	return o
}

func (o LookupEventInvokeConfigResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupEventInvokeConfigResult] {
	return pulumix.Output[LookupEventInvokeConfigResult]{
		OutputState: o.OutputState,
	}
}

func (o LookupEventInvokeConfigResultOutput) DestinationConfig() EventInvokeConfigDestinationConfigPtrOutput {
	return o.ApplyT(func(v LookupEventInvokeConfigResult) *EventInvokeConfigDestinationConfig { return v.DestinationConfig }).(EventInvokeConfigDestinationConfigPtrOutput)
}

func (o LookupEventInvokeConfigResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupEventInvokeConfigResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o LookupEventInvokeConfigResultOutput) MaximumEventAgeInSeconds() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupEventInvokeConfigResult) *int { return v.MaximumEventAgeInSeconds }).(pulumi.IntPtrOutput)
}

func (o LookupEventInvokeConfigResultOutput) MaximumRetryAttempts() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupEventInvokeConfigResult) *int { return v.MaximumRetryAttempts }).(pulumi.IntPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupEventInvokeConfigResultOutput{})
}
