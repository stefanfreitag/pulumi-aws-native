// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package groundstation

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// AWS Ground Station Mission Profile resource type for CloudFormation.
type MissionProfile struct {
	pulumi.CustomResourceState

	Arn pulumi.StringOutput `pulumi:"arn"`
	// Post-pass time needed after the contact.
	ContactPostPassDurationSeconds pulumi.IntPtrOutput `pulumi:"contactPostPassDurationSeconds"`
	// Pre-pass time needed before the contact.
	ContactPrePassDurationSeconds pulumi.IntPtrOutput                   `pulumi:"contactPrePassDurationSeconds"`
	DataflowEdges                 MissionProfileDataflowEdgeArrayOutput `pulumi:"dataflowEdges"`
	// Visibilities with shorter duration than the specified minimum viable contact duration will be ignored when searching for available contacts.
	MinimumViableContactDurationSeconds pulumi.IntOutput `pulumi:"minimumViableContactDurationSeconds"`
	// A name used to identify a mission profile.
	Name              pulumi.StringOutput          `pulumi:"name"`
	Region            pulumi.StringOutput          `pulumi:"region"`
	Tags              MissionProfileTagArrayOutput `pulumi:"tags"`
	TrackingConfigArn pulumi.StringOutput          `pulumi:"trackingConfigArn"`
}

// NewMissionProfile registers a new resource with the given unique name, arguments, and options.
func NewMissionProfile(ctx *pulumi.Context,
	name string, args *MissionProfileArgs, opts ...pulumi.ResourceOption) (*MissionProfile, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DataflowEdges == nil {
		return nil, errors.New("invalid value for required argument 'DataflowEdges'")
	}
	if args.MinimumViableContactDurationSeconds == nil {
		return nil, errors.New("invalid value for required argument 'MinimumViableContactDurationSeconds'")
	}
	if args.TrackingConfigArn == nil {
		return nil, errors.New("invalid value for required argument 'TrackingConfigArn'")
	}
	var resource MissionProfile
	err := ctx.RegisterResource("aws-native:groundstation:MissionProfile", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetMissionProfile gets an existing MissionProfile resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetMissionProfile(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *MissionProfileState, opts ...pulumi.ResourceOption) (*MissionProfile, error) {
	var resource MissionProfile
	err := ctx.ReadResource("aws-native:groundstation:MissionProfile", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering MissionProfile resources.
type missionProfileState struct {
}

type MissionProfileState struct {
}

func (MissionProfileState) ElementType() reflect.Type {
	return reflect.TypeOf((*missionProfileState)(nil)).Elem()
}

type missionProfileArgs struct {
	// Post-pass time needed after the contact.
	ContactPostPassDurationSeconds *int `pulumi:"contactPostPassDurationSeconds"`
	// Pre-pass time needed before the contact.
	ContactPrePassDurationSeconds *int                         `pulumi:"contactPrePassDurationSeconds"`
	DataflowEdges                 []MissionProfileDataflowEdge `pulumi:"dataflowEdges"`
	// Visibilities with shorter duration than the specified minimum viable contact duration will be ignored when searching for available contacts.
	MinimumViableContactDurationSeconds int `pulumi:"minimumViableContactDurationSeconds"`
	// A name used to identify a mission profile.
	Name              *string             `pulumi:"name"`
	Tags              []MissionProfileTag `pulumi:"tags"`
	TrackingConfigArn string              `pulumi:"trackingConfigArn"`
}

// The set of arguments for constructing a MissionProfile resource.
type MissionProfileArgs struct {
	// Post-pass time needed after the contact.
	ContactPostPassDurationSeconds pulumi.IntPtrInput
	// Pre-pass time needed before the contact.
	ContactPrePassDurationSeconds pulumi.IntPtrInput
	DataflowEdges                 MissionProfileDataflowEdgeArrayInput
	// Visibilities with shorter duration than the specified minimum viable contact duration will be ignored when searching for available contacts.
	MinimumViableContactDurationSeconds pulumi.IntInput
	// A name used to identify a mission profile.
	Name              pulumi.StringPtrInput
	Tags              MissionProfileTagArrayInput
	TrackingConfigArn pulumi.StringInput
}

func (MissionProfileArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*missionProfileArgs)(nil)).Elem()
}

type MissionProfileInput interface {
	pulumi.Input

	ToMissionProfileOutput() MissionProfileOutput
	ToMissionProfileOutputWithContext(ctx context.Context) MissionProfileOutput
}

func (*MissionProfile) ElementType() reflect.Type {
	return reflect.TypeOf((**MissionProfile)(nil)).Elem()
}

func (i *MissionProfile) ToMissionProfileOutput() MissionProfileOutput {
	return i.ToMissionProfileOutputWithContext(context.Background())
}

func (i *MissionProfile) ToMissionProfileOutputWithContext(ctx context.Context) MissionProfileOutput {
	return pulumi.ToOutputWithContext(ctx, i).(MissionProfileOutput)
}

type MissionProfileOutput struct{ *pulumi.OutputState }

func (MissionProfileOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**MissionProfile)(nil)).Elem()
}

func (o MissionProfileOutput) ToMissionProfileOutput() MissionProfileOutput {
	return o
}

func (o MissionProfileOutput) ToMissionProfileOutputWithContext(ctx context.Context) MissionProfileOutput {
	return o
}

func (o MissionProfileOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *MissionProfile) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

// Post-pass time needed after the contact.
func (o MissionProfileOutput) ContactPostPassDurationSeconds() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *MissionProfile) pulumi.IntPtrOutput { return v.ContactPostPassDurationSeconds }).(pulumi.IntPtrOutput)
}

// Pre-pass time needed before the contact.
func (o MissionProfileOutput) ContactPrePassDurationSeconds() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *MissionProfile) pulumi.IntPtrOutput { return v.ContactPrePassDurationSeconds }).(pulumi.IntPtrOutput)
}

func (o MissionProfileOutput) DataflowEdges() MissionProfileDataflowEdgeArrayOutput {
	return o.ApplyT(func(v *MissionProfile) MissionProfileDataflowEdgeArrayOutput { return v.DataflowEdges }).(MissionProfileDataflowEdgeArrayOutput)
}

// Visibilities with shorter duration than the specified minimum viable contact duration will be ignored when searching for available contacts.
func (o MissionProfileOutput) MinimumViableContactDurationSeconds() pulumi.IntOutput {
	return o.ApplyT(func(v *MissionProfile) pulumi.IntOutput { return v.MinimumViableContactDurationSeconds }).(pulumi.IntOutput)
}

// A name used to identify a mission profile.
func (o MissionProfileOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *MissionProfile) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

func (o MissionProfileOutput) Region() pulumi.StringOutput {
	return o.ApplyT(func(v *MissionProfile) pulumi.StringOutput { return v.Region }).(pulumi.StringOutput)
}

func (o MissionProfileOutput) Tags() MissionProfileTagArrayOutput {
	return o.ApplyT(func(v *MissionProfile) MissionProfileTagArrayOutput { return v.Tags }).(MissionProfileTagArrayOutput)
}

func (o MissionProfileOutput) TrackingConfigArn() pulumi.StringOutput {
	return o.ApplyT(func(v *MissionProfile) pulumi.StringOutput { return v.TrackingConfigArn }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*MissionProfileInput)(nil)).Elem(), &MissionProfile{})
	pulumi.RegisterOutputType(MissionProfileOutput{})
}
