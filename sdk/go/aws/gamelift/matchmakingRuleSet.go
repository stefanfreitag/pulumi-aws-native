// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package gamelift

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// The AWS::GameLift::MatchmakingRuleSet resource creates an Amazon GameLift (GameLift) matchmaking rule set.
type MatchmakingRuleSet struct {
	pulumi.CustomResourceState

	// The Amazon Resource Name (ARN) that is assigned to a Amazon GameLift matchmaking rule set resource and uniquely identifies it.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds.
	CreationTime pulumi.StringOutput `pulumi:"creationTime"`
	// A unique identifier for the matchmaking rule set.
	Name pulumi.StringOutput `pulumi:"name"`
	// A collection of matchmaking rules, formatted as a JSON string.
	RuleSetBody pulumi.StringOutput `pulumi:"ruleSetBody"`
	// An array of key-value pairs to apply to this resource.
	Tags MatchmakingRuleSetTagArrayOutput `pulumi:"tags"`
}

// NewMatchmakingRuleSet registers a new resource with the given unique name, arguments, and options.
func NewMatchmakingRuleSet(ctx *pulumi.Context,
	name string, args *MatchmakingRuleSetArgs, opts ...pulumi.ResourceOption) (*MatchmakingRuleSet, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.RuleSetBody == nil {
		return nil, errors.New("invalid value for required argument 'RuleSetBody'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"name",
		"ruleSetBody",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource MatchmakingRuleSet
	err := ctx.RegisterResource("aws-native:gamelift:MatchmakingRuleSet", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetMatchmakingRuleSet gets an existing MatchmakingRuleSet resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetMatchmakingRuleSet(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *MatchmakingRuleSetState, opts ...pulumi.ResourceOption) (*MatchmakingRuleSet, error) {
	var resource MatchmakingRuleSet
	err := ctx.ReadResource("aws-native:gamelift:MatchmakingRuleSet", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering MatchmakingRuleSet resources.
type matchmakingRuleSetState struct {
}

type MatchmakingRuleSetState struct {
}

func (MatchmakingRuleSetState) ElementType() reflect.Type {
	return reflect.TypeOf((*matchmakingRuleSetState)(nil)).Elem()
}

type matchmakingRuleSetArgs struct {
	// A unique identifier for the matchmaking rule set.
	Name *string `pulumi:"name"`
	// A collection of matchmaking rules, formatted as a JSON string.
	RuleSetBody string `pulumi:"ruleSetBody"`
	// An array of key-value pairs to apply to this resource.
	Tags []MatchmakingRuleSetTag `pulumi:"tags"`
}

// The set of arguments for constructing a MatchmakingRuleSet resource.
type MatchmakingRuleSetArgs struct {
	// A unique identifier for the matchmaking rule set.
	Name pulumi.StringPtrInput
	// A collection of matchmaking rules, formatted as a JSON string.
	RuleSetBody pulumi.StringInput
	// An array of key-value pairs to apply to this resource.
	Tags MatchmakingRuleSetTagArrayInput
}

func (MatchmakingRuleSetArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*matchmakingRuleSetArgs)(nil)).Elem()
}

type MatchmakingRuleSetInput interface {
	pulumi.Input

	ToMatchmakingRuleSetOutput() MatchmakingRuleSetOutput
	ToMatchmakingRuleSetOutputWithContext(ctx context.Context) MatchmakingRuleSetOutput
}

func (*MatchmakingRuleSet) ElementType() reflect.Type {
	return reflect.TypeOf((**MatchmakingRuleSet)(nil)).Elem()
}

func (i *MatchmakingRuleSet) ToMatchmakingRuleSetOutput() MatchmakingRuleSetOutput {
	return i.ToMatchmakingRuleSetOutputWithContext(context.Background())
}

func (i *MatchmakingRuleSet) ToMatchmakingRuleSetOutputWithContext(ctx context.Context) MatchmakingRuleSetOutput {
	return pulumi.ToOutputWithContext(ctx, i).(MatchmakingRuleSetOutput)
}

func (i *MatchmakingRuleSet) ToOutput(ctx context.Context) pulumix.Output[*MatchmakingRuleSet] {
	return pulumix.Output[*MatchmakingRuleSet]{
		OutputState: i.ToMatchmakingRuleSetOutputWithContext(ctx).OutputState,
	}
}

type MatchmakingRuleSetOutput struct{ *pulumi.OutputState }

func (MatchmakingRuleSetOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**MatchmakingRuleSet)(nil)).Elem()
}

func (o MatchmakingRuleSetOutput) ToMatchmakingRuleSetOutput() MatchmakingRuleSetOutput {
	return o
}

func (o MatchmakingRuleSetOutput) ToMatchmakingRuleSetOutputWithContext(ctx context.Context) MatchmakingRuleSetOutput {
	return o
}

func (o MatchmakingRuleSetOutput) ToOutput(ctx context.Context) pulumix.Output[*MatchmakingRuleSet] {
	return pulumix.Output[*MatchmakingRuleSet]{
		OutputState: o.OutputState,
	}
}

// The Amazon Resource Name (ARN) that is assigned to a Amazon GameLift matchmaking rule set resource and uniquely identifies it.
func (o MatchmakingRuleSetOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *MatchmakingRuleSet) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

// A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds.
func (o MatchmakingRuleSetOutput) CreationTime() pulumi.StringOutput {
	return o.ApplyT(func(v *MatchmakingRuleSet) pulumi.StringOutput { return v.CreationTime }).(pulumi.StringOutput)
}

// A unique identifier for the matchmaking rule set.
func (o MatchmakingRuleSetOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *MatchmakingRuleSet) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// A collection of matchmaking rules, formatted as a JSON string.
func (o MatchmakingRuleSetOutput) RuleSetBody() pulumi.StringOutput {
	return o.ApplyT(func(v *MatchmakingRuleSet) pulumi.StringOutput { return v.RuleSetBody }).(pulumi.StringOutput)
}

// An array of key-value pairs to apply to this resource.
func (o MatchmakingRuleSetOutput) Tags() MatchmakingRuleSetTagArrayOutput {
	return o.ApplyT(func(v *MatchmakingRuleSet) MatchmakingRuleSetTagArrayOutput { return v.Tags }).(MatchmakingRuleSetTagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*MatchmakingRuleSetInput)(nil)).Elem(), &MatchmakingRuleSet{})
	pulumi.RegisterOutputType(MatchmakingRuleSetOutput{})
}
