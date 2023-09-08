// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package servicecatalog

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::ServiceCatalog::LaunchTemplateConstraint
func LookupLaunchTemplateConstraint(ctx *pulumi.Context, args *LookupLaunchTemplateConstraintArgs, opts ...pulumi.InvokeOption) (*LookupLaunchTemplateConstraintResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupLaunchTemplateConstraintResult
	err := ctx.Invoke("aws-native:servicecatalog:getLaunchTemplateConstraint", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupLaunchTemplateConstraintArgs struct {
	Id string `pulumi:"id"`
}

type LookupLaunchTemplateConstraintResult struct {
	AcceptLanguage *string `pulumi:"acceptLanguage"`
	Description    *string `pulumi:"description"`
	Id             *string `pulumi:"id"`
	Rules          *string `pulumi:"rules"`
}

func LookupLaunchTemplateConstraintOutput(ctx *pulumi.Context, args LookupLaunchTemplateConstraintOutputArgs, opts ...pulumi.InvokeOption) LookupLaunchTemplateConstraintResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupLaunchTemplateConstraintResult, error) {
			args := v.(LookupLaunchTemplateConstraintArgs)
			r, err := LookupLaunchTemplateConstraint(ctx, &args, opts...)
			var s LookupLaunchTemplateConstraintResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupLaunchTemplateConstraintResultOutput)
}

type LookupLaunchTemplateConstraintOutputArgs struct {
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupLaunchTemplateConstraintOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupLaunchTemplateConstraintArgs)(nil)).Elem()
}

type LookupLaunchTemplateConstraintResultOutput struct{ *pulumi.OutputState }

func (LookupLaunchTemplateConstraintResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupLaunchTemplateConstraintResult)(nil)).Elem()
}

func (o LookupLaunchTemplateConstraintResultOutput) ToLookupLaunchTemplateConstraintResultOutput() LookupLaunchTemplateConstraintResultOutput {
	return o
}

func (o LookupLaunchTemplateConstraintResultOutput) ToLookupLaunchTemplateConstraintResultOutputWithContext(ctx context.Context) LookupLaunchTemplateConstraintResultOutput {
	return o
}

func (o LookupLaunchTemplateConstraintResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupLaunchTemplateConstraintResult] {
	return pulumix.Output[LookupLaunchTemplateConstraintResult]{
		OutputState: o.OutputState,
	}
}

func (o LookupLaunchTemplateConstraintResultOutput) AcceptLanguage() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupLaunchTemplateConstraintResult) *string { return v.AcceptLanguage }).(pulumi.StringPtrOutput)
}

func (o LookupLaunchTemplateConstraintResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupLaunchTemplateConstraintResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

func (o LookupLaunchTemplateConstraintResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupLaunchTemplateConstraintResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o LookupLaunchTemplateConstraintResultOutput) Rules() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupLaunchTemplateConstraintResult) *string { return v.Rules }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupLaunchTemplateConstraintResultOutput{})
}
