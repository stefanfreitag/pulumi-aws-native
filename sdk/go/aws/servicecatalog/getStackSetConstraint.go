// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package servicecatalog

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::ServiceCatalog::StackSetConstraint
func LookupStackSetConstraint(ctx *pulumi.Context, args *LookupStackSetConstraintArgs, opts ...pulumi.InvokeOption) (*LookupStackSetConstraintResult, error) {
	var rv LookupStackSetConstraintResult
	err := ctx.Invoke("aws-native:servicecatalog:getStackSetConstraint", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupStackSetConstraintArgs struct {
	Id string `pulumi:"id"`
}

type LookupStackSetConstraintResult struct {
	AcceptLanguage       *string  `pulumi:"acceptLanguage"`
	AccountList          []string `pulumi:"accountList"`
	AdminRole            *string  `pulumi:"adminRole"`
	Description          *string  `pulumi:"description"`
	ExecutionRole        *string  `pulumi:"executionRole"`
	Id                   *string  `pulumi:"id"`
	RegionList           []string `pulumi:"regionList"`
	StackInstanceControl *string  `pulumi:"stackInstanceControl"`
}

func LookupStackSetConstraintOutput(ctx *pulumi.Context, args LookupStackSetConstraintOutputArgs, opts ...pulumi.InvokeOption) LookupStackSetConstraintResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupStackSetConstraintResult, error) {
			args := v.(LookupStackSetConstraintArgs)
			r, err := LookupStackSetConstraint(ctx, &args, opts...)
			var s LookupStackSetConstraintResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupStackSetConstraintResultOutput)
}

type LookupStackSetConstraintOutputArgs struct {
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupStackSetConstraintOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupStackSetConstraintArgs)(nil)).Elem()
}

type LookupStackSetConstraintResultOutput struct{ *pulumi.OutputState }

func (LookupStackSetConstraintResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupStackSetConstraintResult)(nil)).Elem()
}

func (o LookupStackSetConstraintResultOutput) ToLookupStackSetConstraintResultOutput() LookupStackSetConstraintResultOutput {
	return o
}

func (o LookupStackSetConstraintResultOutput) ToLookupStackSetConstraintResultOutputWithContext(ctx context.Context) LookupStackSetConstraintResultOutput {
	return o
}

func (o LookupStackSetConstraintResultOutput) AcceptLanguage() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupStackSetConstraintResult) *string { return v.AcceptLanguage }).(pulumi.StringPtrOutput)
}

func (o LookupStackSetConstraintResultOutput) AccountList() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupStackSetConstraintResult) []string { return v.AccountList }).(pulumi.StringArrayOutput)
}

func (o LookupStackSetConstraintResultOutput) AdminRole() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupStackSetConstraintResult) *string { return v.AdminRole }).(pulumi.StringPtrOutput)
}

func (o LookupStackSetConstraintResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupStackSetConstraintResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

func (o LookupStackSetConstraintResultOutput) ExecutionRole() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupStackSetConstraintResult) *string { return v.ExecutionRole }).(pulumi.StringPtrOutput)
}

func (o LookupStackSetConstraintResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupStackSetConstraintResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o LookupStackSetConstraintResultOutput) RegionList() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupStackSetConstraintResult) []string { return v.RegionList }).(pulumi.StringArrayOutput)
}

func (o LookupStackSetConstraintResultOutput) StackInstanceControl() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupStackSetConstraintResult) *string { return v.StackInstanceControl }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupStackSetConstraintResultOutput{})
}
