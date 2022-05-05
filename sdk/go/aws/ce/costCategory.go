// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ce

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Cost Category enables you to map your cost and usage into meaningful categories. You can use Cost Category to organize your costs using a rule-based engine.
type CostCategory struct {
	pulumi.CustomResourceState

	// Cost category ARN
	Arn pulumi.StringOutput `pulumi:"arn"`
	// The default value for the cost category
	DefaultValue   pulumi.StringPtrOutput        `pulumi:"defaultValue"`
	EffectiveStart pulumi.StringOutput           `pulumi:"effectiveStart"`
	Name           pulumi.StringOutput           `pulumi:"name"`
	RuleVersion    CostCategoryRuleVersionOutput `pulumi:"ruleVersion"`
	// JSON array format of Expression in Billing and Cost Management API
	Rules pulumi.StringOutput `pulumi:"rules"`
	// Json array format of CostCategorySplitChargeRule in Billing and Cost Management API
	SplitChargeRules pulumi.StringPtrOutput `pulumi:"splitChargeRules"`
}

// NewCostCategory registers a new resource with the given unique name, arguments, and options.
func NewCostCategory(ctx *pulumi.Context,
	name string, args *CostCategoryArgs, opts ...pulumi.ResourceOption) (*CostCategory, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.RuleVersion == nil {
		return nil, errors.New("invalid value for required argument 'RuleVersion'")
	}
	if args.Rules == nil {
		return nil, errors.New("invalid value for required argument 'Rules'")
	}
	var resource CostCategory
	err := ctx.RegisterResource("aws-native:ce:CostCategory", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetCostCategory gets an existing CostCategory resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetCostCategory(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *CostCategoryState, opts ...pulumi.ResourceOption) (*CostCategory, error) {
	var resource CostCategory
	err := ctx.ReadResource("aws-native:ce:CostCategory", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering CostCategory resources.
type costCategoryState struct {
}

type CostCategoryState struct {
}

func (CostCategoryState) ElementType() reflect.Type {
	return reflect.TypeOf((*costCategoryState)(nil)).Elem()
}

type costCategoryArgs struct {
	// The default value for the cost category
	DefaultValue *string                 `pulumi:"defaultValue"`
	Name         *string                 `pulumi:"name"`
	RuleVersion  CostCategoryRuleVersion `pulumi:"ruleVersion"`
	// JSON array format of Expression in Billing and Cost Management API
	Rules string `pulumi:"rules"`
	// Json array format of CostCategorySplitChargeRule in Billing and Cost Management API
	SplitChargeRules *string `pulumi:"splitChargeRules"`
}

// The set of arguments for constructing a CostCategory resource.
type CostCategoryArgs struct {
	// The default value for the cost category
	DefaultValue pulumi.StringPtrInput
	Name         pulumi.StringPtrInput
	RuleVersion  CostCategoryRuleVersionInput
	// JSON array format of Expression in Billing and Cost Management API
	Rules pulumi.StringInput
	// Json array format of CostCategorySplitChargeRule in Billing and Cost Management API
	SplitChargeRules pulumi.StringPtrInput
}

func (CostCategoryArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*costCategoryArgs)(nil)).Elem()
}

type CostCategoryInput interface {
	pulumi.Input

	ToCostCategoryOutput() CostCategoryOutput
	ToCostCategoryOutputWithContext(ctx context.Context) CostCategoryOutput
}

func (*CostCategory) ElementType() reflect.Type {
	return reflect.TypeOf((**CostCategory)(nil)).Elem()
}

func (i *CostCategory) ToCostCategoryOutput() CostCategoryOutput {
	return i.ToCostCategoryOutputWithContext(context.Background())
}

func (i *CostCategory) ToCostCategoryOutputWithContext(ctx context.Context) CostCategoryOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CostCategoryOutput)
}

type CostCategoryOutput struct{ *pulumi.OutputState }

func (CostCategoryOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**CostCategory)(nil)).Elem()
}

func (o CostCategoryOutput) ToCostCategoryOutput() CostCategoryOutput {
	return o
}

func (o CostCategoryOutput) ToCostCategoryOutputWithContext(ctx context.Context) CostCategoryOutput {
	return o
}

// Cost category ARN
func (o CostCategoryOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *CostCategory) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

// The default value for the cost category
func (o CostCategoryOutput) DefaultValue() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *CostCategory) pulumi.StringPtrOutput { return v.DefaultValue }).(pulumi.StringPtrOutput)
}

func (o CostCategoryOutput) EffectiveStart() pulumi.StringOutput {
	return o.ApplyT(func(v *CostCategory) pulumi.StringOutput { return v.EffectiveStart }).(pulumi.StringOutput)
}

func (o CostCategoryOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *CostCategory) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

func (o CostCategoryOutput) RuleVersion() CostCategoryRuleVersionOutput {
	return o.ApplyT(func(v *CostCategory) CostCategoryRuleVersionOutput { return v.RuleVersion }).(CostCategoryRuleVersionOutput)
}

// JSON array format of Expression in Billing and Cost Management API
func (o CostCategoryOutput) Rules() pulumi.StringOutput {
	return o.ApplyT(func(v *CostCategory) pulumi.StringOutput { return v.Rules }).(pulumi.StringOutput)
}

// Json array format of CostCategorySplitChargeRule in Billing and Cost Management API
func (o CostCategoryOutput) SplitChargeRules() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *CostCategory) pulumi.StringPtrOutput { return v.SplitChargeRules }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*CostCategoryInput)(nil)).Elem(), &CostCategory{})
	pulumi.RegisterOutputType(CostCategoryOutput{})
}
