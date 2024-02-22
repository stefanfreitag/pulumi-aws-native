// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package transfer

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::Transfer::Profile
type Profile struct {
	pulumi.CustomResourceState

	// Specifies the unique Amazon Resource Name (ARN) for the profile.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// AS2 identifier agreed with a trading partner.
	As2Id pulumi.StringOutput `pulumi:"as2Id"`
	// List of the certificate IDs associated with this profile to be used for encryption and signing of AS2 messages.
	CertificateIds pulumi.StringArrayOutput `pulumi:"certificateIds"`
	// A unique identifier for the profile
	ProfileId pulumi.StringOutput `pulumi:"profileId"`
	// Enum specifying whether the profile is local or associated with a trading partner.
	ProfileType ProfileTypeOutput `pulumi:"profileType"`
	// An array of key-value pairs to apply to this resource.
	Tags aws.TagArrayOutput `pulumi:"tags"`
}

// NewProfile registers a new resource with the given unique name, arguments, and options.
func NewProfile(ctx *pulumi.Context,
	name string, args *ProfileArgs, opts ...pulumi.ResourceOption) (*Profile, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.As2Id == nil {
		return nil, errors.New("invalid value for required argument 'As2Id'")
	}
	if args.ProfileType == nil {
		return nil, errors.New("invalid value for required argument 'ProfileType'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"profileType",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Profile
	err := ctx.RegisterResource("aws-native:transfer:Profile", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetProfile gets an existing Profile resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetProfile(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ProfileState, opts ...pulumi.ResourceOption) (*Profile, error) {
	var resource Profile
	err := ctx.ReadResource("aws-native:transfer:Profile", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Profile resources.
type profileState struct {
}

type ProfileState struct {
}

func (ProfileState) ElementType() reflect.Type {
	return reflect.TypeOf((*profileState)(nil)).Elem()
}

type profileArgs struct {
	// AS2 identifier agreed with a trading partner.
	As2Id string `pulumi:"as2Id"`
	// List of the certificate IDs associated with this profile to be used for encryption and signing of AS2 messages.
	CertificateIds []string `pulumi:"certificateIds"`
	// Enum specifying whether the profile is local or associated with a trading partner.
	ProfileType ProfileType `pulumi:"profileType"`
	// An array of key-value pairs to apply to this resource.
	Tags []aws.Tag `pulumi:"tags"`
}

// The set of arguments for constructing a Profile resource.
type ProfileArgs struct {
	// AS2 identifier agreed with a trading partner.
	As2Id pulumi.StringInput
	// List of the certificate IDs associated with this profile to be used for encryption and signing of AS2 messages.
	CertificateIds pulumi.StringArrayInput
	// Enum specifying whether the profile is local or associated with a trading partner.
	ProfileType ProfileTypeInput
	// An array of key-value pairs to apply to this resource.
	Tags aws.TagArrayInput
}

func (ProfileArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*profileArgs)(nil)).Elem()
}

type ProfileInput interface {
	pulumi.Input

	ToProfileOutput() ProfileOutput
	ToProfileOutputWithContext(ctx context.Context) ProfileOutput
}

func (*Profile) ElementType() reflect.Type {
	return reflect.TypeOf((**Profile)(nil)).Elem()
}

func (i *Profile) ToProfileOutput() ProfileOutput {
	return i.ToProfileOutputWithContext(context.Background())
}

func (i *Profile) ToProfileOutputWithContext(ctx context.Context) ProfileOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ProfileOutput)
}

type ProfileOutput struct{ *pulumi.OutputState }

func (ProfileOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Profile)(nil)).Elem()
}

func (o ProfileOutput) ToProfileOutput() ProfileOutput {
	return o
}

func (o ProfileOutput) ToProfileOutputWithContext(ctx context.Context) ProfileOutput {
	return o
}

// Specifies the unique Amazon Resource Name (ARN) for the profile.
func (o ProfileOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *Profile) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

// AS2 identifier agreed with a trading partner.
func (o ProfileOutput) As2Id() pulumi.StringOutput {
	return o.ApplyT(func(v *Profile) pulumi.StringOutput { return v.As2Id }).(pulumi.StringOutput)
}

// List of the certificate IDs associated with this profile to be used for encryption and signing of AS2 messages.
func (o ProfileOutput) CertificateIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Profile) pulumi.StringArrayOutput { return v.CertificateIds }).(pulumi.StringArrayOutput)
}

// A unique identifier for the profile
func (o ProfileOutput) ProfileId() pulumi.StringOutput {
	return o.ApplyT(func(v *Profile) pulumi.StringOutput { return v.ProfileId }).(pulumi.StringOutput)
}

// Enum specifying whether the profile is local or associated with a trading partner.
func (o ProfileOutput) ProfileType() ProfileTypeOutput {
	return o.ApplyT(func(v *Profile) ProfileTypeOutput { return v.ProfileType }).(ProfileTypeOutput)
}

// An array of key-value pairs to apply to this resource.
func (o ProfileOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v *Profile) aws.TagArrayOutput { return v.Tags }).(aws.TagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ProfileInput)(nil)).Elem(), &Profile{})
	pulumi.RegisterOutputType(ProfileOutput{})
}
