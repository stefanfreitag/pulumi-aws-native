// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package s3

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// The AWS::S3::StorageLensGroup resource is an Amazon S3 resource type that you can use to create Storage Lens Group.
func LookupStorageLensGroup(ctx *pulumi.Context, args *LookupStorageLensGroupArgs, opts ...pulumi.InvokeOption) (*LookupStorageLensGroupResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupStorageLensGroupResult
	err := ctx.Invoke("aws-native:s3:getStorageLensGroup", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupStorageLensGroupArgs struct {
	Name string `pulumi:"name"`
}

type LookupStorageLensGroupResult struct {
	Filter *StorageLensGroupFilter `pulumi:"filter"`
	// The ARN for the Amazon S3 Storage Lens Group.
	StorageLensGroupArn *string `pulumi:"storageLensGroupArn"`
	// A set of tags (key-value pairs) for this Amazon S3 Storage Lens Group.
	Tags []StorageLensGroupTag `pulumi:"tags"`
}

func LookupStorageLensGroupOutput(ctx *pulumi.Context, args LookupStorageLensGroupOutputArgs, opts ...pulumi.InvokeOption) LookupStorageLensGroupResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupStorageLensGroupResult, error) {
			args := v.(LookupStorageLensGroupArgs)
			r, err := LookupStorageLensGroup(ctx, &args, opts...)
			var s LookupStorageLensGroupResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupStorageLensGroupResultOutput)
}

type LookupStorageLensGroupOutputArgs struct {
	Name pulumi.StringInput `pulumi:"name"`
}

func (LookupStorageLensGroupOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupStorageLensGroupArgs)(nil)).Elem()
}

type LookupStorageLensGroupResultOutput struct{ *pulumi.OutputState }

func (LookupStorageLensGroupResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupStorageLensGroupResult)(nil)).Elem()
}

func (o LookupStorageLensGroupResultOutput) ToLookupStorageLensGroupResultOutput() LookupStorageLensGroupResultOutput {
	return o
}

func (o LookupStorageLensGroupResultOutput) ToLookupStorageLensGroupResultOutputWithContext(ctx context.Context) LookupStorageLensGroupResultOutput {
	return o
}

func (o LookupStorageLensGroupResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupStorageLensGroupResult] {
	return pulumix.Output[LookupStorageLensGroupResult]{
		OutputState: o.OutputState,
	}
}

func (o LookupStorageLensGroupResultOutput) Filter() StorageLensGroupFilterPtrOutput {
	return o.ApplyT(func(v LookupStorageLensGroupResult) *StorageLensGroupFilter { return v.Filter }).(StorageLensGroupFilterPtrOutput)
}

// The ARN for the Amazon S3 Storage Lens Group.
func (o LookupStorageLensGroupResultOutput) StorageLensGroupArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupStorageLensGroupResult) *string { return v.StorageLensGroupArn }).(pulumi.StringPtrOutput)
}

// A set of tags (key-value pairs) for this Amazon S3 Storage Lens Group.
func (o LookupStorageLensGroupResultOutput) Tags() StorageLensGroupTagArrayOutput {
	return o.ApplyT(func(v LookupStorageLensGroupResult) []StorageLensGroupTag { return v.Tags }).(StorageLensGroupTagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupStorageLensGroupResultOutput{})
}
