// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ssm

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::SSM::ResourcePolicy
func LookupResourcePolicy(ctx *pulumi.Context, args *LookupResourcePolicyArgs, opts ...pulumi.InvokeOption) (*LookupResourcePolicyResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupResourcePolicyResult
	err := ctx.Invoke("aws-native:ssm:getResourcePolicy", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupResourcePolicyArgs struct {
	// An unique identifier within the policies of a resource.
	PolicyId string `pulumi:"policyId"`
	// Arn of OpsItemGroup etc.
	ResourceArn string `pulumi:"resourceArn"`
}

type LookupResourcePolicyResult struct {
	// Actual policy statement.
	//
	// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::SSM::ResourcePolicy` for more information about the expected schema for this property.
	Policy interface{} `pulumi:"policy"`
	// A snapshot identifier for the policy over time.
	PolicyHash *string `pulumi:"policyHash"`
	// An unique identifier within the policies of a resource.
	PolicyId *string `pulumi:"policyId"`
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
	// An unique identifier within the policies of a resource.
	PolicyId pulumi.StringInput `pulumi:"policyId"`
	// Arn of OpsItemGroup etc.
	ResourceArn pulumi.StringInput `pulumi:"resourceArn"`
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

// Actual policy statement.
//
// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::SSM::ResourcePolicy` for more information about the expected schema for this property.
func (o LookupResourcePolicyResultOutput) Policy() pulumi.AnyOutput {
	return o.ApplyT(func(v LookupResourcePolicyResult) interface{} { return v.Policy }).(pulumi.AnyOutput)
}

// A snapshot identifier for the policy over time.
func (o LookupResourcePolicyResultOutput) PolicyHash() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupResourcePolicyResult) *string { return v.PolicyHash }).(pulumi.StringPtrOutput)
}

// An unique identifier within the policies of a resource.
func (o LookupResourcePolicyResultOutput) PolicyId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupResourcePolicyResult) *string { return v.PolicyId }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupResourcePolicyResultOutput{})
}
