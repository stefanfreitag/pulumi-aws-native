// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cleanrooms

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Represents an AWS account that is a part of a collaboration
type Membership struct {
	pulumi.CustomResourceState

	Arn                           pulumi.StringOutput            `pulumi:"arn"`
	CollaborationArn              pulumi.StringOutput            `pulumi:"collaborationArn"`
	CollaborationCreatorAccountId pulumi.StringOutput            `pulumi:"collaborationCreatorAccountId"`
	CollaborationIdentifier       pulumi.StringOutput            `pulumi:"collaborationIdentifier"`
	MembershipIdentifier          pulumi.StringOutput            `pulumi:"membershipIdentifier"`
	QueryLogStatus                MembershipQueryLogStatusOutput `pulumi:"queryLogStatus"`
	// An arbitrary set of tags (key-value pairs) for this cleanrooms membership.
	Tags MembershipTagArrayOutput `pulumi:"tags"`
}

// NewMembership registers a new resource with the given unique name, arguments, and options.
func NewMembership(ctx *pulumi.Context,
	name string, args *MembershipArgs, opts ...pulumi.ResourceOption) (*Membership, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.CollaborationIdentifier == nil {
		return nil, errors.New("invalid value for required argument 'CollaborationIdentifier'")
	}
	if args.QueryLogStatus == nil {
		return nil, errors.New("invalid value for required argument 'QueryLogStatus'")
	}
	var resource Membership
	err := ctx.RegisterResource("aws-native:cleanrooms:Membership", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetMembership gets an existing Membership resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetMembership(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *MembershipState, opts ...pulumi.ResourceOption) (*Membership, error) {
	var resource Membership
	err := ctx.ReadResource("aws-native:cleanrooms:Membership", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Membership resources.
type membershipState struct {
}

type MembershipState struct {
}

func (MembershipState) ElementType() reflect.Type {
	return reflect.TypeOf((*membershipState)(nil)).Elem()
}

type membershipArgs struct {
	CollaborationIdentifier string                   `pulumi:"collaborationIdentifier"`
	QueryLogStatus          MembershipQueryLogStatus `pulumi:"queryLogStatus"`
	// An arbitrary set of tags (key-value pairs) for this cleanrooms membership.
	Tags []MembershipTag `pulumi:"tags"`
}

// The set of arguments for constructing a Membership resource.
type MembershipArgs struct {
	CollaborationIdentifier pulumi.StringInput
	QueryLogStatus          MembershipQueryLogStatusInput
	// An arbitrary set of tags (key-value pairs) for this cleanrooms membership.
	Tags MembershipTagArrayInput
}

func (MembershipArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*membershipArgs)(nil)).Elem()
}

type MembershipInput interface {
	pulumi.Input

	ToMembershipOutput() MembershipOutput
	ToMembershipOutputWithContext(ctx context.Context) MembershipOutput
}

func (*Membership) ElementType() reflect.Type {
	return reflect.TypeOf((**Membership)(nil)).Elem()
}

func (i *Membership) ToMembershipOutput() MembershipOutput {
	return i.ToMembershipOutputWithContext(context.Background())
}

func (i *Membership) ToMembershipOutputWithContext(ctx context.Context) MembershipOutput {
	return pulumi.ToOutputWithContext(ctx, i).(MembershipOutput)
}

type MembershipOutput struct{ *pulumi.OutputState }

func (MembershipOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Membership)(nil)).Elem()
}

func (o MembershipOutput) ToMembershipOutput() MembershipOutput {
	return o
}

func (o MembershipOutput) ToMembershipOutputWithContext(ctx context.Context) MembershipOutput {
	return o
}

func (o MembershipOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *Membership) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

func (o MembershipOutput) CollaborationArn() pulumi.StringOutput {
	return o.ApplyT(func(v *Membership) pulumi.StringOutput { return v.CollaborationArn }).(pulumi.StringOutput)
}

func (o MembershipOutput) CollaborationCreatorAccountId() pulumi.StringOutput {
	return o.ApplyT(func(v *Membership) pulumi.StringOutput { return v.CollaborationCreatorAccountId }).(pulumi.StringOutput)
}

func (o MembershipOutput) CollaborationIdentifier() pulumi.StringOutput {
	return o.ApplyT(func(v *Membership) pulumi.StringOutput { return v.CollaborationIdentifier }).(pulumi.StringOutput)
}

func (o MembershipOutput) MembershipIdentifier() pulumi.StringOutput {
	return o.ApplyT(func(v *Membership) pulumi.StringOutput { return v.MembershipIdentifier }).(pulumi.StringOutput)
}

func (o MembershipOutput) QueryLogStatus() MembershipQueryLogStatusOutput {
	return o.ApplyT(func(v *Membership) MembershipQueryLogStatusOutput { return v.QueryLogStatus }).(MembershipQueryLogStatusOutput)
}

// An arbitrary set of tags (key-value pairs) for this cleanrooms membership.
func (o MembershipOutput) Tags() MembershipTagArrayOutput {
	return o.ApplyT(func(v *Membership) MembershipTagArrayOutput { return v.Tags }).(MembershipTagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*MembershipInput)(nil)).Elem(), &Membership{})
	pulumi.RegisterOutputType(MembershipOutput{})
}
