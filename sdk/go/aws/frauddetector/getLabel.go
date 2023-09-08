// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package frauddetector

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// An label for fraud detector.
func LookupLabel(ctx *pulumi.Context, args *LookupLabelArgs, opts ...pulumi.InvokeOption) (*LookupLabelResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupLabelResult
	err := ctx.Invoke("aws-native:frauddetector:getLabel", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupLabelArgs struct {
	// The label ARN.
	Arn string `pulumi:"arn"`
}

type LookupLabelResult struct {
	// The label ARN.
	Arn *string `pulumi:"arn"`
	// The timestamp when the label was created.
	CreatedTime *string `pulumi:"createdTime"`
	// The label description.
	Description *string `pulumi:"description"`
	// The timestamp when the label was last updated.
	LastUpdatedTime *string `pulumi:"lastUpdatedTime"`
	// Tags associated with this label.
	Tags []LabelTag `pulumi:"tags"`
}

func LookupLabelOutput(ctx *pulumi.Context, args LookupLabelOutputArgs, opts ...pulumi.InvokeOption) LookupLabelResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupLabelResult, error) {
			args := v.(LookupLabelArgs)
			r, err := LookupLabel(ctx, &args, opts...)
			var s LookupLabelResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupLabelResultOutput)
}

type LookupLabelOutputArgs struct {
	// The label ARN.
	Arn pulumi.StringInput `pulumi:"arn"`
}

func (LookupLabelOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupLabelArgs)(nil)).Elem()
}

type LookupLabelResultOutput struct{ *pulumi.OutputState }

func (LookupLabelResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupLabelResult)(nil)).Elem()
}

func (o LookupLabelResultOutput) ToLookupLabelResultOutput() LookupLabelResultOutput {
	return o
}

func (o LookupLabelResultOutput) ToLookupLabelResultOutputWithContext(ctx context.Context) LookupLabelResultOutput {
	return o
}

func (o LookupLabelResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupLabelResult] {
	return pulumix.Output[LookupLabelResult]{
		OutputState: o.OutputState,
	}
}

// The label ARN.
func (o LookupLabelResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupLabelResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

// The timestamp when the label was created.
func (o LookupLabelResultOutput) CreatedTime() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupLabelResult) *string { return v.CreatedTime }).(pulumi.StringPtrOutput)
}

// The label description.
func (o LookupLabelResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupLabelResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

// The timestamp when the label was last updated.
func (o LookupLabelResultOutput) LastUpdatedTime() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupLabelResult) *string { return v.LastUpdatedTime }).(pulumi.StringPtrOutput)
}

// Tags associated with this label.
func (o LookupLabelResultOutput) Tags() LabelTagArrayOutput {
	return o.ApplyT(func(v LookupLabelResult) []LabelTag { return v.Tags }).(LabelTagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupLabelResultOutput{})
}
