// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package vpclattice

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Retrieves information about the resource policy. The resource policy is an IAM policy created by AWS RAM on behalf of the resource owner when they share a resource.
func LookupResourcePolicy(ctx *pulumi.Context, args *LookupResourcePolicyArgs, opts ...pulumi.InvokeOption) (*LookupResourcePolicyResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupResourcePolicyResult
	err := ctx.Invoke("aws-native:vpclattice:getResourcePolicy", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupResourcePolicyArgs struct {
	ResourceArn string `pulumi:"resourceArn"`
}

type LookupResourcePolicyResult struct {
	Policy interface{} `pulumi:"policy"`
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

func (o LookupResourcePolicyResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupResourcePolicyResult] {
	return pulumix.Output[LookupResourcePolicyResult]{
		OutputState: o.OutputState,
	}
}

func (o LookupResourcePolicyResultOutput) Policy() pulumi.AnyOutput {
	return o.ApplyT(func(v LookupResourcePolicyResult) interface{} { return v.Policy }).(pulumi.AnyOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupResourcePolicyResultOutput{})
}
