// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package mediatailor

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Definition of AWS::MediaTailor::Channel Resource Type
type Channel struct {
	pulumi.CustomResourceState

	// <p>The ARN of the channel.</p>
	Arn              pulumi.StringOutput                        `pulumi:"arn"`
	ChannelName      pulumi.StringOutput                        `pulumi:"channelName"`
	FillerSlate      ChannelSlateSourcePtrOutput                `pulumi:"fillerSlate"`
	LogConfiguration ChannelLogConfigurationForChannelPtrOutput `pulumi:"logConfiguration"`
	// <p>The channel's output properties.</p>
	Outputs      ChannelRequestOutputItemArrayOutput `pulumi:"outputs"`
	PlaybackMode ChannelPlaybackModeOutput           `pulumi:"playbackMode"`
	// The tags to assign to the channel.
	Tags                   ChannelTagArrayOutput                  `pulumi:"tags"`
	Tier                   ChannelTierPtrOutput                   `pulumi:"tier"`
	TimeShiftConfiguration ChannelTimeShiftConfigurationPtrOutput `pulumi:"timeShiftConfiguration"`
}

// NewChannel registers a new resource with the given unique name, arguments, and options.
func NewChannel(ctx *pulumi.Context,
	name string, args *ChannelArgs, opts ...pulumi.ResourceOption) (*Channel, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Outputs == nil {
		return nil, errors.New("invalid value for required argument 'Outputs'")
	}
	if args.PlaybackMode == nil {
		return nil, errors.New("invalid value for required argument 'PlaybackMode'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"channelName",
		"tier",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Channel
	err := ctx.RegisterResource("aws-native:mediatailor:Channel", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetChannel gets an existing Channel resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetChannel(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ChannelState, opts ...pulumi.ResourceOption) (*Channel, error) {
	var resource Channel
	err := ctx.ReadResource("aws-native:mediatailor:Channel", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Channel resources.
type channelState struct {
}

type ChannelState struct {
}

func (ChannelState) ElementType() reflect.Type {
	return reflect.TypeOf((*channelState)(nil)).Elem()
}

type channelArgs struct {
	ChannelName      *string                            `pulumi:"channelName"`
	FillerSlate      *ChannelSlateSource                `pulumi:"fillerSlate"`
	LogConfiguration *ChannelLogConfigurationForChannel `pulumi:"logConfiguration"`
	// <p>The channel's output properties.</p>
	Outputs      []ChannelRequestOutputItem `pulumi:"outputs"`
	PlaybackMode ChannelPlaybackMode        `pulumi:"playbackMode"`
	// The tags to assign to the channel.
	Tags                   []ChannelTag                   `pulumi:"tags"`
	Tier                   *ChannelTier                   `pulumi:"tier"`
	TimeShiftConfiguration *ChannelTimeShiftConfiguration `pulumi:"timeShiftConfiguration"`
}

// The set of arguments for constructing a Channel resource.
type ChannelArgs struct {
	ChannelName      pulumi.StringPtrInput
	FillerSlate      ChannelSlateSourcePtrInput
	LogConfiguration ChannelLogConfigurationForChannelPtrInput
	// <p>The channel's output properties.</p>
	Outputs      ChannelRequestOutputItemArrayInput
	PlaybackMode ChannelPlaybackModeInput
	// The tags to assign to the channel.
	Tags                   ChannelTagArrayInput
	Tier                   ChannelTierPtrInput
	TimeShiftConfiguration ChannelTimeShiftConfigurationPtrInput
}

func (ChannelArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*channelArgs)(nil)).Elem()
}

type ChannelInput interface {
	pulumi.Input

	ToChannelOutput() ChannelOutput
	ToChannelOutputWithContext(ctx context.Context) ChannelOutput
}

func (*Channel) ElementType() reflect.Type {
	return reflect.TypeOf((**Channel)(nil)).Elem()
}

func (i *Channel) ToChannelOutput() ChannelOutput {
	return i.ToChannelOutputWithContext(context.Background())
}

func (i *Channel) ToChannelOutputWithContext(ctx context.Context) ChannelOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ChannelOutput)
}

func (i *Channel) ToOutput(ctx context.Context) pulumix.Output[*Channel] {
	return pulumix.Output[*Channel]{
		OutputState: i.ToChannelOutputWithContext(ctx).OutputState,
	}
}

type ChannelOutput struct{ *pulumi.OutputState }

func (ChannelOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Channel)(nil)).Elem()
}

func (o ChannelOutput) ToChannelOutput() ChannelOutput {
	return o
}

func (o ChannelOutput) ToChannelOutputWithContext(ctx context.Context) ChannelOutput {
	return o
}

func (o ChannelOutput) ToOutput(ctx context.Context) pulumix.Output[*Channel] {
	return pulumix.Output[*Channel]{
		OutputState: o.OutputState,
	}
}

// <p>The ARN of the channel.</p>
func (o ChannelOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *Channel) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

func (o ChannelOutput) ChannelName() pulumi.StringOutput {
	return o.ApplyT(func(v *Channel) pulumi.StringOutput { return v.ChannelName }).(pulumi.StringOutput)
}

func (o ChannelOutput) FillerSlate() ChannelSlateSourcePtrOutput {
	return o.ApplyT(func(v *Channel) ChannelSlateSourcePtrOutput { return v.FillerSlate }).(ChannelSlateSourcePtrOutput)
}

func (o ChannelOutput) LogConfiguration() ChannelLogConfigurationForChannelPtrOutput {
	return o.ApplyT(func(v *Channel) ChannelLogConfigurationForChannelPtrOutput { return v.LogConfiguration }).(ChannelLogConfigurationForChannelPtrOutput)
}

// <p>The channel's output properties.</p>
func (o ChannelOutput) Outputs() ChannelRequestOutputItemArrayOutput {
	return o.ApplyT(func(v *Channel) ChannelRequestOutputItemArrayOutput { return v.Outputs }).(ChannelRequestOutputItemArrayOutput)
}

func (o ChannelOutput) PlaybackMode() ChannelPlaybackModeOutput {
	return o.ApplyT(func(v *Channel) ChannelPlaybackModeOutput { return v.PlaybackMode }).(ChannelPlaybackModeOutput)
}

// The tags to assign to the channel.
func (o ChannelOutput) Tags() ChannelTagArrayOutput {
	return o.ApplyT(func(v *Channel) ChannelTagArrayOutput { return v.Tags }).(ChannelTagArrayOutput)
}

func (o ChannelOutput) Tier() ChannelTierPtrOutput {
	return o.ApplyT(func(v *Channel) ChannelTierPtrOutput { return v.Tier }).(ChannelTierPtrOutput)
}

func (o ChannelOutput) TimeShiftConfiguration() ChannelTimeShiftConfigurationPtrOutput {
	return o.ApplyT(func(v *Channel) ChannelTimeShiftConfigurationPtrOutput { return v.TimeShiftConfiguration }).(ChannelTimeShiftConfigurationPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ChannelInput)(nil)).Elem(), &Channel{})
	pulumi.RegisterOutputType(ChannelOutput{})
}
