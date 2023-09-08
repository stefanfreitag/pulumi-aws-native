// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package iot

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// A dimension can be used to limit the scope of a metric used in a security profile for AWS IoT Device Defender.
func LookupDimension(ctx *pulumi.Context, args *LookupDimensionArgs, opts ...pulumi.InvokeOption) (*LookupDimensionResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupDimensionResult
	err := ctx.Invoke("aws-native:iot:getDimension", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupDimensionArgs struct {
	// A unique identifier for the dimension.
	Name string `pulumi:"name"`
}

type LookupDimensionResult struct {
	// The ARN (Amazon resource name) of the created dimension.
	Arn *string `pulumi:"arn"`
	// Specifies the value or list of values for the dimension.
	StringValues []string `pulumi:"stringValues"`
	// Metadata that can be used to manage the dimension.
	Tags []DimensionTag `pulumi:"tags"`
}

func LookupDimensionOutput(ctx *pulumi.Context, args LookupDimensionOutputArgs, opts ...pulumi.InvokeOption) LookupDimensionResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupDimensionResult, error) {
			args := v.(LookupDimensionArgs)
			r, err := LookupDimension(ctx, &args, opts...)
			var s LookupDimensionResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupDimensionResultOutput)
}

type LookupDimensionOutputArgs struct {
	// A unique identifier for the dimension.
	Name pulumi.StringInput `pulumi:"name"`
}

func (LookupDimensionOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDimensionArgs)(nil)).Elem()
}

type LookupDimensionResultOutput struct{ *pulumi.OutputState }

func (LookupDimensionResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDimensionResult)(nil)).Elem()
}

func (o LookupDimensionResultOutput) ToLookupDimensionResultOutput() LookupDimensionResultOutput {
	return o
}

func (o LookupDimensionResultOutput) ToLookupDimensionResultOutputWithContext(ctx context.Context) LookupDimensionResultOutput {
	return o
}

func (o LookupDimensionResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupDimensionResult] {
	return pulumix.Output[LookupDimensionResult]{
		OutputState: o.OutputState,
	}
}

// The ARN (Amazon resource name) of the created dimension.
func (o LookupDimensionResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDimensionResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

// Specifies the value or list of values for the dimension.
func (o LookupDimensionResultOutput) StringValues() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupDimensionResult) []string { return v.StringValues }).(pulumi.StringArrayOutput)
}

// Metadata that can be used to manage the dimension.
func (o LookupDimensionResultOutput) Tags() DimensionTagArrayOutput {
	return o.ApplyT(func(v LookupDimensionResult) []DimensionTag { return v.Tags }).(DimensionTagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupDimensionResultOutput{})
}
