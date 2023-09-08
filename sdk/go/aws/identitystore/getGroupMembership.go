// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package identitystore

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type Definition for AWS:IdentityStore::GroupMembership
func LookupGroupMembership(ctx *pulumi.Context, args *LookupGroupMembershipArgs, opts ...pulumi.InvokeOption) (*LookupGroupMembershipResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupGroupMembershipResult
	err := ctx.Invoke("aws-native:identitystore:getGroupMembership", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupGroupMembershipArgs struct {
	// The globally unique identifier for the identity store.
	IdentityStoreId string `pulumi:"identityStoreId"`
	// The identifier for a GroupMembership in the identity store.
	MembershipId string `pulumi:"membershipId"`
}

type LookupGroupMembershipResult struct {
	// The unique identifier for a group in the identity store.
	GroupId *string `pulumi:"groupId"`
	// An object containing the identifier of a group member.
	MemberId *GroupMembershipMemberId `pulumi:"memberId"`
	// The identifier for a GroupMembership in the identity store.
	MembershipId *string `pulumi:"membershipId"`
}

func LookupGroupMembershipOutput(ctx *pulumi.Context, args LookupGroupMembershipOutputArgs, opts ...pulumi.InvokeOption) LookupGroupMembershipResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupGroupMembershipResult, error) {
			args := v.(LookupGroupMembershipArgs)
			r, err := LookupGroupMembership(ctx, &args, opts...)
			var s LookupGroupMembershipResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupGroupMembershipResultOutput)
}

type LookupGroupMembershipOutputArgs struct {
	// The globally unique identifier for the identity store.
	IdentityStoreId pulumi.StringInput `pulumi:"identityStoreId"`
	// The identifier for a GroupMembership in the identity store.
	MembershipId pulumi.StringInput `pulumi:"membershipId"`
}

func (LookupGroupMembershipOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupGroupMembershipArgs)(nil)).Elem()
}

type LookupGroupMembershipResultOutput struct{ *pulumi.OutputState }

func (LookupGroupMembershipResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupGroupMembershipResult)(nil)).Elem()
}

func (o LookupGroupMembershipResultOutput) ToLookupGroupMembershipResultOutput() LookupGroupMembershipResultOutput {
	return o
}

func (o LookupGroupMembershipResultOutput) ToLookupGroupMembershipResultOutputWithContext(ctx context.Context) LookupGroupMembershipResultOutput {
	return o
}

func (o LookupGroupMembershipResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupGroupMembershipResult] {
	return pulumix.Output[LookupGroupMembershipResult]{
		OutputState: o.OutputState,
	}
}

// The unique identifier for a group in the identity store.
func (o LookupGroupMembershipResultOutput) GroupId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupGroupMembershipResult) *string { return v.GroupId }).(pulumi.StringPtrOutput)
}

// An object containing the identifier of a group member.
func (o LookupGroupMembershipResultOutput) MemberId() GroupMembershipMemberIdPtrOutput {
	return o.ApplyT(func(v LookupGroupMembershipResult) *GroupMembershipMemberId { return v.MemberId }).(GroupMembershipMemberIdPtrOutput)
}

// The identifier for a GroupMembership in the identity store.
func (o LookupGroupMembershipResultOutput) MembershipId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupGroupMembershipResult) *string { return v.MembershipId }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupGroupMembershipResultOutput{})
}
