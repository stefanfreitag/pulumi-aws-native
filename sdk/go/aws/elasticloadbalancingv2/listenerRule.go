// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package elasticloadbalancingv2

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::ElasticLoadBalancingV2::ListenerRule
type ListenerRule struct {
	pulumi.CustomResourceState

	Actions     ListenerRuleActionArrayOutput        `pulumi:"actions"`
	Conditions  ListenerRuleRuleConditionArrayOutput `pulumi:"conditions"`
	IsDefault   pulumi.BoolOutput                    `pulumi:"isDefault"`
	ListenerArn pulumi.StringPtrOutput               `pulumi:"listenerArn"`
	Priority    pulumi.IntOutput                     `pulumi:"priority"`
	RuleArn     pulumi.StringOutput                  `pulumi:"ruleArn"`
}

// NewListenerRule registers a new resource with the given unique name, arguments, and options.
func NewListenerRule(ctx *pulumi.Context,
	name string, args *ListenerRuleArgs, opts ...pulumi.ResourceOption) (*ListenerRule, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Actions == nil {
		return nil, errors.New("invalid value for required argument 'Actions'")
	}
	if args.Conditions == nil {
		return nil, errors.New("invalid value for required argument 'Conditions'")
	}
	if args.Priority == nil {
		return nil, errors.New("invalid value for required argument 'Priority'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"listenerArn",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource ListenerRule
	err := ctx.RegisterResource("aws-native:elasticloadbalancingv2:ListenerRule", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetListenerRule gets an existing ListenerRule resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetListenerRule(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ListenerRuleState, opts ...pulumi.ResourceOption) (*ListenerRule, error) {
	var resource ListenerRule
	err := ctx.ReadResource("aws-native:elasticloadbalancingv2:ListenerRule", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ListenerRule resources.
type listenerRuleState struct {
}

type ListenerRuleState struct {
}

func (ListenerRuleState) ElementType() reflect.Type {
	return reflect.TypeOf((*listenerRuleState)(nil)).Elem()
}

type listenerRuleArgs struct {
	Actions     []ListenerRuleAction        `pulumi:"actions"`
	Conditions  []ListenerRuleRuleCondition `pulumi:"conditions"`
	ListenerArn *string                     `pulumi:"listenerArn"`
	Priority    int                         `pulumi:"priority"`
}

// The set of arguments for constructing a ListenerRule resource.
type ListenerRuleArgs struct {
	Actions     ListenerRuleActionArrayInput
	Conditions  ListenerRuleRuleConditionArrayInput
	ListenerArn pulumi.StringPtrInput
	Priority    pulumi.IntInput
}

func (ListenerRuleArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*listenerRuleArgs)(nil)).Elem()
}

type ListenerRuleInput interface {
	pulumi.Input

	ToListenerRuleOutput() ListenerRuleOutput
	ToListenerRuleOutputWithContext(ctx context.Context) ListenerRuleOutput
}

func (*ListenerRule) ElementType() reflect.Type {
	return reflect.TypeOf((**ListenerRule)(nil)).Elem()
}

func (i *ListenerRule) ToListenerRuleOutput() ListenerRuleOutput {
	return i.ToListenerRuleOutputWithContext(context.Background())
}

func (i *ListenerRule) ToListenerRuleOutputWithContext(ctx context.Context) ListenerRuleOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ListenerRuleOutput)
}

func (i *ListenerRule) ToOutput(ctx context.Context) pulumix.Output[*ListenerRule] {
	return pulumix.Output[*ListenerRule]{
		OutputState: i.ToListenerRuleOutputWithContext(ctx).OutputState,
	}
}

type ListenerRuleOutput struct{ *pulumi.OutputState }

func (ListenerRuleOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ListenerRule)(nil)).Elem()
}

func (o ListenerRuleOutput) ToListenerRuleOutput() ListenerRuleOutput {
	return o
}

func (o ListenerRuleOutput) ToListenerRuleOutputWithContext(ctx context.Context) ListenerRuleOutput {
	return o
}

func (o ListenerRuleOutput) ToOutput(ctx context.Context) pulumix.Output[*ListenerRule] {
	return pulumix.Output[*ListenerRule]{
		OutputState: o.OutputState,
	}
}

func (o ListenerRuleOutput) Actions() ListenerRuleActionArrayOutput {
	return o.ApplyT(func(v *ListenerRule) ListenerRuleActionArrayOutput { return v.Actions }).(ListenerRuleActionArrayOutput)
}

func (o ListenerRuleOutput) Conditions() ListenerRuleRuleConditionArrayOutput {
	return o.ApplyT(func(v *ListenerRule) ListenerRuleRuleConditionArrayOutput { return v.Conditions }).(ListenerRuleRuleConditionArrayOutput)
}

func (o ListenerRuleOutput) IsDefault() pulumi.BoolOutput {
	return o.ApplyT(func(v *ListenerRule) pulumi.BoolOutput { return v.IsDefault }).(pulumi.BoolOutput)
}

func (o ListenerRuleOutput) ListenerArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ListenerRule) pulumi.StringPtrOutput { return v.ListenerArn }).(pulumi.StringPtrOutput)
}

func (o ListenerRuleOutput) Priority() pulumi.IntOutput {
	return o.ApplyT(func(v *ListenerRule) pulumi.IntOutput { return v.Priority }).(pulumi.IntOutput)
}

func (o ListenerRuleOutput) RuleArn() pulumi.StringOutput {
	return o.ApplyT(func(v *ListenerRule) pulumi.StringOutput { return v.RuleArn }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ListenerRuleInput)(nil)).Elem(), &ListenerRule{})
	pulumi.RegisterOutputType(ListenerRuleOutput{})
}
