// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package securityhub

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// The AWS::SecurityHub::AutomationRule resource represents the Automation Rule in your account. One rule resource is created for each Automation Rule in which you configure rule criteria and actions.
func LookupAutomationRule(ctx *pulumi.Context, args *LookupAutomationRuleArgs, opts ...pulumi.InvokeOption) (*LookupAutomationRuleResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupAutomationRuleResult
	err := ctx.Invoke("aws-native:securityhub:getAutomationRule", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupAutomationRuleArgs struct {
	// An Automation Rule Arn is automatically created
	RuleArn string `pulumi:"ruleArn"`
}

type LookupAutomationRuleResult struct {
	Actions []AutomationRulesAction `pulumi:"actions"`
	// The date and time when Automation Rule was created
	CreatedAt *string `pulumi:"createdAt"`
	// The identifier by which created the rule
	CreatedBy *string `pulumi:"createdBy"`
	// The rule criteria for evaluating findings
	Criteria *AutomationRulesFindingFilters `pulumi:"criteria"`
	// Rule description
	Description *string `pulumi:"description"`
	// If Rule is a terminal rule
	IsTerminal *bool `pulumi:"isTerminal"`
	// An Automation Rule Arn is automatically created
	RuleArn *string `pulumi:"ruleArn"`
	// Rule name
	RuleName *string `pulumi:"ruleName"`
	// Rule order value
	RuleOrder *int `pulumi:"ruleOrder"`
	// Status of the Rule upon creation
	RuleStatus *AutomationRuleRuleStatus `pulumi:"ruleStatus"`
	Tags       *AutomationRuleTags       `pulumi:"tags"`
	// The date and time when Automation Rule was last updated
	UpdatedAt *string `pulumi:"updatedAt"`
}

func LookupAutomationRuleOutput(ctx *pulumi.Context, args LookupAutomationRuleOutputArgs, opts ...pulumi.InvokeOption) LookupAutomationRuleResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupAutomationRuleResult, error) {
			args := v.(LookupAutomationRuleArgs)
			r, err := LookupAutomationRule(ctx, &args, opts...)
			var s LookupAutomationRuleResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupAutomationRuleResultOutput)
}

type LookupAutomationRuleOutputArgs struct {
	// An Automation Rule Arn is automatically created
	RuleArn pulumi.StringInput `pulumi:"ruleArn"`
}

func (LookupAutomationRuleOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupAutomationRuleArgs)(nil)).Elem()
}

type LookupAutomationRuleResultOutput struct{ *pulumi.OutputState }

func (LookupAutomationRuleResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupAutomationRuleResult)(nil)).Elem()
}

func (o LookupAutomationRuleResultOutput) ToLookupAutomationRuleResultOutput() LookupAutomationRuleResultOutput {
	return o
}

func (o LookupAutomationRuleResultOutput) ToLookupAutomationRuleResultOutputWithContext(ctx context.Context) LookupAutomationRuleResultOutput {
	return o
}

func (o LookupAutomationRuleResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupAutomationRuleResult] {
	return pulumix.Output[LookupAutomationRuleResult]{
		OutputState: o.OutputState,
	}
}

func (o LookupAutomationRuleResultOutput) Actions() AutomationRulesActionArrayOutput {
	return o.ApplyT(func(v LookupAutomationRuleResult) []AutomationRulesAction { return v.Actions }).(AutomationRulesActionArrayOutput)
}

// The date and time when Automation Rule was created
func (o LookupAutomationRuleResultOutput) CreatedAt() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupAutomationRuleResult) *string { return v.CreatedAt }).(pulumi.StringPtrOutput)
}

// The identifier by which created the rule
func (o LookupAutomationRuleResultOutput) CreatedBy() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupAutomationRuleResult) *string { return v.CreatedBy }).(pulumi.StringPtrOutput)
}

// The rule criteria for evaluating findings
func (o LookupAutomationRuleResultOutput) Criteria() AutomationRulesFindingFiltersPtrOutput {
	return o.ApplyT(func(v LookupAutomationRuleResult) *AutomationRulesFindingFilters { return v.Criteria }).(AutomationRulesFindingFiltersPtrOutput)
}

// Rule description
func (o LookupAutomationRuleResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupAutomationRuleResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

// If Rule is a terminal rule
func (o LookupAutomationRuleResultOutput) IsTerminal() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupAutomationRuleResult) *bool { return v.IsTerminal }).(pulumi.BoolPtrOutput)
}

// An Automation Rule Arn is automatically created
func (o LookupAutomationRuleResultOutput) RuleArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupAutomationRuleResult) *string { return v.RuleArn }).(pulumi.StringPtrOutput)
}

// Rule name
func (o LookupAutomationRuleResultOutput) RuleName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupAutomationRuleResult) *string { return v.RuleName }).(pulumi.StringPtrOutput)
}

// Rule order value
func (o LookupAutomationRuleResultOutput) RuleOrder() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupAutomationRuleResult) *int { return v.RuleOrder }).(pulumi.IntPtrOutput)
}

// Status of the Rule upon creation
func (o LookupAutomationRuleResultOutput) RuleStatus() AutomationRuleRuleStatusPtrOutput {
	return o.ApplyT(func(v LookupAutomationRuleResult) *AutomationRuleRuleStatus { return v.RuleStatus }).(AutomationRuleRuleStatusPtrOutput)
}

func (o LookupAutomationRuleResultOutput) Tags() AutomationRuleTagsPtrOutput {
	return o.ApplyT(func(v LookupAutomationRuleResult) *AutomationRuleTags { return v.Tags }).(AutomationRuleTagsPtrOutput)
}

// The date and time when Automation Rule was last updated
func (o LookupAutomationRuleResultOutput) UpdatedAt() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupAutomationRuleResult) *string { return v.UpdatedAt }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupAutomationRuleResultOutput{})
}
