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

// Resource Type definition for AWS::GameLift::MatchmakingConfiguration
//
// Deprecated: MatchmakingConfiguration is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type MatchmakingConfiguration struct {
	pulumi.CustomResourceState

	AcceptanceRequired       pulumi.BoolOutput                               `pulumi:"acceptanceRequired"`
	AcceptanceTimeoutSeconds pulumi.IntPtrOutput                             `pulumi:"acceptanceTimeoutSeconds"`
	AdditionalPlayerCount    pulumi.IntPtrOutput                             `pulumi:"additionalPlayerCount"`
	Arn                      pulumi.StringOutput                             `pulumi:"arn"`
	BackfillMode             pulumi.StringPtrOutput                          `pulumi:"backfillMode"`
	CustomEventData          pulumi.StringPtrOutput                          `pulumi:"customEventData"`
	Description              pulumi.StringPtrOutput                          `pulumi:"description"`
	FlexMatchMode            pulumi.StringPtrOutput                          `pulumi:"flexMatchMode"`
	GameProperties           MatchmakingConfigurationGamePropertyArrayOutput `pulumi:"gameProperties"`
	GameSessionData          pulumi.StringPtrOutput                          `pulumi:"gameSessionData"`
	GameSessionQueueArns     pulumi.StringArrayOutput                        `pulumi:"gameSessionQueueArns"`
	Name                     pulumi.StringOutput                             `pulumi:"name"`
	NotificationTarget       pulumi.StringPtrOutput                          `pulumi:"notificationTarget"`
	RequestTimeoutSeconds    pulumi.IntOutput                                `pulumi:"requestTimeoutSeconds"`
	RuleSetName              pulumi.StringOutput                             `pulumi:"ruleSetName"`
	Tags                     MatchmakingConfigurationTagArrayOutput          `pulumi:"tags"`
}

// NewMatchmakingConfiguration registers a new resource with the given unique name, arguments, and options.
func NewMatchmakingConfiguration(ctx *pulumi.Context,
	name string, args *MatchmakingConfigurationArgs, opts ...pulumi.ResourceOption) (*MatchmakingConfiguration, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.AcceptanceRequired == nil {
		return nil, errors.New("invalid value for required argument 'AcceptanceRequired'")
	}
	if args.RequestTimeoutSeconds == nil {
		return nil, errors.New("invalid value for required argument 'RequestTimeoutSeconds'")
	}
	if args.RuleSetName == nil {
		return nil, errors.New("invalid value for required argument 'RuleSetName'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"name",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource MatchmakingConfiguration
	err := ctx.RegisterResource("aws-native:gamelift:MatchmakingConfiguration", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetMatchmakingConfiguration gets an existing MatchmakingConfiguration resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetMatchmakingConfiguration(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *MatchmakingConfigurationState, opts ...pulumi.ResourceOption) (*MatchmakingConfiguration, error) {
	var resource MatchmakingConfiguration
	err := ctx.ReadResource("aws-native:gamelift:MatchmakingConfiguration", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering MatchmakingConfiguration resources.
type matchmakingConfigurationState struct {
}

type MatchmakingConfigurationState struct {
}

func (MatchmakingConfigurationState) ElementType() reflect.Type {
	return reflect.TypeOf((*matchmakingConfigurationState)(nil)).Elem()
}

type matchmakingConfigurationArgs struct {
	AcceptanceRequired       bool                                   `pulumi:"acceptanceRequired"`
	AcceptanceTimeoutSeconds *int                                   `pulumi:"acceptanceTimeoutSeconds"`
	AdditionalPlayerCount    *int                                   `pulumi:"additionalPlayerCount"`
	BackfillMode             *string                                `pulumi:"backfillMode"`
	CustomEventData          *string                                `pulumi:"customEventData"`
	Description              *string                                `pulumi:"description"`
	FlexMatchMode            *string                                `pulumi:"flexMatchMode"`
	GameProperties           []MatchmakingConfigurationGameProperty `pulumi:"gameProperties"`
	GameSessionData          *string                                `pulumi:"gameSessionData"`
	GameSessionQueueArns     []string                               `pulumi:"gameSessionQueueArns"`
	Name                     *string                                `pulumi:"name"`
	NotificationTarget       *string                                `pulumi:"notificationTarget"`
	RequestTimeoutSeconds    int                                    `pulumi:"requestTimeoutSeconds"`
	RuleSetName              string                                 `pulumi:"ruleSetName"`
	Tags                     []MatchmakingConfigurationTag          `pulumi:"tags"`
}

// The set of arguments for constructing a MatchmakingConfiguration resource.
type MatchmakingConfigurationArgs struct {
	AcceptanceRequired       pulumi.BoolInput
	AcceptanceTimeoutSeconds pulumi.IntPtrInput
	AdditionalPlayerCount    pulumi.IntPtrInput
	BackfillMode             pulumi.StringPtrInput
	CustomEventData          pulumi.StringPtrInput
	Description              pulumi.StringPtrInput
	FlexMatchMode            pulumi.StringPtrInput
	GameProperties           MatchmakingConfigurationGamePropertyArrayInput
	GameSessionData          pulumi.StringPtrInput
	GameSessionQueueArns     pulumi.StringArrayInput
	Name                     pulumi.StringPtrInput
	NotificationTarget       pulumi.StringPtrInput
	RequestTimeoutSeconds    pulumi.IntInput
	RuleSetName              pulumi.StringInput
	Tags                     MatchmakingConfigurationTagArrayInput
}

func (MatchmakingConfigurationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*matchmakingConfigurationArgs)(nil)).Elem()
}

type MatchmakingConfigurationInput interface {
	pulumi.Input

	ToMatchmakingConfigurationOutput() MatchmakingConfigurationOutput
	ToMatchmakingConfigurationOutputWithContext(ctx context.Context) MatchmakingConfigurationOutput
}

func (*MatchmakingConfiguration) ElementType() reflect.Type {
	return reflect.TypeOf((**MatchmakingConfiguration)(nil)).Elem()
}

func (i *MatchmakingConfiguration) ToMatchmakingConfigurationOutput() MatchmakingConfigurationOutput {
	return i.ToMatchmakingConfigurationOutputWithContext(context.Background())
}

func (i *MatchmakingConfiguration) ToMatchmakingConfigurationOutputWithContext(ctx context.Context) MatchmakingConfigurationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(MatchmakingConfigurationOutput)
}

func (i *MatchmakingConfiguration) ToOutput(ctx context.Context) pulumix.Output[*MatchmakingConfiguration] {
	return pulumix.Output[*MatchmakingConfiguration]{
		OutputState: i.ToMatchmakingConfigurationOutputWithContext(ctx).OutputState,
	}
}

type MatchmakingConfigurationOutput struct{ *pulumi.OutputState }

func (MatchmakingConfigurationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**MatchmakingConfiguration)(nil)).Elem()
}

func (o MatchmakingConfigurationOutput) ToMatchmakingConfigurationOutput() MatchmakingConfigurationOutput {
	return o
}

func (o MatchmakingConfigurationOutput) ToMatchmakingConfigurationOutputWithContext(ctx context.Context) MatchmakingConfigurationOutput {
	return o
}

func (o MatchmakingConfigurationOutput) ToOutput(ctx context.Context) pulumix.Output[*MatchmakingConfiguration] {
	return pulumix.Output[*MatchmakingConfiguration]{
		OutputState: o.OutputState,
	}
}

func (o MatchmakingConfigurationOutput) AcceptanceRequired() pulumi.BoolOutput {
	return o.ApplyT(func(v *MatchmakingConfiguration) pulumi.BoolOutput { return v.AcceptanceRequired }).(pulumi.BoolOutput)
}

func (o MatchmakingConfigurationOutput) AcceptanceTimeoutSeconds() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *MatchmakingConfiguration) pulumi.IntPtrOutput { return v.AcceptanceTimeoutSeconds }).(pulumi.IntPtrOutput)
}

func (o MatchmakingConfigurationOutput) AdditionalPlayerCount() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *MatchmakingConfiguration) pulumi.IntPtrOutput { return v.AdditionalPlayerCount }).(pulumi.IntPtrOutput)
}

func (o MatchmakingConfigurationOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *MatchmakingConfiguration) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

func (o MatchmakingConfigurationOutput) BackfillMode() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *MatchmakingConfiguration) pulumi.StringPtrOutput { return v.BackfillMode }).(pulumi.StringPtrOutput)
}

func (o MatchmakingConfigurationOutput) CustomEventData() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *MatchmakingConfiguration) pulumi.StringPtrOutput { return v.CustomEventData }).(pulumi.StringPtrOutput)
}

func (o MatchmakingConfigurationOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *MatchmakingConfiguration) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

func (o MatchmakingConfigurationOutput) FlexMatchMode() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *MatchmakingConfiguration) pulumi.StringPtrOutput { return v.FlexMatchMode }).(pulumi.StringPtrOutput)
}

func (o MatchmakingConfigurationOutput) GameProperties() MatchmakingConfigurationGamePropertyArrayOutput {
	return o.ApplyT(func(v *MatchmakingConfiguration) MatchmakingConfigurationGamePropertyArrayOutput {
		return v.GameProperties
	}).(MatchmakingConfigurationGamePropertyArrayOutput)
}

func (o MatchmakingConfigurationOutput) GameSessionData() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *MatchmakingConfiguration) pulumi.StringPtrOutput { return v.GameSessionData }).(pulumi.StringPtrOutput)
}

func (o MatchmakingConfigurationOutput) GameSessionQueueArns() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *MatchmakingConfiguration) pulumi.StringArrayOutput { return v.GameSessionQueueArns }).(pulumi.StringArrayOutput)
}

func (o MatchmakingConfigurationOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *MatchmakingConfiguration) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

func (o MatchmakingConfigurationOutput) NotificationTarget() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *MatchmakingConfiguration) pulumi.StringPtrOutput { return v.NotificationTarget }).(pulumi.StringPtrOutput)
}

func (o MatchmakingConfigurationOutput) RequestTimeoutSeconds() pulumi.IntOutput {
	return o.ApplyT(func(v *MatchmakingConfiguration) pulumi.IntOutput { return v.RequestTimeoutSeconds }).(pulumi.IntOutput)
}

func (o MatchmakingConfigurationOutput) RuleSetName() pulumi.StringOutput {
	return o.ApplyT(func(v *MatchmakingConfiguration) pulumi.StringOutput { return v.RuleSetName }).(pulumi.StringOutput)
}

func (o MatchmakingConfigurationOutput) Tags() MatchmakingConfigurationTagArrayOutput {
	return o.ApplyT(func(v *MatchmakingConfiguration) MatchmakingConfigurationTagArrayOutput { return v.Tags }).(MatchmakingConfigurationTagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*MatchmakingConfigurationInput)(nil)).Elem(), &MatchmakingConfiguration{})
	pulumi.RegisterOutputType(MatchmakingConfigurationOutput{})
}
