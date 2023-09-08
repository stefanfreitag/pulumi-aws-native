// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package datasync

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource schema for AWS::DataSync::LocationNFS
func LookupLocationNfs(ctx *pulumi.Context, args *LookupLocationNfsArgs, opts ...pulumi.InvokeOption) (*LookupLocationNfsResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupLocationNfsResult
	err := ctx.Invoke("aws-native:datasync:getLocationNfs", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupLocationNfsArgs struct {
	// The Amazon Resource Name (ARN) of the NFS location.
	LocationArn string `pulumi:"locationArn"`
}

type LookupLocationNfsResult struct {
	// The Amazon Resource Name (ARN) of the NFS location.
	LocationArn *string `pulumi:"locationArn"`
	// The URL of the NFS location that was described.
	LocationUri  *string                  `pulumi:"locationUri"`
	MountOptions *LocationNfsMountOptions `pulumi:"mountOptions"`
	OnPremConfig *LocationNfsOnPremConfig `pulumi:"onPremConfig"`
	// An array of key-value pairs to apply to this resource.
	Tags []LocationNfsTag `pulumi:"tags"`
}

func LookupLocationNfsOutput(ctx *pulumi.Context, args LookupLocationNfsOutputArgs, opts ...pulumi.InvokeOption) LookupLocationNfsResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupLocationNfsResult, error) {
			args := v.(LookupLocationNfsArgs)
			r, err := LookupLocationNfs(ctx, &args, opts...)
			var s LookupLocationNfsResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupLocationNfsResultOutput)
}

type LookupLocationNfsOutputArgs struct {
	// The Amazon Resource Name (ARN) of the NFS location.
	LocationArn pulumi.StringInput `pulumi:"locationArn"`
}

func (LookupLocationNfsOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupLocationNfsArgs)(nil)).Elem()
}

type LookupLocationNfsResultOutput struct{ *pulumi.OutputState }

func (LookupLocationNfsResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupLocationNfsResult)(nil)).Elem()
}

func (o LookupLocationNfsResultOutput) ToLookupLocationNfsResultOutput() LookupLocationNfsResultOutput {
	return o
}

func (o LookupLocationNfsResultOutput) ToLookupLocationNfsResultOutputWithContext(ctx context.Context) LookupLocationNfsResultOutput {
	return o
}

func (o LookupLocationNfsResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupLocationNfsResult] {
	return pulumix.Output[LookupLocationNfsResult]{
		OutputState: o.OutputState,
	}
}

// The Amazon Resource Name (ARN) of the NFS location.
func (o LookupLocationNfsResultOutput) LocationArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupLocationNfsResult) *string { return v.LocationArn }).(pulumi.StringPtrOutput)
}

// The URL of the NFS location that was described.
func (o LookupLocationNfsResultOutput) LocationUri() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupLocationNfsResult) *string { return v.LocationUri }).(pulumi.StringPtrOutput)
}

func (o LookupLocationNfsResultOutput) MountOptions() LocationNfsMountOptionsPtrOutput {
	return o.ApplyT(func(v LookupLocationNfsResult) *LocationNfsMountOptions { return v.MountOptions }).(LocationNfsMountOptionsPtrOutput)
}

func (o LookupLocationNfsResultOutput) OnPremConfig() LocationNfsOnPremConfigPtrOutput {
	return o.ApplyT(func(v LookupLocationNfsResult) *LocationNfsOnPremConfig { return v.OnPremConfig }).(LocationNfsOnPremConfigPtrOutput)
}

// An array of key-value pairs to apply to this resource.
func (o LookupLocationNfsResultOutput) Tags() LocationNfsTagArrayOutput {
	return o.ApplyT(func(v LookupLocationNfsResult) []LocationNfsTag { return v.Tags }).(LocationNfsTagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupLocationNfsResultOutput{})
}
