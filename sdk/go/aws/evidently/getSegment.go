// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package evidently

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::Evidently::Segment
func LookupSegment(ctx *pulumi.Context, args *LookupSegmentArgs, opts ...pulumi.InvokeOption) (*LookupSegmentResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupSegmentResult
	err := ctx.Invoke("aws-native:evidently:getSegment", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupSegmentArgs struct {
	Arn string `pulumi:"arn"`
}

type LookupSegmentResult struct {
	Arn         *string `pulumi:"arn"`
	Description *string `pulumi:"description"`
	Name        *string `pulumi:"name"`
	Pattern     *string `pulumi:"pattern"`
	// An array of key-value pairs to apply to this resource.
	Tags []aws.Tag `pulumi:"tags"`
}

func LookupSegmentOutput(ctx *pulumi.Context, args LookupSegmentOutputArgs, opts ...pulumi.InvokeOption) LookupSegmentResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupSegmentResult, error) {
			args := v.(LookupSegmentArgs)
			r, err := LookupSegment(ctx, &args, opts...)
			var s LookupSegmentResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupSegmentResultOutput)
}

type LookupSegmentOutputArgs struct {
	Arn pulumi.StringInput `pulumi:"arn"`
}

func (LookupSegmentOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupSegmentArgs)(nil)).Elem()
}

type LookupSegmentResultOutput struct{ *pulumi.OutputState }

func (LookupSegmentResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupSegmentResult)(nil)).Elem()
}

func (o LookupSegmentResultOutput) ToLookupSegmentResultOutput() LookupSegmentResultOutput {
	return o
}

func (o LookupSegmentResultOutput) ToLookupSegmentResultOutputWithContext(ctx context.Context) LookupSegmentResultOutput {
	return o
}

func (o LookupSegmentResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupSegmentResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

func (o LookupSegmentResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupSegmentResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

func (o LookupSegmentResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupSegmentResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func (o LookupSegmentResultOutput) Pattern() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupSegmentResult) *string { return v.Pattern }).(pulumi.StringPtrOutput)
}

// An array of key-value pairs to apply to this resource.
func (o LookupSegmentResultOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v LookupSegmentResult) []aws.Tag { return v.Tags }).(aws.TagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupSegmentResultOutput{})
}
