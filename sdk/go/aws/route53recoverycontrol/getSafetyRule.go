// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package route53recoverycontrol

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource schema for AWS Route53 Recovery Control basic constructs and validation rules.
func LookupSafetyRule(ctx *pulumi.Context, args *LookupSafetyRuleArgs, opts ...pulumi.InvokeOption) (*LookupSafetyRuleResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupSafetyRuleResult
	err := ctx.Invoke("aws-native:route53recoverycontrol:getSafetyRule", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupSafetyRuleArgs struct {
	// The Amazon Resource Name (ARN) of the safety rule.
	SafetyRuleArn string `pulumi:"safetyRuleArn"`
}

type LookupSafetyRuleResult struct {
	AssertionRule *SafetyRuleAssertionRule `pulumi:"assertionRule"`
	GatingRule    *SafetyRuleGatingRule    `pulumi:"gatingRule"`
	Name          *string                  `pulumi:"name"`
	// The Amazon Resource Name (ARN) of the safety rule.
	SafetyRuleArn *string `pulumi:"safetyRuleArn"`
	// The deployment status of the routing control. Status can be one of the following: PENDING, DEPLOYED, PENDING_DELETION.
	Status *SafetyRuleStatus `pulumi:"status"`
}

func LookupSafetyRuleOutput(ctx *pulumi.Context, args LookupSafetyRuleOutputArgs, opts ...pulumi.InvokeOption) LookupSafetyRuleResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupSafetyRuleResult, error) {
			args := v.(LookupSafetyRuleArgs)
			r, err := LookupSafetyRule(ctx, &args, opts...)
			var s LookupSafetyRuleResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupSafetyRuleResultOutput)
}

type LookupSafetyRuleOutputArgs struct {
	// The Amazon Resource Name (ARN) of the safety rule.
	SafetyRuleArn pulumi.StringInput `pulumi:"safetyRuleArn"`
}

func (LookupSafetyRuleOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupSafetyRuleArgs)(nil)).Elem()
}

type LookupSafetyRuleResultOutput struct{ *pulumi.OutputState }

func (LookupSafetyRuleResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupSafetyRuleResult)(nil)).Elem()
}

func (o LookupSafetyRuleResultOutput) ToLookupSafetyRuleResultOutput() LookupSafetyRuleResultOutput {
	return o
}

func (o LookupSafetyRuleResultOutput) ToLookupSafetyRuleResultOutputWithContext(ctx context.Context) LookupSafetyRuleResultOutput {
	return o
}

func (o LookupSafetyRuleResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupSafetyRuleResult] {
	return pulumix.Output[LookupSafetyRuleResult]{
		OutputState: o.OutputState,
	}
}

func (o LookupSafetyRuleResultOutput) AssertionRule() SafetyRuleAssertionRulePtrOutput {
	return o.ApplyT(func(v LookupSafetyRuleResult) *SafetyRuleAssertionRule { return v.AssertionRule }).(SafetyRuleAssertionRulePtrOutput)
}

func (o LookupSafetyRuleResultOutput) GatingRule() SafetyRuleGatingRulePtrOutput {
	return o.ApplyT(func(v LookupSafetyRuleResult) *SafetyRuleGatingRule { return v.GatingRule }).(SafetyRuleGatingRulePtrOutput)
}

func (o LookupSafetyRuleResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupSafetyRuleResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

// The Amazon Resource Name (ARN) of the safety rule.
func (o LookupSafetyRuleResultOutput) SafetyRuleArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupSafetyRuleResult) *string { return v.SafetyRuleArn }).(pulumi.StringPtrOutput)
}

// The deployment status of the routing control. Status can be one of the following: PENDING, DEPLOYED, PENDING_DELETION.
func (o LookupSafetyRuleResultOutput) Status() SafetyRuleStatusPtrOutput {
	return o.ApplyT(func(v LookupSafetyRuleResult) *SafetyRuleStatus { return v.Status }).(SafetyRuleStatusPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupSafetyRuleResultOutput{})
}
