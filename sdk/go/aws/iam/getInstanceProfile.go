// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package iam

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::IAM::InstanceProfile
func LookupInstanceProfile(ctx *pulumi.Context, args *LookupInstanceProfileArgs, opts ...pulumi.InvokeOption) (*LookupInstanceProfileResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupInstanceProfileResult
	err := ctx.Invoke("aws-native:iam:getInstanceProfile", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupInstanceProfileArgs struct {
	// The name of the instance profile to create.
	InstanceProfileName string `pulumi:"instanceProfileName"`
}

type LookupInstanceProfileResult struct {
	// The Amazon Resource Name (ARN) of the instance profile.
	Arn *string `pulumi:"arn"`
	// The name of the role to associate with the instance profile. Only one role can be assigned to an EC2 instance at a time, and all applications on the instance share the same role and permissions.
	Roles []string `pulumi:"roles"`
}

func LookupInstanceProfileOutput(ctx *pulumi.Context, args LookupInstanceProfileOutputArgs, opts ...pulumi.InvokeOption) LookupInstanceProfileResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupInstanceProfileResult, error) {
			args := v.(LookupInstanceProfileArgs)
			r, err := LookupInstanceProfile(ctx, &args, opts...)
			var s LookupInstanceProfileResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupInstanceProfileResultOutput)
}

type LookupInstanceProfileOutputArgs struct {
	// The name of the instance profile to create.
	InstanceProfileName pulumi.StringInput `pulumi:"instanceProfileName"`
}

func (LookupInstanceProfileOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupInstanceProfileArgs)(nil)).Elem()
}

type LookupInstanceProfileResultOutput struct{ *pulumi.OutputState }

func (LookupInstanceProfileResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupInstanceProfileResult)(nil)).Elem()
}

func (o LookupInstanceProfileResultOutput) ToLookupInstanceProfileResultOutput() LookupInstanceProfileResultOutput {
	return o
}

func (o LookupInstanceProfileResultOutput) ToLookupInstanceProfileResultOutputWithContext(ctx context.Context) LookupInstanceProfileResultOutput {
	return o
}

func (o LookupInstanceProfileResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupInstanceProfileResult] {
	return pulumix.Output[LookupInstanceProfileResult]{
		OutputState: o.OutputState,
	}
}

// The Amazon Resource Name (ARN) of the instance profile.
func (o LookupInstanceProfileResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupInstanceProfileResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

// The name of the role to associate with the instance profile. Only one role can be assigned to an EC2 instance at a time, and all applications on the instance share the same role and permissions.
func (o LookupInstanceProfileResultOutput) Roles() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupInstanceProfileResult) []string { return v.Roles }).(pulumi.StringArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupInstanceProfileResultOutput{})
}
