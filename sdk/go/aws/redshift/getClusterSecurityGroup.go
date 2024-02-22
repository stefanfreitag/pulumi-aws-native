// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package redshift

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::Redshift::ClusterSecurityGroup
func LookupClusterSecurityGroup(ctx *pulumi.Context, args *LookupClusterSecurityGroupArgs, opts ...pulumi.InvokeOption) (*LookupClusterSecurityGroupResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupClusterSecurityGroupResult
	err := ctx.Invoke("aws-native:redshift:getClusterSecurityGroup", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupClusterSecurityGroupArgs struct {
	Id string `pulumi:"id"`
}

type LookupClusterSecurityGroupResult struct {
	Id   *string   `pulumi:"id"`
	Tags []aws.Tag `pulumi:"tags"`
}

func LookupClusterSecurityGroupOutput(ctx *pulumi.Context, args LookupClusterSecurityGroupOutputArgs, opts ...pulumi.InvokeOption) LookupClusterSecurityGroupResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupClusterSecurityGroupResult, error) {
			args := v.(LookupClusterSecurityGroupArgs)
			r, err := LookupClusterSecurityGroup(ctx, &args, opts...)
			var s LookupClusterSecurityGroupResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupClusterSecurityGroupResultOutput)
}

type LookupClusterSecurityGroupOutputArgs struct {
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupClusterSecurityGroupOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupClusterSecurityGroupArgs)(nil)).Elem()
}

type LookupClusterSecurityGroupResultOutput struct{ *pulumi.OutputState }

func (LookupClusterSecurityGroupResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupClusterSecurityGroupResult)(nil)).Elem()
}

func (o LookupClusterSecurityGroupResultOutput) ToLookupClusterSecurityGroupResultOutput() LookupClusterSecurityGroupResultOutput {
	return o
}

func (o LookupClusterSecurityGroupResultOutput) ToLookupClusterSecurityGroupResultOutputWithContext(ctx context.Context) LookupClusterSecurityGroupResultOutput {
	return o
}

func (o LookupClusterSecurityGroupResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupClusterSecurityGroupResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o LookupClusterSecurityGroupResultOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v LookupClusterSecurityGroupResult) []aws.Tag { return v.Tags }).(aws.TagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupClusterSecurityGroupResultOutput{})
}
