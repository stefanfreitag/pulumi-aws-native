// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package managedblockchain

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::ManagedBlockchain::Member
//
// Deprecated: Member is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
type Member struct {
	pulumi.CustomResourceState

	InvitationId         pulumi.StringPtrOutput              `pulumi:"invitationId"`
	MemberConfiguration  MemberMemberConfigurationOutput     `pulumi:"memberConfiguration"`
	MemberId             pulumi.StringOutput                 `pulumi:"memberId"`
	NetworkConfiguration MemberNetworkConfigurationPtrOutput `pulumi:"networkConfiguration"`
	NetworkId            pulumi.StringPtrOutput              `pulumi:"networkId"`
}

// NewMember registers a new resource with the given unique name, arguments, and options.
func NewMember(ctx *pulumi.Context,
	name string, args *MemberArgs, opts ...pulumi.ResourceOption) (*Member, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.MemberConfiguration == nil {
		return nil, errors.New("invalid value for required argument 'MemberConfiguration'")
	}
	var resource Member
	err := ctx.RegisterResource("aws-native:managedblockchain:Member", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetMember gets an existing Member resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetMember(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *MemberState, opts ...pulumi.ResourceOption) (*Member, error) {
	var resource Member
	err := ctx.ReadResource("aws-native:managedblockchain:Member", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Member resources.
type memberState struct {
}

type MemberState struct {
}

func (MemberState) ElementType() reflect.Type {
	return reflect.TypeOf((*memberState)(nil)).Elem()
}

type memberArgs struct {
	InvitationId         *string                     `pulumi:"invitationId"`
	MemberConfiguration  MemberMemberConfiguration   `pulumi:"memberConfiguration"`
	NetworkConfiguration *MemberNetworkConfiguration `pulumi:"networkConfiguration"`
	NetworkId            *string                     `pulumi:"networkId"`
}

// The set of arguments for constructing a Member resource.
type MemberArgs struct {
	InvitationId         pulumi.StringPtrInput
	MemberConfiguration  MemberMemberConfigurationInput
	NetworkConfiguration MemberNetworkConfigurationPtrInput
	NetworkId            pulumi.StringPtrInput
}

func (MemberArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*memberArgs)(nil)).Elem()
}

type MemberInput interface {
	pulumi.Input

	ToMemberOutput() MemberOutput
	ToMemberOutputWithContext(ctx context.Context) MemberOutput
}

func (*Member) ElementType() reflect.Type {
	return reflect.TypeOf((*Member)(nil))
}

func (i *Member) ToMemberOutput() MemberOutput {
	return i.ToMemberOutputWithContext(context.Background())
}

func (i *Member) ToMemberOutputWithContext(ctx context.Context) MemberOutput {
	return pulumi.ToOutputWithContext(ctx, i).(MemberOutput)
}

type MemberOutput struct{ *pulumi.OutputState }

func (MemberOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Member)(nil))
}

func (o MemberOutput) ToMemberOutput() MemberOutput {
	return o
}

func (o MemberOutput) ToMemberOutputWithContext(ctx context.Context) MemberOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(MemberOutput{})
}
