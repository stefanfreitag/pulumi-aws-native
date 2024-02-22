// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package wafv2

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Contains the Rules that identify the requests that you want to allow, block, or count. In a RuleGroup, you also specify a default action (ALLOW or BLOCK), and the action for each Rule that you add to a RuleGroup, for example, block requests from specified IP addresses or block requests from specified referrers. You also associate the RuleGroup with a CloudFront distribution to identify the requests that you want AWS WAF to filter. If you add more than one Rule to a RuleGroup, a request needs to match only one of the specifications to be allowed, blocked, or counted.
type RuleGroup struct {
	pulumi.CustomResourceState

	Arn pulumi.StringOutput `pulumi:"arn"`
	// Collection of Available Labels.
	AvailableLabels RuleGroupLabelSummaryArrayOutput `pulumi:"availableLabels"`
	Capacity        pulumi.IntOutput                 `pulumi:"capacity"`
	// Collection of Consumed Labels.
	ConsumedLabels       RuleGroupLabelSummaryArrayOutput       `pulumi:"consumedLabels"`
	CustomResponseBodies RuleGroupCustomResponseBodiesPtrOutput `pulumi:"customResponseBodies"`
	Description          pulumi.StringPtrOutput                 `pulumi:"description"`
	LabelNamespace       pulumi.StringOutput                    `pulumi:"labelNamespace"`
	Name                 pulumi.StringPtrOutput                 `pulumi:"name"`
	// Collection of Rules.
	Rules            RuleGroupRuleArrayOutput        `pulumi:"rules"`
	Scope            RuleGroupScopeOutput            `pulumi:"scope"`
	Tags             aws.TagArrayOutput              `pulumi:"tags"`
	VisibilityConfig RuleGroupVisibilityConfigOutput `pulumi:"visibilityConfig"`
}

// NewRuleGroup registers a new resource with the given unique name, arguments, and options.
func NewRuleGroup(ctx *pulumi.Context,
	name string, args *RuleGroupArgs, opts ...pulumi.ResourceOption) (*RuleGroup, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Capacity == nil {
		return nil, errors.New("invalid value for required argument 'Capacity'")
	}
	if args.Scope == nil {
		return nil, errors.New("invalid value for required argument 'Scope'")
	}
	if args.VisibilityConfig == nil {
		return nil, errors.New("invalid value for required argument 'VisibilityConfig'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"name",
		"scope",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource RuleGroup
	err := ctx.RegisterResource("aws-native:wafv2:RuleGroup", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetRuleGroup gets an existing RuleGroup resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetRuleGroup(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *RuleGroupState, opts ...pulumi.ResourceOption) (*RuleGroup, error) {
	var resource RuleGroup
	err := ctx.ReadResource("aws-native:wafv2:RuleGroup", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering RuleGroup resources.
type ruleGroupState struct {
}

type RuleGroupState struct {
}

func (RuleGroupState) ElementType() reflect.Type {
	return reflect.TypeOf((*ruleGroupState)(nil)).Elem()
}

type ruleGroupArgs struct {
	// Collection of Available Labels.
	AvailableLabels []RuleGroupLabelSummary `pulumi:"availableLabels"`
	Capacity        int                     `pulumi:"capacity"`
	// Collection of Consumed Labels.
	ConsumedLabels       []RuleGroupLabelSummary        `pulumi:"consumedLabels"`
	CustomResponseBodies *RuleGroupCustomResponseBodies `pulumi:"customResponseBodies"`
	Description          *string                        `pulumi:"description"`
	Name                 *string                        `pulumi:"name"`
	// Collection of Rules.
	Rules            []RuleGroupRule           `pulumi:"rules"`
	Scope            RuleGroupScope            `pulumi:"scope"`
	Tags             []aws.Tag                 `pulumi:"tags"`
	VisibilityConfig RuleGroupVisibilityConfig `pulumi:"visibilityConfig"`
}

// The set of arguments for constructing a RuleGroup resource.
type RuleGroupArgs struct {
	// Collection of Available Labels.
	AvailableLabels RuleGroupLabelSummaryArrayInput
	Capacity        pulumi.IntInput
	// Collection of Consumed Labels.
	ConsumedLabels       RuleGroupLabelSummaryArrayInput
	CustomResponseBodies RuleGroupCustomResponseBodiesPtrInput
	Description          pulumi.StringPtrInput
	Name                 pulumi.StringPtrInput
	// Collection of Rules.
	Rules            RuleGroupRuleArrayInput
	Scope            RuleGroupScopeInput
	Tags             aws.TagArrayInput
	VisibilityConfig RuleGroupVisibilityConfigInput
}

func (RuleGroupArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ruleGroupArgs)(nil)).Elem()
}

type RuleGroupInput interface {
	pulumi.Input

	ToRuleGroupOutput() RuleGroupOutput
	ToRuleGroupOutputWithContext(ctx context.Context) RuleGroupOutput
}

func (*RuleGroup) ElementType() reflect.Type {
	return reflect.TypeOf((**RuleGroup)(nil)).Elem()
}

func (i *RuleGroup) ToRuleGroupOutput() RuleGroupOutput {
	return i.ToRuleGroupOutputWithContext(context.Background())
}

func (i *RuleGroup) ToRuleGroupOutputWithContext(ctx context.Context) RuleGroupOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RuleGroupOutput)
}

type RuleGroupOutput struct{ *pulumi.OutputState }

func (RuleGroupOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**RuleGroup)(nil)).Elem()
}

func (o RuleGroupOutput) ToRuleGroupOutput() RuleGroupOutput {
	return o
}

func (o RuleGroupOutput) ToRuleGroupOutputWithContext(ctx context.Context) RuleGroupOutput {
	return o
}

func (o RuleGroupOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *RuleGroup) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

// Collection of Available Labels.
func (o RuleGroupOutput) AvailableLabels() RuleGroupLabelSummaryArrayOutput {
	return o.ApplyT(func(v *RuleGroup) RuleGroupLabelSummaryArrayOutput { return v.AvailableLabels }).(RuleGroupLabelSummaryArrayOutput)
}

func (o RuleGroupOutput) Capacity() pulumi.IntOutput {
	return o.ApplyT(func(v *RuleGroup) pulumi.IntOutput { return v.Capacity }).(pulumi.IntOutput)
}

// Collection of Consumed Labels.
func (o RuleGroupOutput) ConsumedLabels() RuleGroupLabelSummaryArrayOutput {
	return o.ApplyT(func(v *RuleGroup) RuleGroupLabelSummaryArrayOutput { return v.ConsumedLabels }).(RuleGroupLabelSummaryArrayOutput)
}

func (o RuleGroupOutput) CustomResponseBodies() RuleGroupCustomResponseBodiesPtrOutput {
	return o.ApplyT(func(v *RuleGroup) RuleGroupCustomResponseBodiesPtrOutput { return v.CustomResponseBodies }).(RuleGroupCustomResponseBodiesPtrOutput)
}

func (o RuleGroupOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *RuleGroup) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

func (o RuleGroupOutput) LabelNamespace() pulumi.StringOutput {
	return o.ApplyT(func(v *RuleGroup) pulumi.StringOutput { return v.LabelNamespace }).(pulumi.StringOutput)
}

func (o RuleGroupOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *RuleGroup) pulumi.StringPtrOutput { return v.Name }).(pulumi.StringPtrOutput)
}

// Collection of Rules.
func (o RuleGroupOutput) Rules() RuleGroupRuleArrayOutput {
	return o.ApplyT(func(v *RuleGroup) RuleGroupRuleArrayOutput { return v.Rules }).(RuleGroupRuleArrayOutput)
}

func (o RuleGroupOutput) Scope() RuleGroupScopeOutput {
	return o.ApplyT(func(v *RuleGroup) RuleGroupScopeOutput { return v.Scope }).(RuleGroupScopeOutput)
}

func (o RuleGroupOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v *RuleGroup) aws.TagArrayOutput { return v.Tags }).(aws.TagArrayOutput)
}

func (o RuleGroupOutput) VisibilityConfig() RuleGroupVisibilityConfigOutput {
	return o.ApplyT(func(v *RuleGroup) RuleGroupVisibilityConfigOutput { return v.VisibilityConfig }).(RuleGroupVisibilityConfigOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*RuleGroupInput)(nil)).Elem(), &RuleGroup{})
	pulumi.RegisterOutputType(RuleGroupOutput{})
}
