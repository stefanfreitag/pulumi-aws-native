// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package iot

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// A custom metric published by your devices to Device Defender.
func LookupCustomMetric(ctx *pulumi.Context, args *LookupCustomMetricArgs, opts ...pulumi.InvokeOption) (*LookupCustomMetricResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupCustomMetricResult
	err := ctx.Invoke("aws-native:iot:getCustomMetric", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupCustomMetricArgs struct {
	// The name of the custom metric. This will be used in the metric report submitted from the device/thing. Shouldn't begin with aws: . Cannot be updated once defined.
	MetricName string `pulumi:"metricName"`
}

type LookupCustomMetricResult struct {
	// Field represents a friendly name in the console for the custom metric; it doesn't have to be unique. Don't use this name as the metric identifier in the device metric report. Can be updated once defined.
	DisplayName *string `pulumi:"displayName"`
	// The Amazon Resource Number (ARN) of the custom metric.
	MetricArn *string `pulumi:"metricArn"`
	// An array of key-value pairs to apply to this resource.
	Tags []aws.Tag `pulumi:"tags"`
}

func LookupCustomMetricOutput(ctx *pulumi.Context, args LookupCustomMetricOutputArgs, opts ...pulumi.InvokeOption) LookupCustomMetricResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupCustomMetricResult, error) {
			args := v.(LookupCustomMetricArgs)
			r, err := LookupCustomMetric(ctx, &args, opts...)
			var s LookupCustomMetricResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupCustomMetricResultOutput)
}

type LookupCustomMetricOutputArgs struct {
	// The name of the custom metric. This will be used in the metric report submitted from the device/thing. Shouldn't begin with aws: . Cannot be updated once defined.
	MetricName pulumi.StringInput `pulumi:"metricName"`
}

func (LookupCustomMetricOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupCustomMetricArgs)(nil)).Elem()
}

type LookupCustomMetricResultOutput struct{ *pulumi.OutputState }

func (LookupCustomMetricResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupCustomMetricResult)(nil)).Elem()
}

func (o LookupCustomMetricResultOutput) ToLookupCustomMetricResultOutput() LookupCustomMetricResultOutput {
	return o
}

func (o LookupCustomMetricResultOutput) ToLookupCustomMetricResultOutputWithContext(ctx context.Context) LookupCustomMetricResultOutput {
	return o
}

// Field represents a friendly name in the console for the custom metric; it doesn't have to be unique. Don't use this name as the metric identifier in the device metric report. Can be updated once defined.
func (o LookupCustomMetricResultOutput) DisplayName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupCustomMetricResult) *string { return v.DisplayName }).(pulumi.StringPtrOutput)
}

// The Amazon Resource Number (ARN) of the custom metric.
func (o LookupCustomMetricResultOutput) MetricArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupCustomMetricResult) *string { return v.MetricArn }).(pulumi.StringPtrOutput)
}

// An array of key-value pairs to apply to this resource.
func (o LookupCustomMetricResultOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v LookupCustomMetricResult) []aws.Tag { return v.Tags }).(aws.TagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupCustomMetricResultOutput{})
}
