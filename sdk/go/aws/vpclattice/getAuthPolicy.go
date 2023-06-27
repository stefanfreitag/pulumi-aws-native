// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package vpclattice

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Creates or updates the auth policy.
func LookupAuthPolicy(ctx *pulumi.Context, args *LookupAuthPolicyArgs, opts ...pulumi.InvokeOption) (*LookupAuthPolicyResult, error) {
	var rv LookupAuthPolicyResult
	err := ctx.Invoke("aws-native:vpclattice:getAuthPolicy", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupAuthPolicyArgs struct {
	ResourceIdentifier string `pulumi:"resourceIdentifier"`
}

type LookupAuthPolicyResult struct {
	Policy interface{}          `pulumi:"policy"`
	State  *AuthPolicyStateEnum `pulumi:"state"`
}

func LookupAuthPolicyOutput(ctx *pulumi.Context, args LookupAuthPolicyOutputArgs, opts ...pulumi.InvokeOption) LookupAuthPolicyResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupAuthPolicyResult, error) {
			args := v.(LookupAuthPolicyArgs)
			r, err := LookupAuthPolicy(ctx, &args, opts...)
			var s LookupAuthPolicyResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupAuthPolicyResultOutput)
}

type LookupAuthPolicyOutputArgs struct {
	ResourceIdentifier pulumi.StringInput `pulumi:"resourceIdentifier"`
}

func (LookupAuthPolicyOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupAuthPolicyArgs)(nil)).Elem()
}

type LookupAuthPolicyResultOutput struct{ *pulumi.OutputState }

func (LookupAuthPolicyResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupAuthPolicyResult)(nil)).Elem()
}

func (o LookupAuthPolicyResultOutput) ToLookupAuthPolicyResultOutput() LookupAuthPolicyResultOutput {
	return o
}

func (o LookupAuthPolicyResultOutput) ToLookupAuthPolicyResultOutputWithContext(ctx context.Context) LookupAuthPolicyResultOutput {
	return o
}

func (o LookupAuthPolicyResultOutput) Policy() pulumi.AnyOutput {
	return o.ApplyT(func(v LookupAuthPolicyResult) interface{} { return v.Policy }).(pulumi.AnyOutput)
}

func (o LookupAuthPolicyResultOutput) State() AuthPolicyStateEnumPtrOutput {
	return o.ApplyT(func(v LookupAuthPolicyResult) *AuthPolicyStateEnum { return v.State }).(AuthPolicyStateEnumPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupAuthPolicyResultOutput{})
}
