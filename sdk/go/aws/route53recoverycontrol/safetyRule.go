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
type SafetyRule struct {
	pulumi.CustomResourceState

	AssertionRule SafetyRuleAssertionRulePtrOutput `pulumi:"assertionRule"`
	// The Amazon Resource Name (ARN) of the control panel.
	ControlPanelArn pulumi.StringPtrOutput        `pulumi:"controlPanelArn"`
	GatingRule      SafetyRuleGatingRulePtrOutput `pulumi:"gatingRule"`
	Name            pulumi.StringPtrOutput        `pulumi:"name"`
	RuleConfig      SafetyRuleRuleConfigPtrOutput `pulumi:"ruleConfig"`
	// The Amazon Resource Name (ARN) of the safety rule.
	SafetyRuleArn pulumi.StringOutput `pulumi:"safetyRuleArn"`
	// The deployment status of the routing control. Status can be one of the following: PENDING, DEPLOYED, PENDING_DELETION.
	Status SafetyRuleStatusOutput `pulumi:"status"`
	// A collection of tags associated with a resource
	Tags SafetyRuleTagArrayOutput `pulumi:"tags"`
}

// NewSafetyRule registers a new resource with the given unique name, arguments, and options.
func NewSafetyRule(ctx *pulumi.Context,
	name string, args *SafetyRuleArgs, opts ...pulumi.ResourceOption) (*SafetyRule, error) {
	if args == nil {
		args = &SafetyRuleArgs{}
	}

	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"controlPanelArn",
		"ruleConfig",
		"tags[*]",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource SafetyRule
	err := ctx.RegisterResource("aws-native:route53recoverycontrol:SafetyRule", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSafetyRule gets an existing SafetyRule resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSafetyRule(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SafetyRuleState, opts ...pulumi.ResourceOption) (*SafetyRule, error) {
	var resource SafetyRule
	err := ctx.ReadResource("aws-native:route53recoverycontrol:SafetyRule", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering SafetyRule resources.
type safetyRuleState struct {
}

type SafetyRuleState struct {
}

func (SafetyRuleState) ElementType() reflect.Type {
	return reflect.TypeOf((*safetyRuleState)(nil)).Elem()
}

type safetyRuleArgs struct {
	AssertionRule *SafetyRuleAssertionRule `pulumi:"assertionRule"`
	// The Amazon Resource Name (ARN) of the control panel.
	ControlPanelArn *string               `pulumi:"controlPanelArn"`
	GatingRule      *SafetyRuleGatingRule `pulumi:"gatingRule"`
	Name            *string               `pulumi:"name"`
	RuleConfig      *SafetyRuleRuleConfig `pulumi:"ruleConfig"`
	// A collection of tags associated with a resource
	Tags []SafetyRuleTag `pulumi:"tags"`
}

// The set of arguments for constructing a SafetyRule resource.
type SafetyRuleArgs struct {
	AssertionRule SafetyRuleAssertionRulePtrInput
	// The Amazon Resource Name (ARN) of the control panel.
	ControlPanelArn pulumi.StringPtrInput
	GatingRule      SafetyRuleGatingRulePtrInput
	Name            pulumi.StringPtrInput
	RuleConfig      SafetyRuleRuleConfigPtrInput
	// A collection of tags associated with a resource
	Tags SafetyRuleTagArrayInput
}

func (SafetyRuleArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*safetyRuleArgs)(nil)).Elem()
}

type SafetyRuleInput interface {
	pulumi.Input

	ToSafetyRuleOutput() SafetyRuleOutput
	ToSafetyRuleOutputWithContext(ctx context.Context) SafetyRuleOutput
}

func (*SafetyRule) ElementType() reflect.Type {
	return reflect.TypeOf((**SafetyRule)(nil)).Elem()
}

func (i *SafetyRule) ToSafetyRuleOutput() SafetyRuleOutput {
	return i.ToSafetyRuleOutputWithContext(context.Background())
}

func (i *SafetyRule) ToSafetyRuleOutputWithContext(ctx context.Context) SafetyRuleOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SafetyRuleOutput)
}

func (i *SafetyRule) ToOutput(ctx context.Context) pulumix.Output[*SafetyRule] {
	return pulumix.Output[*SafetyRule]{
		OutputState: i.ToSafetyRuleOutputWithContext(ctx).OutputState,
	}
}

type SafetyRuleOutput struct{ *pulumi.OutputState }

func (SafetyRuleOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**SafetyRule)(nil)).Elem()
}

func (o SafetyRuleOutput) ToSafetyRuleOutput() SafetyRuleOutput {
	return o
}

func (o SafetyRuleOutput) ToSafetyRuleOutputWithContext(ctx context.Context) SafetyRuleOutput {
	return o
}

func (o SafetyRuleOutput) ToOutput(ctx context.Context) pulumix.Output[*SafetyRule] {
	return pulumix.Output[*SafetyRule]{
		OutputState: o.OutputState,
	}
}

func (o SafetyRuleOutput) AssertionRule() SafetyRuleAssertionRulePtrOutput {
	return o.ApplyT(func(v *SafetyRule) SafetyRuleAssertionRulePtrOutput { return v.AssertionRule }).(SafetyRuleAssertionRulePtrOutput)
}

// The Amazon Resource Name (ARN) of the control panel.
func (o SafetyRuleOutput) ControlPanelArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *SafetyRule) pulumi.StringPtrOutput { return v.ControlPanelArn }).(pulumi.StringPtrOutput)
}

func (o SafetyRuleOutput) GatingRule() SafetyRuleGatingRulePtrOutput {
	return o.ApplyT(func(v *SafetyRule) SafetyRuleGatingRulePtrOutput { return v.GatingRule }).(SafetyRuleGatingRulePtrOutput)
}

func (o SafetyRuleOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *SafetyRule) pulumi.StringPtrOutput { return v.Name }).(pulumi.StringPtrOutput)
}

func (o SafetyRuleOutput) RuleConfig() SafetyRuleRuleConfigPtrOutput {
	return o.ApplyT(func(v *SafetyRule) SafetyRuleRuleConfigPtrOutput { return v.RuleConfig }).(SafetyRuleRuleConfigPtrOutput)
}

// The Amazon Resource Name (ARN) of the safety rule.
func (o SafetyRuleOutput) SafetyRuleArn() pulumi.StringOutput {
	return o.ApplyT(func(v *SafetyRule) pulumi.StringOutput { return v.SafetyRuleArn }).(pulumi.StringOutput)
}

// The deployment status of the routing control. Status can be one of the following: PENDING, DEPLOYED, PENDING_DELETION.
func (o SafetyRuleOutput) Status() SafetyRuleStatusOutput {
	return o.ApplyT(func(v *SafetyRule) SafetyRuleStatusOutput { return v.Status }).(SafetyRuleStatusOutput)
}

// A collection of tags associated with a resource
func (o SafetyRuleOutput) Tags() SafetyRuleTagArrayOutput {
	return o.ApplyT(func(v *SafetyRule) SafetyRuleTagArrayOutput { return v.Tags }).(SafetyRuleTagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*SafetyRuleInput)(nil)).Elem(), &SafetyRule{})
	pulumi.RegisterOutputType(SafetyRuleOutput{})
}
