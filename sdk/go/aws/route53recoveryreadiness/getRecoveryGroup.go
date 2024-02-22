// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package route53recoveryreadiness

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// AWS Route53 Recovery Readiness Recovery Group Schema and API specifications.
func LookupRecoveryGroup(ctx *pulumi.Context, args *LookupRecoveryGroupArgs, opts ...pulumi.InvokeOption) (*LookupRecoveryGroupResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupRecoveryGroupResult
	err := ctx.Invoke("aws-native:route53recoveryreadiness:getRecoveryGroup", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupRecoveryGroupArgs struct {
	// The name of the recovery group to create.
	RecoveryGroupName string `pulumi:"recoveryGroupName"`
}

type LookupRecoveryGroupResult struct {
	// A list of the cell Amazon Resource Names (ARNs) in the recovery group.
	Cells []string `pulumi:"cells"`
	// A collection of tags associated with a resource.
	RecoveryGroupArn *string `pulumi:"recoveryGroupArn"`
	// A collection of tags associated with a resource.
	Tags []aws.Tag `pulumi:"tags"`
}

func LookupRecoveryGroupOutput(ctx *pulumi.Context, args LookupRecoveryGroupOutputArgs, opts ...pulumi.InvokeOption) LookupRecoveryGroupResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupRecoveryGroupResult, error) {
			args := v.(LookupRecoveryGroupArgs)
			r, err := LookupRecoveryGroup(ctx, &args, opts...)
			var s LookupRecoveryGroupResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupRecoveryGroupResultOutput)
}

type LookupRecoveryGroupOutputArgs struct {
	// The name of the recovery group to create.
	RecoveryGroupName pulumi.StringInput `pulumi:"recoveryGroupName"`
}

func (LookupRecoveryGroupOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupRecoveryGroupArgs)(nil)).Elem()
}

type LookupRecoveryGroupResultOutput struct{ *pulumi.OutputState }

func (LookupRecoveryGroupResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupRecoveryGroupResult)(nil)).Elem()
}

func (o LookupRecoveryGroupResultOutput) ToLookupRecoveryGroupResultOutput() LookupRecoveryGroupResultOutput {
	return o
}

func (o LookupRecoveryGroupResultOutput) ToLookupRecoveryGroupResultOutputWithContext(ctx context.Context) LookupRecoveryGroupResultOutput {
	return o
}

// A list of the cell Amazon Resource Names (ARNs) in the recovery group.
func (o LookupRecoveryGroupResultOutput) Cells() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupRecoveryGroupResult) []string { return v.Cells }).(pulumi.StringArrayOutput)
}

// A collection of tags associated with a resource.
func (o LookupRecoveryGroupResultOutput) RecoveryGroupArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupRecoveryGroupResult) *string { return v.RecoveryGroupArn }).(pulumi.StringPtrOutput)
}

// A collection of tags associated with a resource.
func (o LookupRecoveryGroupResultOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v LookupRecoveryGroupResult) []aws.Tag { return v.Tags }).(aws.TagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupRecoveryGroupResultOutput{})
}
