// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package datasync

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource schema for AWS::DataSync::LocationEFS.
func LookupLocationEfs(ctx *pulumi.Context, args *LookupLocationEfsArgs, opts ...pulumi.InvokeOption) (*LookupLocationEfsResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupLocationEfsResult
	err := ctx.Invoke("aws-native:datasync:getLocationEfs", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupLocationEfsArgs struct {
	// The Amazon Resource Name (ARN) of the Amazon EFS file system location that is created.
	LocationArn string `pulumi:"locationArn"`
}

type LookupLocationEfsResult struct {
	// The Amazon Resource Name (ARN) of the Amazon EFS file system location that is created.
	LocationArn *string `pulumi:"locationArn"`
	// The URL of the EFS location that was described.
	LocationUri *string `pulumi:"locationUri"`
	// An array of key-value pairs to apply to this resource.
	Tags []aws.Tag `pulumi:"tags"`
}

func LookupLocationEfsOutput(ctx *pulumi.Context, args LookupLocationEfsOutputArgs, opts ...pulumi.InvokeOption) LookupLocationEfsResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupLocationEfsResult, error) {
			args := v.(LookupLocationEfsArgs)
			r, err := LookupLocationEfs(ctx, &args, opts...)
			var s LookupLocationEfsResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupLocationEfsResultOutput)
}

type LookupLocationEfsOutputArgs struct {
	// The Amazon Resource Name (ARN) of the Amazon EFS file system location that is created.
	LocationArn pulumi.StringInput `pulumi:"locationArn"`
}

func (LookupLocationEfsOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupLocationEfsArgs)(nil)).Elem()
}

type LookupLocationEfsResultOutput struct{ *pulumi.OutputState }

func (LookupLocationEfsResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupLocationEfsResult)(nil)).Elem()
}

func (o LookupLocationEfsResultOutput) ToLookupLocationEfsResultOutput() LookupLocationEfsResultOutput {
	return o
}

func (o LookupLocationEfsResultOutput) ToLookupLocationEfsResultOutputWithContext(ctx context.Context) LookupLocationEfsResultOutput {
	return o
}

// The Amazon Resource Name (ARN) of the Amazon EFS file system location that is created.
func (o LookupLocationEfsResultOutput) LocationArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupLocationEfsResult) *string { return v.LocationArn }).(pulumi.StringPtrOutput)
}

// The URL of the EFS location that was described.
func (o LookupLocationEfsResultOutput) LocationUri() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupLocationEfsResult) *string { return v.LocationUri }).(pulumi.StringPtrOutput)
}

// An array of key-value pairs to apply to this resource.
func (o LookupLocationEfsResultOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v LookupLocationEfsResult) []aws.Tag { return v.Tags }).(aws.TagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupLocationEfsResultOutput{})
}
