// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ivs

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::IVS::StreamKey
type StreamKey struct {
	pulumi.CustomResourceState

	// Stream Key ARN is automatically generated on creation and assigned as the unique identifier.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// Channel ARN for the stream.
	ChannelArn pulumi.StringOutput `pulumi:"channelArn"`
	// A list of key-value pairs that contain metadata for the asset model.
	Tags StreamKeyTagArrayOutput `pulumi:"tags"`
	// Stream-key value.
	Value pulumi.StringOutput `pulumi:"value"`
}

// NewStreamKey registers a new resource with the given unique name, arguments, and options.
func NewStreamKey(ctx *pulumi.Context,
	name string, args *StreamKeyArgs, opts ...pulumi.ResourceOption) (*StreamKey, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ChannelArn == nil {
		return nil, errors.New("invalid value for required argument 'ChannelArn'")
	}
	var resource StreamKey
	err := ctx.RegisterResource("aws-native:ivs:StreamKey", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetStreamKey gets an existing StreamKey resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetStreamKey(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *StreamKeyState, opts ...pulumi.ResourceOption) (*StreamKey, error) {
	var resource StreamKey
	err := ctx.ReadResource("aws-native:ivs:StreamKey", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering StreamKey resources.
type streamKeyState struct {
}

type StreamKeyState struct {
}

func (StreamKeyState) ElementType() reflect.Type {
	return reflect.TypeOf((*streamKeyState)(nil)).Elem()
}

type streamKeyArgs struct {
	// Channel ARN for the stream.
	ChannelArn string `pulumi:"channelArn"`
	// A list of key-value pairs that contain metadata for the asset model.
	Tags []StreamKeyTag `pulumi:"tags"`
}

// The set of arguments for constructing a StreamKey resource.
type StreamKeyArgs struct {
	// Channel ARN for the stream.
	ChannelArn pulumi.StringInput
	// A list of key-value pairs that contain metadata for the asset model.
	Tags StreamKeyTagArrayInput
}

func (StreamKeyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*streamKeyArgs)(nil)).Elem()
}

type StreamKeyInput interface {
	pulumi.Input

	ToStreamKeyOutput() StreamKeyOutput
	ToStreamKeyOutputWithContext(ctx context.Context) StreamKeyOutput
}

func (*StreamKey) ElementType() reflect.Type {
	return reflect.TypeOf((**StreamKey)(nil)).Elem()
}

func (i *StreamKey) ToStreamKeyOutput() StreamKeyOutput {
	return i.ToStreamKeyOutputWithContext(context.Background())
}

func (i *StreamKey) ToStreamKeyOutputWithContext(ctx context.Context) StreamKeyOutput {
	return pulumi.ToOutputWithContext(ctx, i).(StreamKeyOutput)
}

type StreamKeyOutput struct{ *pulumi.OutputState }

func (StreamKeyOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**StreamKey)(nil)).Elem()
}

func (o StreamKeyOutput) ToStreamKeyOutput() StreamKeyOutput {
	return o
}

func (o StreamKeyOutput) ToStreamKeyOutputWithContext(ctx context.Context) StreamKeyOutput {
	return o
}

// Stream Key ARN is automatically generated on creation and assigned as the unique identifier.
func (o StreamKeyOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *StreamKey) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

// Channel ARN for the stream.
func (o StreamKeyOutput) ChannelArn() pulumi.StringOutput {
	return o.ApplyT(func(v *StreamKey) pulumi.StringOutput { return v.ChannelArn }).(pulumi.StringOutput)
}

// A list of key-value pairs that contain metadata for the asset model.
func (o StreamKeyOutput) Tags() StreamKeyTagArrayOutput {
	return o.ApplyT(func(v *StreamKey) StreamKeyTagArrayOutput { return v.Tags }).(StreamKeyTagArrayOutput)
}

// Stream-key value.
func (o StreamKeyOutput) Value() pulumi.StringOutput {
	return o.ApplyT(func(v *StreamKey) pulumi.StringOutput { return v.Value }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*StreamKeyInput)(nil)).Elem(), &StreamKey{})
	pulumi.RegisterOutputType(StreamKeyOutput{})
}
