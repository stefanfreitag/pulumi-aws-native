// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package logs

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// The resource schema for AWSLogs ResourcePolicy
func LookupResourcePolicy(ctx *pulumi.Context, args *LookupResourcePolicyArgs, opts ...pulumi.InvokeOption) (*LookupResourcePolicyResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupResourcePolicyResult
	err := ctx.Invoke("aws-native:logs:getResourcePolicy", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupResourcePolicyArgs struct {
	// A name for resource policy
	PolicyName string `pulumi:"policyName"`
}

type LookupResourcePolicyResult struct {
	// The policy document
	PolicyDocument *string `pulumi:"policyDocument"`
}

func LookupResourcePolicyOutput(ctx *pulumi.Context, args LookupResourcePolicyOutputArgs, opts ...pulumi.InvokeOption) LookupResourcePolicyResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupResourcePolicyResult, error) {
			args := v.(LookupResourcePolicyArgs)
			r, err := LookupResourcePolicy(ctx, &args, opts...)
			var s LookupResourcePolicyResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupResourcePolicyResultOutput)
}

type LookupResourcePolicyOutputArgs struct {
	// A name for resource policy
	PolicyName pulumi.StringInput `pulumi:"policyName"`
}

func (LookupResourcePolicyOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupResourcePolicyArgs)(nil)).Elem()
}

type LookupResourcePolicyResultOutput struct{ *pulumi.OutputState }

func (LookupResourcePolicyResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupResourcePolicyResult)(nil)).Elem()
}

func (o LookupResourcePolicyResultOutput) ToLookupResourcePolicyResultOutput() LookupResourcePolicyResultOutput {
	return o
}

func (o LookupResourcePolicyResultOutput) ToLookupResourcePolicyResultOutputWithContext(ctx context.Context) LookupResourcePolicyResultOutput {
	return o
}

func (o LookupResourcePolicyResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupResourcePolicyResult] {
	return pulumix.Output[LookupResourcePolicyResult]{
		OutputState: o.OutputState,
	}
}

// The policy document
func (o LookupResourcePolicyResultOutput) PolicyDocument() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupResourcePolicyResult) *string { return v.PolicyDocument }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupResourcePolicyResultOutput{})
}
