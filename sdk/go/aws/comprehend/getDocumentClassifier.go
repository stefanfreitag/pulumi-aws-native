// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package comprehend

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Document Classifier enables training document classifier models.
func LookupDocumentClassifier(ctx *pulumi.Context, args *LookupDocumentClassifierArgs, opts ...pulumi.InvokeOption) (*LookupDocumentClassifierResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupDocumentClassifierResult
	err := ctx.Invoke("aws-native:comprehend:getDocumentClassifier", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupDocumentClassifierArgs struct {
	Arn string `pulumi:"arn"`
}

type LookupDocumentClassifierResult struct {
	Arn         *string   `pulumi:"arn"`
	ModelPolicy *string   `pulumi:"modelPolicy"`
	Tags        []aws.Tag `pulumi:"tags"`
}

func LookupDocumentClassifierOutput(ctx *pulumi.Context, args LookupDocumentClassifierOutputArgs, opts ...pulumi.InvokeOption) LookupDocumentClassifierResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupDocumentClassifierResult, error) {
			args := v.(LookupDocumentClassifierArgs)
			r, err := LookupDocumentClassifier(ctx, &args, opts...)
			var s LookupDocumentClassifierResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupDocumentClassifierResultOutput)
}

type LookupDocumentClassifierOutputArgs struct {
	Arn pulumi.StringInput `pulumi:"arn"`
}

func (LookupDocumentClassifierOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDocumentClassifierArgs)(nil)).Elem()
}

type LookupDocumentClassifierResultOutput struct{ *pulumi.OutputState }

func (LookupDocumentClassifierResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDocumentClassifierResult)(nil)).Elem()
}

func (o LookupDocumentClassifierResultOutput) ToLookupDocumentClassifierResultOutput() LookupDocumentClassifierResultOutput {
	return o
}

func (o LookupDocumentClassifierResultOutput) ToLookupDocumentClassifierResultOutputWithContext(ctx context.Context) LookupDocumentClassifierResultOutput {
	return o
}

func (o LookupDocumentClassifierResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDocumentClassifierResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

func (o LookupDocumentClassifierResultOutput) ModelPolicy() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDocumentClassifierResult) *string { return v.ModelPolicy }).(pulumi.StringPtrOutput)
}

func (o LookupDocumentClassifierResultOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v LookupDocumentClassifierResult) []aws.Tag { return v.Tags }).(aws.TagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupDocumentClassifierResultOutput{})
}
