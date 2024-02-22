// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ivs

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::IVS::StreamKey
func LookupStreamKey(ctx *pulumi.Context, args *LookupStreamKeyArgs, opts ...pulumi.InvokeOption) (*LookupStreamKeyResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupStreamKeyResult
	err := ctx.Invoke("aws-native:ivs:getStreamKey", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupStreamKeyArgs struct {
	// Stream Key ARN is automatically generated on creation and assigned as the unique identifier.
	Arn string `pulumi:"arn"`
}

type LookupStreamKeyResult struct {
	// Stream Key ARN is automatically generated on creation and assigned as the unique identifier.
	Arn *string `pulumi:"arn"`
	// A list of key-value pairs that contain metadata for the asset model.
	Tags []aws.Tag `pulumi:"tags"`
	// Stream-key value.
	Value *string `pulumi:"value"`
}

func LookupStreamKeyOutput(ctx *pulumi.Context, args LookupStreamKeyOutputArgs, opts ...pulumi.InvokeOption) LookupStreamKeyResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupStreamKeyResult, error) {
			args := v.(LookupStreamKeyArgs)
			r, err := LookupStreamKey(ctx, &args, opts...)
			var s LookupStreamKeyResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupStreamKeyResultOutput)
}

type LookupStreamKeyOutputArgs struct {
	// Stream Key ARN is automatically generated on creation and assigned as the unique identifier.
	Arn pulumi.StringInput `pulumi:"arn"`
}

func (LookupStreamKeyOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupStreamKeyArgs)(nil)).Elem()
}

type LookupStreamKeyResultOutput struct{ *pulumi.OutputState }

func (LookupStreamKeyResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupStreamKeyResult)(nil)).Elem()
}

func (o LookupStreamKeyResultOutput) ToLookupStreamKeyResultOutput() LookupStreamKeyResultOutput {
	return o
}

func (o LookupStreamKeyResultOutput) ToLookupStreamKeyResultOutputWithContext(ctx context.Context) LookupStreamKeyResultOutput {
	return o
}

// Stream Key ARN is automatically generated on creation and assigned as the unique identifier.
func (o LookupStreamKeyResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupStreamKeyResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

// A list of key-value pairs that contain metadata for the asset model.
func (o LookupStreamKeyResultOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v LookupStreamKeyResult) []aws.Tag { return v.Tags }).(aws.TagArrayOutput)
}

// Stream-key value.
func (o LookupStreamKeyResultOutput) Value() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupStreamKeyResult) *string { return v.Value }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupStreamKeyResultOutput{})
}
